package life

import (
	"context"
	"encoding/json"
	"net/http"
	"slices"
	"strconv"
	"sync"
	"time"

	"github.com/KlyntarNetwork/Web1337Golang/crypto_primitives/ed25519"
	"github.com/VladChernenko/UndchainCore/block"
	"github.com/VladChernenko/UndchainCore/common_functions"
	"github.com/VladChernenko/UndchainCore/globals"
	"github.com/VladChernenko/UndchainCore/structures"
	"github.com/VladChernenko/UndchainCore/utils"
	ws_structures "github.com/VladChernenko/UndchainCore/websocket"
	"github.com/gorilla/websocket"
	"github.com/syndtr/goleveldb/leveldb"
)

type DoubleMap = map[string]map[string][]byte

var ALRP_METADATA = make(map[string]*structures.AlrpSkeleton) // previousLeaderPubkey => ALRP_METADATA

var WEBSOCKET_CONNECTIONS_FOR_ALRP = make(map[string]*websocket.Conn) // quorumMember => websocket handler

type RotationProofCollector struct {
	wsConnMap map[string]*websocket.Conn
	quorum    []string
	majority  int
	timeout   time.Duration
}

func BlocksGenerationThread() {

	for {

		generateBlock()

		time.Sleep(1 * time.Second)

	}

}

func alrpRequestTemplate(leaderID string, epochHandler *structures.EpochDataHandler) []byte {

	alrpMetadataForPool := ALRP_METADATA[leaderID]

	if alrpMetadataForPool != nil {

		request := ws_structures.WsLeaderRotationProofRequest{
			Route:               "get_leader_rotation_proof",
			IndexOfPoolToRotate: slices.Index(epochHandler.LeadersSequence, leaderID),
			AfpForFirstBlock:    alrpMetadataForPool.AfpForFirstBlock,
			SkipData:            alrpMetadataForPool.SkipData,
		}

		if rawMsg, err := json.Marshal(request); err == nil {

			return rawMsg

		}

	}

	return []byte{}

}

// To grab proofs for multiple previous leaders in a parallel way
func (collector *RotationProofCollector) AlrpForLeadersCollector(ctx context.Context, leaderIDs []string, epochHandler *structures.EpochDataHandler) DoubleMap {

	var wg sync.WaitGroup
	mu := sync.Mutex{}

	result := make(DoubleMap)

	for _, leaderID := range leaderIDs {
		wg.Add(1)

		go func(leaderID string) {

			defer wg.Done()

			waiter := utils.NewQuorumWaiter(len(collector.quorum))

			// Create a timeout for a call
			leaderCtx, cancel := context.WithTimeout(ctx, collector.timeout)
			defer cancel()

			message := alrpRequestTemplate(leaderID, epochHandler)

			responses, ok := waiter.SendAndWait(leaderCtx, message, collector.quorum, collector.wsConnMap, collector.majority)
			if !ok {
				return
			}

			mu.Lock()
			result[leaderID] = responses
			mu.Unlock()

		}(leaderID)
	}

	wg.Wait()
	return result
}

func getTransactionsFromMempool() []structures.Transaction {

	globals.MEMPOOL.Mutex.Lock()
	defer globals.MEMPOOL.Mutex.Unlock()

	limit := globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.NetworkParameters.TxLimitPerBlock

	if limit > len(globals.MEMPOOL.Slice) {
		limit = len(globals.MEMPOOL.Slice)
	}

	transactions := make([]structures.Transaction, limit)

	copy(transactions, globals.MEMPOOL.Slice[:limit])

	globals.MEMPOOL.Slice = globals.MEMPOOL.Slice[limit:]

	return transactions
}

