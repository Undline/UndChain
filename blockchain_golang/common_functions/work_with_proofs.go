package common_functions

import (
	"context"
	"encoding/json"
	"net/http"
	"slices"
	"strconv"
	"strings"
	"sync"
	"time"

	"github.com/KlyntarNetwork/Web1337Golang/crypto_primitives/ed25519"
	"github.com/VladChernenko/UndchainCore/block"
	"github.com/VladChernenko/UndchainCore/globals"
	"github.com/VladChernenko/UndchainCore/structures"
)

type PivotSearchData struct {
	Position          int
	PivotPubKey       string
	FirstBlockByPivot *block.Block
	FirstBlockHash    string
}

var APPROVEMENT_THREAD_PIVOT, EXECUTION_THREAD_PIVOT *PivotSearchData

func GetBlock(epochIndex int, blockCreator string, index uint, epochHandler *structures.EpochDataHandler) *block.Block {

	blockID := strconv.Itoa(epochIndex) + ":" + blockCreator + ":" + strconv.Itoa(int(index))

	blockAsBytes, err := globals.BLOCKS.Get([]byte(blockID), nil)

	if err == nil {

		var blockParsed *block.Block

		err = json.Unmarshal(blockAsBytes, &blockParsed)

		if err == nil {
			return blockParsed
		}

	}

	// Find from other nodes

	quorumUrlsAndPubkeys := GetQuorumUrlsAndPubkeys(epochHandler)

	var quorumUrls []string

	for _, quorumMember := range quorumUrlsAndPubkeys {

		quorumUrls = append(quorumUrls, quorumMember.Url)

	}

	allKnownNodes := append(quorumUrls, globals.CONFIGURATION.BootstrapNodes...)

	resultChan := make(chan *block.Block, len(allKnownNodes))
	var wg sync.WaitGroup

	for _, node := range allKnownNodes {

		if node == globals.CONFIGURATION.MyHostname {
			continue
		}

		wg.Add(1)
		go func(endpoint string) {

			defer wg.Done()

			ctx, cancel := context.WithTimeout(context.Background(), time.Second)
			defer cancel()

			url := endpoint + "/block/" + blockID
			req, err := http.NewRequestWithContext(ctx, "GET", url, nil)
			if err != nil {
				return
			}

			resp, err := http.DefaultClient.Do(req)
			if err != nil || resp.StatusCode != http.StatusOK {
				return
			}
			defer resp.Body.Close()

			var block block.Block

			if err := json.NewDecoder(resp.Body).Decode(&block); err == nil {
				resultChan <- &block
			}

		}(node)

	}

	go func() {
		wg.Wait()
		close(resultChan)
	}()

	for block := range resultChan {
		if block != nil {
			return block
		}
	}

	return nil
}

func VerifyAggregatedEpochFinalizationProof(
	proofStruct *structures.AggregatedEpochFinalizationProof,
	quorum []string,
	majority int,
	epochFullID string,
) bool {

	dataThatShouldBeSigned := "EPOCH_DONE:" +
		strconv.Itoa(int(proofStruct.LastLeader)) + ":" +
		strconv.Itoa(int(proofStruct.LastIndex)) + ":" +
		proofStruct.LastHash + ":" +
		proofStruct.HashOfFirstBlockByLastLeader + ":" +
		epochFullID

	okSignatures := 0
	seen := make(map[string]bool)
	quorumMap := make(map[string]bool)

	for _, pk := range quorum {
		quorumMap[strings.ToLower(pk)] = true
	}

	for pubKey, signature := range proofStruct.Proofs {

		if ed25519.VerifySignature(dataThatShouldBeSigned, pubKey, signature) {
			loweredPubKey := strings.ToLower(pubKey)
			if quorumMap[loweredPubKey] && !seen[loweredPubKey] {
				seen[loweredPubKey] = true
				okSignatures++
			}
		}
	}

	return okSignatures >= majority

}