func getAggregatedEpochFinalizationProof(epochHandler *structures.EpochDataHandler) *structures.AggregatedEpochFinalizationProof {

	previousEpochIndex := epochHandler.Id - 1

	// Try to find locally

	aefpProofRaw, err := globals.EPOCH_DATA.Get([]byte("AEFP:"+strconv.Itoa(previousEpochIndex)), nil)

	aefpParsed := new(structures.AggregatedEpochFinalizationProof)

	if parsErr := json.Unmarshal(aefpProofRaw, aefpParsed); parsErr == nil && err == nil {

		return aefpParsed

	}

	quorumUrlsAndPubkeys := common_functions.GetQuorumUrlsAndPubkeys(epochHandler)

	var quorumUrls []string

	for _, quorumMember := range quorumUrlsAndPubkeys {

		quorumUrls = append(quorumUrls, quorumMember.Url)

	}

	allKnownNodes := append(quorumUrls, globals.CONFIGURATION.BootstrapNodes...)

	legacyEpochHandlerRaw, err := globals.EPOCH_DATA.Get([]byte("EPOCH_HANDLER:"+strconv.Itoa(previousEpochIndex)), nil)

	if err != nil {
		return nil
	}

	legacyEpochHandler := new(structures.EpochDataHandler)

	errParse := json.Unmarshal(legacyEpochHandlerRaw, legacyEpochHandler)

	if errParse != nil {
		return nil
	}

	legacyEpochFullID := legacyEpochHandler.Hash + "#" + strconv.Itoa(legacyEpochHandler.Id)

	legacyMajority := common_functions.GetQuorumMajority(legacyEpochHandler)

	legacyQuorum := legacyEpochHandler.Quorum

	// Prepare requests
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()

	resultChan := make(chan structures.AggregatedEpochFinalizationProof, 1)

	var wg sync.WaitGroup

	for _, nodeEndpoint := range allKnownNodes {

		wg.Add(1)

		go func(endpoint string) {
			defer wg.Done()

			reqCtx, reqCancel := context.WithTimeout(ctx, time.Second)
			defer reqCancel()

			finalURL := endpoint + "/aggregated_epoch_finalization_proof/" + strconv.Itoa(previousEpochIndex)

			req, err := http.NewRequestWithContext(reqCtx, "GET", finalURL, nil)
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

			var proofCandidate structures.AggregatedEpochFinalizationProof

			if err := json.NewDecoder(resp.Body).Decode(&proofCandidate); err != nil {
				return
			}

			if common_functions.VerifyAggregatedEpochFinalizationProof(&proofCandidate, legacyQuorum, legacyMajority, legacyEpochFullID) {
				select {
				case resultChan <- proofCandidate:
					cancel() // stop other goroutines
				default:
				}
			}
		}(nodeEndpoint)
	}

	go func() {
		wg.Wait()
		close(resultChan)
	}()

	// We need only first valid result

	aefp, ok := <-resultChan

	if ok {
		return &aefp
	}

	return nil
}

func getAggregatedLeaderRotationProof(majority, epochIndex int, leaderPubkey string) *structures.AggregatedLeaderRotationProof {

	alrpMetadataForPool := ALRP_METADATA[leaderPubkey]

	if alrpMetadataForPool != nil {

		if len(alrpMetadataForPool.Proofs) >= majority {

			// 1. In case in .proofs we have 2/3 votes - return ALRP

			aggregatedLeaderRotationProof := &structures.AggregatedLeaderRotationProof{

				FirstBlockHash: alrpMetadataForPool.AfpForFirstBlock.BlockHash,
				SkipIndex:      alrpMetadataForPool.SkipData.Index,
				SkipHash:       alrpMetadataForPool.SkipData.Hash,
				Proofs:         alrpMetadataForPool.Proofs,
			}

			return aggregatedLeaderRotationProof

		}

	} else {

		// 2. If no data in ALRP_METADATA - create empty template

		skipDataForLeader := structures.PoolVotingStat{}

		keyBytes := []byte(strconv.Itoa(epochIndex) + ":" + leaderPubkey)

		if finStatsRaw, dbErr := globals.FINALIZATION_VOTING_STATS.Get(keyBytes, nil); dbErr == nil {

			if jsonErrParse := json.Unmarshal(finStatsRaw, &skipDataForLeader); jsonErrParse == nil {

				firstBlockID := strconv.Itoa(epochIndex) + ":" + leaderPubkey + ":0"

				if afpForFirstBlockRaw, errAfp := globals.EPOCH_DATA.Get([]byte("AFP:"+firstBlockID), nil); errAfp == nil {

					var afpForFirstBlock structures.AggregatedFinalizationProof

					if errParse := json.Unmarshal(afpForFirstBlockRaw, &afpForFirstBlock); errParse == nil {

						ALRP_METADATA[leaderPubkey] = &structures.AlrpSkeleton{

							AfpForFirstBlock: afpForFirstBlock,

							SkipData: skipDataForLeader,

							Proofs: make(map[string]string),
						}

					}

				}

			}

		}

		if _, alrpDataExists := ALRP_METADATA[leaderPubkey]; !alrpDataExists {

			// Create just empty template

			ALRP_METADATA[leaderPubkey] = structures.NewAlrpSkeletonTemplate()

		}

	}

	return nil

}