func VerifyAggregatedFinalizationProof(
	proof *structures.AggregatedFinalizationProof,
	epochHandler *structures.EpochDataHandler,
) bool {

	epochFullID := epochHandler.Hash + "#" + strconv.Itoa(epochHandler.Id)

	dataThatShouldBeSigned := proof.PrevBlockHash + proof.BlockId + proof.BlockHash + epochFullID

	majority := GetQuorumMajority(epochHandler)

	okSignatures := 0

	seen := make(map[string]bool)

	quorumMap := make(map[string]bool)

	for _, pk := range epochHandler.Quorum {
		quorumMap[strings.ToLower(pk)] = true
	}

	for pubKey, signature := range proof.Proofs {

		if ed25519.VerifySignature(dataThatShouldBeSigned, pubKey, signature) {

			loweredPubKey := strings.ToLower(pubKey)

			if quorumMap[loweredPubKey] && !seen[loweredPubKey] {
				seen[loweredPubKey] = true
				okSignatures++
			}
		}
	}

	return okSignatures >= majority
}

func VerifyAggregatedLeaderRotationProof(
	pubKeyOfSomePreviousLeader string,
	proof *structures.AggregatedLeaderRotationProof,
	epochHandler *structures.EpochDataHandler,
) bool {

	epochFullID := epochHandler.Hash + "#" + strconv.Itoa(epochHandler.Id)

	dataThatShouldBeSigned := "LEADER_ROTATION_PROOF:" + pubKeyOfSomePreviousLeader + ":" +
		proof.FirstBlockHash + ":" +
		strconv.Itoa(proof.SkipIndex) + ":" +
		proof.SkipHash + ":" +
		epochFullID

	majority := GetQuorumMajority(epochHandler)

	okSignatures := 0
	seen := make(map[string]bool)
	quorumMap := make(map[string]bool)

	for _, pk := range epochHandler.Quorum {
		quorumMap[strings.ToLower(pk)] = true
	}

	for pubKey, signature := range proof.Proofs {

		if ed25519.VerifySignature(dataThatShouldBeSigned, pubKey, signature) {

			loweredPubKey := strings.ToLower(pubKey)

			if quorumMap[loweredPubKey] && !seen[loweredPubKey] {
				seen[loweredPubKey] = true
				okSignatures++
			}

		}

	}

	return okSignatures >= majority

}

func CheckAlrpChainValidity(firstBlockInThisEpochByPool *block.Block, epochHandler *structures.EpochDataHandler, position int) bool {

	aggregatedLeadersRotationProofsRef := firstBlockInThisEpochByPool.ExtraData.AggregatedLeadersRotationProofs

	arrayIndexer := 0

	arrayForIteration := slices.Clone(epochHandler.LeadersSequence[:position])

	slices.Reverse(arrayForIteration) // we need reversed version

	bumpedWithPoolWhoCreatedAtLeastOneBlock := false

	for _, poolPubKey := range arrayForIteration {

		if alrpForThisPool, ok := aggregatedLeadersRotationProofsRef[poolPubKey]; ok {

			signaIsOk := VerifyAggregatedLeaderRotationProof(poolPubKey, alrpForThisPool, epochHandler)

			if signaIsOk {

				arrayIndexer++

				if alrpForThisPool.SkipIndex >= 0 {

					bumpedWithPoolWhoCreatedAtLeastOneBlock = true

					break

				}

			} else {

				return false

			}

		} else {

			return false

		}

	}

	if arrayIndexer == position || bumpedWithPoolWhoCreatedAtLeastOneBlock {

		return true

	}

	return false

}