func getBatchOfApprovedDelayedTxsByQuorum(indexOfLeader int) structures.DelayedTransactionsBatch {

	epochHandlerRef := &globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.EpochDataHandler

	prevEpochIndex := epochHandlerRef.Id - 2

	if indexOfLeader != 0 {

		return structures.DelayedTransactionsBatch{
			EpochIndex:          prevEpochIndex,
			DelayedTransactions: []map[string]string{},
			Proofs:              map[string]string{},
		}

	}

	// var delayedTransactions []map[string]string

	return structures.DelayedTransactionsBatch{}

}

func generateBlock() {

	globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RLock()

	defer globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RUnlock()

	epochHandlerRef := &globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.EpochDataHandler

	if !utils.EpochStillFresh(&globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler) {

		return

	}

	epochFullID := epochHandlerRef.Hash + "#" + strconv.Itoa(epochHandlerRef.Id)

	epochIndex := epochHandlerRef.Id

	currentLeaderPubKey := epochHandlerRef.LeadersSequence[epochHandlerRef.CurrentLeaderIndex]

	PROOFS_GRABBER_MUTEX.RLock()

	// Safe "if" branch to prevent unnecessary blocks generation

	if currentLeaderPubKey == globals.CONFIGURATION.PublicKey && !(globals.GENERATION_THREAD_METADATA_HANDLER.NextIndex > PROOFS_GRABBER.AcceptedIndex+1) {

		PROOFS_GRABBER_MUTEX.RUnlock()

		var aefpForPreviousEpoch *structures.AggregatedEpochFinalizationProof = nil

		// Check if <epochFullID> is the same in APPROVEMENT_THREAD and in GENERATION_THREAD

		if globals.GENERATION_THREAD_METADATA_HANDLER.EpochFullId != epochFullID {

			// If new epoch - add the aggregated proof of previous epoch finalization

			if epochIndex != 0 {

				aefpForPreviousEpoch = getAggregatedEpochFinalizationProof(epochHandlerRef)

				if aefpForPreviousEpoch == nil {

					return

				}

			}

			// Update the index & hash of epoch

			globals.GENERATION_THREAD_METADATA_HANDLER.EpochFullId = epochFullID

			// Nullish the index & hash in generation thread for new epoch

			globals.GENERATION_THREAD_METADATA_HANDLER.PrevHash = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"

			globals.GENERATION_THREAD_METADATA_HANDLER.NextIndex = 0

			// Open websocket connections with the quorum of new epoch

			utils.OpenWebsocketConnectionsWithQuorum(epochHandlerRef.Quorum, WEBSOCKET_CONNECTIONS_FOR_ALRP)

		}

		extraData := block.ExtraData{}

		if globals.GENERATION_THREAD_METADATA_HANDLER.NextIndex == 0 {

			if epochIndex > 0 {

				if aefpForPreviousEpoch != nil {

					extraData.AefpForPreviousEpoch = aefpForPreviousEpoch

				} else {

					return

				}

			}

			majority := common_functions.GetQuorumMajority(epochHandlerRef)

			// Build the template to insert to the extraData of block. Structure is {pool0:ALRP,...,poolN:ALRP}

			myIndexInLeadersSequence := slices.Index(epochHandlerRef.LeadersSequence, globals.CONFIGURATION.PublicKey)

			if myIndexInLeadersSequence > 0 {

				// Get all previous pools - from zero to <my_position>

				pubKeysOfAllThePreviousPools := slices.Clone(epochHandlerRef.LeadersSequence[:myIndexInLeadersSequence])

				slices.Reverse(pubKeysOfAllThePreviousPools)

				previousToMeLeaderPubKey := epochHandlerRef.LeadersSequence[myIndexInLeadersSequence-1]

				extraData.DelayedTransactionsBatch = getBatchOfApprovedDelayedTxsByQuorum(epochHandlerRef.CurrentLeaderIndex)

				//_____________________ Fill the extraData.aggregatedLeadersRotationProofs _____________________

				alrpsForPreviousLeaders := make(map[string]*structures.AggregatedLeaderRotationProof)

				/*

				   Here we need to fill the object with aggregated leader rotation proofs (ALRPs) for all the previous pools till the pool which was rotated on not-zero height

				   If we can't find all the required ALRPs - skip this iteration to try again later

				*/

				// Add the ALRP for the previous pools in leaders sequence

				pubkeysOfLeadersToGetAlrps := []string{}

				for _, leaderPubKey := range pubKeysOfAllThePreviousPools {

					votingFinalizationStatsPerPool := &structures.PoolVotingStat{
						Index: -1,
					}

					keyBytes := []byte(strconv.Itoa(epochIndex) + ":" + leaderPubKey)

					if finStatsRaw, err := globals.FINALIZATION_VOTING_STATS.Get(keyBytes, nil); err == nil {

						if jsonErrParse := json.Unmarshal(finStatsRaw, votingFinalizationStatsPerPool); jsonErrParse == nil {

							proofThatAtLeastFirstBlockWasCreated := votingFinalizationStatsPerPool.Index >= 0

							// We 100% need ALRP for previous pool
							// But no need in pools who created at least one block in epoch and it's not our previous pool

							if leaderPubKey != previousToMeLeaderPubKey && proofThatAtLeastFirstBlockWasCreated {

								break

							}

						}

					}

					pubkeysOfLeadersToGetAlrps = append(pubkeysOfLeadersToGetAlrps, leaderPubKey)

				}

				breakedCycle := false

				for _, leaderID := range pubkeysOfLeadersToGetAlrps {

					if possibleAlrp := getAggregatedLeaderRotationProof(majority, epochIndex, leaderID); possibleAlrp != nil {

						alrpsForPreviousLeaders[leaderID] = possibleAlrp

					} else {

						breakedCycle = true // this is a signal that we need to initiate ALRP finding process at least one more time

						break
					}

				}

				if breakedCycle {

					// Now when we have a list of previous leader to get ALRP for them - run it

					collector := RotationProofCollector{
						wsConnMap: WEBSOCKET_CONNECTIONS_FOR_ALRP,
						quorum:    epochHandlerRef.Quorum,
						majority:  majority,
						timeout:   5 * time.Second,
					}

					resultsOfAlrpRequests := collector.AlrpForLeadersCollector(context.Background(), pubkeysOfLeadersToGetAlrps, epochHandlerRef)

					// Parse results here and modify the content inside ALRP_METADATA

					for leaderID, validatorsResponses := range resultsOfAlrpRequests {

						if alrpMetadataForPrevLeader, ok := ALRP_METADATA[leaderID]; ok {

							for validatorID, validatorResponse := range validatorsResponses {

								var response structures.ResponseStatus

								if errParse := json.Unmarshal(validatorResponse, &response); errParse == nil {

									if response.Status == "OK" {

										var lrpOk ws_structures.WsLeaderRotationProofResponseOk

										if errParse := json.Unmarshal(validatorResponse, &lrpOk); errParse == nil {

											dataThatShouldBeSigned := "LEADER_ROTATION_PROOF:" + leaderID

											dataThatShouldBeSigned += ":" + alrpMetadataForPrevLeader.AfpForFirstBlock.BlockHash

											dataThatShouldBeSigned += ":" + strconv.Itoa(alrpMetadataForPrevLeader.SkipData.Index)

											dataThatShouldBeSigned += ":" + alrpMetadataForPrevLeader.SkipData.Hash

											dataThatShouldBeSigned += ":" + epochFullID

											if validatorID == lrpOk.Voter && leaderID == lrpOk.ForPoolPubkey && ed25519.VerifySignature(dataThatShouldBeSigned, validatorID, lrpOk.Sig) {

												alrpMetadataForPrevLeader.Proofs[validatorID] = lrpOk.Sig

											}

										}

										if len(alrpMetadataForPrevLeader.Proofs) >= majority {

											break

										}

									} else if response.Status == "UPGRADE" {

										var lrpUpgrade ws_structures.WsLeaderRotationProofResponseUpgrade

										if errParse := json.Unmarshal(validatorResponse, &lrpUpgrade); errParse == nil {

											ourLocalHeightIsLower := alrpMetadataForPrevLeader.SkipData.Index < lrpUpgrade.SkipData.Index

											if ourLocalHeightIsLower {

												blockIdInAfp := strconv.Itoa(epochIndex) + ":" + lrpUpgrade.ForPoolPubkey + strconv.Itoa(lrpUpgrade.SkipData.Index)

												proposedHeightIsValid := lrpUpgrade.SkipData.Hash == lrpUpgrade.AfpForFirstBlock.BlockHash && blockIdInAfp == lrpUpgrade.AfpForFirstBlock.BlockId && common_functions.VerifyAggregatedFinalizationProof(&lrpUpgrade.SkipData.Afp, epochHandlerRef)

												firstBlockID := strconv.Itoa(epochIndex) + ":" + lrpUpgrade.ForPoolPubkey + ":0"

												proposedFirstBlockIsValid := firstBlockID == lrpUpgrade.AfpForFirstBlock.BlockId && common_functions.VerifyAggregatedFinalizationProof(&lrpUpgrade.AfpForFirstBlock, epochHandlerRef)

												if proposedFirstBlockIsValid && proposedHeightIsValid {

													alrpMetadataForPrevLeader.AfpForFirstBlock = lrpUpgrade.AfpForFirstBlock

													alrpMetadataForPrevLeader.SkipData = lrpUpgrade.SkipData

													alrpMetadataForPrevLeader.Proofs = make(map[string]string)

												}

											}

										}

									}

								}

							}

						}

					}

					return

				} else {

					extraData.AggregatedLeadersRotationProofs = alrpsForPreviousLeaders

				}

			}

		}

		extraData.Rest = globals.CONFIGURATION.ExtraDataToBlock

		blockDbAtomicBatch := new(leveldb.Batch)

		blockCandidate := block.NewBlock(getTransactionsFromMempool(), extraData, epochFullID)

		blockHash := blockCandidate.GetHash()

		blockCandidate.Sig = ed25519.GenerateSignature(globals.CONFIGURATION.PrivateKey, blockHash)

		// BlockID has the following format => epochID(epochIndex):Ed25519_Pubkey:IndexOfBlockInCurrentEpoch

		blockID := strconv.Itoa(epochIndex) + ":" + globals.CONFIGURATION.PublicKey + ":" + strconv.Itoa(blockCandidate.Index)

		utils.LogWithTime("New block generated "+blockID, utils.CYAN_COLOR)

		if blockBytes, serializeErr := json.Marshal(blockCandidate); serializeErr == nil {

			globals.GENERATION_THREAD_METADATA_HANDLER.PrevHash = blockHash

			globals.GENERATION_THREAD_METADATA_HANDLER.NextIndex++

			if gtBytes, serializeErr2 := json.Marshal(globals.GENERATION_THREAD_METADATA_HANDLER); serializeErr2 == nil {

				// Store block locally

				blockDbAtomicBatch.Put([]byte(blockID), blockBytes)

				// Update the GENERATION_THREAD after all

				blockDbAtomicBatch.Put([]byte("GT"), gtBytes)

				if err := globals.BLOCKS.Write(blockDbAtomicBatch, nil); err != nil {

					panic("Can't store GT and block candidate")

				}

			}

		}

	} else {

		PROOFS_GRABBER_MUTEX.RUnlock()

	}

}