func ExtendedCheckAlrpChainValidity(firstBlockInThisEpochByPool *block.Block, epochHandler *structures.EpochDataHandler, position int, dontCheckSigna bool) (bool, map[string]structures.ExecutionStatsPerPool) {

	aggregatedLeadersRotationProofsRef := firstBlockInThisEpochByPool.ExtraData.AggregatedLeadersRotationProofs

	infoAboutFinalBlocksInThisEpoch := make(map[string]structures.ExecutionStatsPerPool)

	arrayIndexer := 0

	arrayForIteration := slices.Clone(epochHandler.LeadersSequence[:position])

	slices.Reverse(arrayForIteration) // we need reversed version

	bumpedWithPoolWhoCreatedAtLeastOneBlock := false

	for _, poolPubKey := range arrayForIteration {

		if alrpForThisPool, ok := aggregatedLeadersRotationProofsRef[poolPubKey]; ok {

			signaIsOk := dontCheckSigna || VerifyAggregatedLeaderRotationProof(poolPubKey, alrpForThisPool, epochHandler)

			if signaIsOk {

				infoAboutFinalBlocksInThisEpoch[poolPubKey] = structures.ExecutionStatsPerPool{
					Index:          alrpForThisPool.SkipIndex,
					Hash:           alrpForThisPool.SkipHash,
					FirstBlockHash: alrpForThisPool.FirstBlockHash,
				}

				arrayIndexer++

				if alrpForThisPool.SkipIndex >= 0 {

					bumpedWithPoolWhoCreatedAtLeastOneBlock = true

					break

				}

			} else {

				return false, make(map[string]structures.ExecutionStatsPerPool)

			}

		} else {

			return false, make(map[string]structures.ExecutionStatsPerPool)

		}

	}

	if arrayIndexer == position || bumpedWithPoolWhoCreatedAtLeastOneBlock {

		return true, infoAboutFinalBlocksInThisEpoch

	}

	return false, make(map[string]structures.ExecutionStatsPerPool)

}

func GetFirstBlockInEpoch(epochHandler *structures.EpochDataHandler, threadType string) *structures.FirstBlockResult {

	var pivotData *PivotSearchData = APPROVEMENT_THREAD_PIVOT

	if threadType == "EXECUTION" {

		pivotData = EXECUTION_THREAD_PIVOT

	}

	if pivotData == nil {

		allKnownNodes := GetQuorumUrlsAndPubkeys(epochHandler)

		var wg sync.WaitGroup

		responses := make(chan *structures.FirstBlockAssumption, len(allKnownNodes))

		for _, node := range allKnownNodes {
			wg.Add(1)

			go func(nodeUrl string) {
				defer wg.Done()

				ctx, cancel := context.WithTimeout(context.Background(), time.Second)
				defer cancel()

				req, err := http.NewRequestWithContext(ctx, "GET", nodeUrl+"/first_block_assumption/"+strconv.Itoa(epochHandler.Id), nil)
				if err != nil {
					return
				}

				resp, err := http.DefaultClient.Do(req)
				if err != nil {
					return
				}
				defer resp.Body.Close()

				var prop structures.FirstBlockAssumption
				if err := json.NewDecoder(resp.Body).Decode(&prop); err != nil {
					return
				}

				responses <- &prop
			}(node.Url)
		}

		wg.Wait()

		close(responses)

		minimalIndexOfLeader := 1_000_000_000

		var afpForSecondBlock *structures.AggregatedFinalizationProof

		for prop := range responses {

			if prop == nil {
				continue
			}

			if prop.IndexOfFirstBlockCreator < 0 || prop.IndexOfFirstBlockCreator >= len(epochHandler.LeadersSequence) {
				continue
			}

			firstBlockCreator := epochHandler.LeadersSequence[prop.IndexOfFirstBlockCreator]

			if VerifyAggregatedFinalizationProof(&prop.AfpForSecondBlock, epochHandler) {

				expectedSecondBlockID := strconv.Itoa(epochHandler.Id) + ":" + firstBlockCreator + ":1"

				if expectedSecondBlockID == prop.AfpForSecondBlock.BlockId && prop.IndexOfFirstBlockCreator < minimalIndexOfLeader {

					minimalIndexOfLeader = prop.IndexOfFirstBlockCreator

					afpForSecondBlock = &prop.AfpForSecondBlock

				}

			}

		}

		if afpForSecondBlock != nil {

			position := minimalIndexOfLeader

			pivotPubKey := epochHandler.LeadersSequence[position]

			firstBlockByPivot := GetBlock(epochHandler.Id, pivotPubKey, uint(0), epochHandler)

			firstBlockHash := afpForSecondBlock.PrevBlockHash

			if firstBlockByPivot != nil && firstBlockHash == firstBlockByPivot.GetHash() {

				pivotData = &PivotSearchData{

					Position:          position,
					PivotPubKey:       pivotPubKey,
					FirstBlockByPivot: firstBlockByPivot,
					FirstBlockHash:    firstBlockHash,
				}
			}
		}
	}

	if pivotData != nil {

		// In pivot we have first block created in epoch by some pool

		// Try to move closer to the beginning of the epochHandler.leadersSequence to find the real first block

		// Based on ALRP in pivot block - find the real first block

		blockToEnumerateAlrp := pivotData.FirstBlockByPivot

		if pivotData.Position == 0 {

			defer func() {

				if threadType == "EXECUTION" {

					EXECUTION_THREAD_PIVOT = nil

				} else {
					APPROVEMENT_THREAD_PIVOT = nil
				}

			}()

			return &structures.FirstBlockResult{

				FirstBlockCreator: pivotData.PivotPubKey,
				FirstBlockHash:    pivotData.FirstBlockHash,
			}
		}

		for position := pivotData.Position - 1; position >= 0; position-- {

			previousPool := epochHandler.LeadersSequence[position]

			leaderRotationProof := blockToEnumerateAlrp.ExtraData.AggregatedLeadersRotationProofs[previousPool]

			if position == 0 {

				defer func() {

					if threadType == "EXECUTION" {

						EXECUTION_THREAD_PIVOT = nil

					} else {
						APPROVEMENT_THREAD_PIVOT = nil
					}

				}()

				if leaderRotationProof.SkipIndex == -1 {
					return &structures.FirstBlockResult{
						FirstBlockCreator: pivotData.PivotPubKey,
						FirstBlockHash:    pivotData.FirstBlockHash,
					}
				} else {
					return &structures.FirstBlockResult{
						FirstBlockCreator: previousPool,
						FirstBlockHash:    leaderRotationProof.FirstBlockHash,
					}
				}

			} else if leaderRotationProof.SkipIndex != -1 {

				// Found new potential pivot

				firstBlockByNewPivot := GetBlock(epochHandler.Id, previousPool, 0, epochHandler)

				if firstBlockByNewPivot == nil {
					return nil
				}

				if firstBlockByNewPivot.GetHash() == leaderRotationProof.FirstBlockHash {

					pivotData.Position = position

					pivotData.PivotPubKey = previousPool

					pivotData.FirstBlockByPivot = firstBlockByNewPivot

					pivotData.FirstBlockHash = leaderRotationProof.FirstBlockHash

					break // break cycle to run the cycle later with new pivot

				} else {

					return nil

				}
			}
		}
	}

	return nil

}

func GetVerifiedAggregatedFinalizationProofByBlockId(blockID string, epochHandler *structures.EpochDataHandler) *structures.AggregatedFinalizationProof {

	localAfpAsBytes, err := globals.EPOCH_DATA.Get([]byte("AFP:"+blockID), nil)

	if err == nil {

		var localAfpParsed *structures.AggregatedFinalizationProof

		err = json.Unmarshal(localAfpAsBytes, &localAfpParsed)

		if err != nil {
			return nil
		}

		return localAfpParsed

	}

	quorum := GetQuorumUrlsAndPubkeys(epochHandler)

	resultChan := make(chan *structures.AggregatedFinalizationProof, len(quorum))

	var wg sync.WaitGroup

	for _, node := range quorum {
		wg.Add(1)
		go func(endpoint string) {
			defer wg.Done()

			ctx, cancel := context.WithTimeout(context.Background(), time.Second)
			defer cancel()

			req, err := http.NewRequestWithContext(ctx, "GET", endpoint+"/aggregated_finalization_proof/"+blockID, nil)
			if err != nil {
				return
			}

			resp, err := http.DefaultClient.Do(req)
			if err != nil {
				return
			}
			defer resp.Body.Close()

			if resp.StatusCode != http.StatusOK {
				return
			}

			var afp structures.AggregatedFinalizationProof
			if err := json.NewDecoder(resp.Body).Decode(&afp); err != nil {
				return
			}

			if VerifyAggregatedFinalizationProof(&afp, epochHandler) {
				resultChan <- &afp
			}
		}(node.Url)
	}

	go func() {
		wg.Wait()
		close(resultChan)
	}()

	// Return first valid AFP
	for res := range resultChan {
		if res != nil {
			return res
		}
	}

	return nil
}
