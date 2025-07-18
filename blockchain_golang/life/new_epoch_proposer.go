package life

import (
	"bytes"
	"context"
	"encoding/json"
	"io"
	"net/http"
	"slices"
	"strconv"
	"sync"
	"time"

	"github.com/KlyntarNetwork/Web1337Golang/crypto_primitives/ed25519"
	"github.com/VladChernenko/UndchainCore/common_functions"
	"github.com/VladChernenko/UndchainCore/globals"
	"github.com/VladChernenko/UndchainCore/structures"
	"github.com/VladChernenko/UndchainCore/utils"
)

type Agreement struct {
	PubKey, Sig string
}

type LastLeaderProposition struct {
	EpochIndex, LeaderIndex int
	QuorumAgreements        map[string]string
}

var LAST_LEADER_PROPOSITION = LastLeaderProposition{
	EpochIndex:       -1,
	LeaderIndex:      0,
	QuorumAgreements: make(map[string]string),
}

func NewEpochProposerThread() {

	for {

		globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RLock()

		if utils.EpochStillFresh(&globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler) {

			globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RUnlock()

			time.Sleep(1 * time.Second)

			continue
		}

		epochHandlerRef := &globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.EpochDataHandler

		epochIndex := epochHandlerRef.Id

		// Reset CURRENT_LEADER_STATE only if epoch changed

		if LAST_LEADER_PROPOSITION.EpochIndex != epochIndex {

			LAST_LEADER_PROPOSITION = LastLeaderProposition{
				EpochIndex:       epochIndex,
				LeaderIndex:      0,
				QuorumAgreements: make(map[string]string),
			}

		}

		epochFullId := epochHandlerRef.Hash + "#" + strconv.Itoa(epochHandlerRef.Id)

		leadersSequence := epochHandlerRef.LeadersSequence

		pubKeyOfLeader := leadersSequence[LAST_LEADER_PROPOSITION.LeaderIndex]

		iAmInTheQuorum := slices.Contains(epochHandlerRef.Quorum, globals.CONFIGURATION.PublicKey)

		if iAmInTheQuorum {

			majority := common_functions.GetQuorumMajority(epochHandlerRef)

			var localVotingData structures.PoolVotingStat

			localVotingDataRaw, err := globals.FINALIZATION_VOTING_STATS.Get([]byte(strconv.Itoa(epochIndex)+":"+pubKeyOfLeader), nil)

			if err != nil {

				localVotingData = structures.NewPoolVotingStatTemplate()

			} else {

				json.Unmarshal(localVotingDataRaw, &localVotingData)

			}

			if localVotingData.Index == -1 {

				for position := LAST_LEADER_PROPOSITION.LeaderIndex - 1; position >= 0; position-- {

					prevLeader := epochHandlerRef.LeadersSequence[position]

					prevVotingDataRaw, err := globals.FINALIZATION_VOTING_STATS.Get([]byte(strconv.Itoa(epochIndex)+":"+prevLeader), nil)

					if err == nil {

						var prevVotingData structures.PoolVotingStat

						json.Unmarshal(prevVotingDataRaw, &prevVotingData)

						if prevVotingData.Index > -1 {

							pubKeyOfLeader = prevLeader

							LAST_LEADER_PROPOSITION.LeaderIndex = position

							localVotingData = prevVotingData

							break

						}

					}

				}

			}

			var epochFinishPropositionRequest structures.EpochFinishRequest

			if _, err := globals.EPOCH_DATA.Get([]byte("AEFP:"+strconv.Itoa(epochIndex)), nil); err != nil {

				firstBlockID := strconv.Itoa(epochIndex) + ":" + pubKeyOfLeader + ":0"
				afpForFirstBlockRaw, _ := globals.EPOCH_DATA.Get([]byte("AFP:"+firstBlockID), nil)
				var afpForFirstBlock structures.AggregatedFinalizationProof
				json.Unmarshal(afpForFirstBlockRaw, &afpForFirstBlock)

				epochFinishPropositionRequest = structures.EpochFinishRequest{
					CurrentLeader:        LAST_LEADER_PROPOSITION.LeaderIndex,
					LastBlockProposition: localVotingData,
					AfpForFirstBlock:     afpForFirstBlock,
				}

			} else {

				globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RUnlock()

				time.Sleep(1 * time.Second)

				continue

			}

			quorumMembers := common_functions.GetQuorumUrlsAndPubkeys(epochHandlerRef)

			resultsCh := make(chan Agreement, len(quorumMembers))
			upgradeCh := make(chan structures.EpochFinishResponseUpgrade, len(quorumMembers))

			var wg sync.WaitGroup

			for _, descriptor := range quorumMembers {

				if _, ok := LAST_LEADER_PROPOSITION.QuorumAgreements[descriptor.PubKey]; ok {
					continue
				}

				wg.Add(1)

				go func(desc structures.QuorumMemberData) {
					defer wg.Done()

					body, _ := json.Marshal(epochFinishPropositionRequest)
					ctxReq, cancel := context.WithTimeout(context.Background(), time.Second)
					defer cancel()

					req, _ := http.NewRequestWithContext(ctxReq, "POST", desc.Url+"/epoch_proposition", bytes.NewReader(body))
					req.Header.Set("Content-Type", "application/json")

					client := &http.Client{}
					resp, err := client.Do(req)

					if err != nil {
						return
					}

					defer resp.Body.Close()

					responseBytes, err := io.ReadAll(resp.Body)

					if err != nil {
						return
					}

					var responseStatus structures.ResponseStatus

					if err := json.Unmarshal(responseBytes, &responseStatus); err != nil {
						return
					}

					switch responseStatus.Status {

					case "OK":

						dataToSign := "EPOCH_DONE:" + strconv.Itoa(epochFinishPropositionRequest.CurrentLeader) + ":" +
							strconv.Itoa(epochFinishPropositionRequest.LastBlockProposition.Index) + ":" +
							epochFinishPropositionRequest.LastBlockProposition.Hash + ":" +
							epochFinishPropositionRequest.AfpForFirstBlock.BlockHash + ":" +
							epochFullId

						var resultAsStruct structures.EpochFinishResponseOk

						json.Unmarshal(responseBytes, &resultAsStruct)

						if ed25519.VerifySignature(dataToSign, desc.PubKey, resultAsStruct.Sig) {

							resultsCh <- Agreement{
								PubKey: desc.PubKey,
								Sig:    resultAsStruct.Sig,
							}

						}

					case "UPGRADE":

						var resultAsStruct structures.EpochFinishResponseUpgrade

						json.Unmarshal(responseBytes, &resultAsStruct)

						if common_functions.VerifyAggregatedFinalizationProof(&resultAsStruct.LastBlockProposition.Afp, epochHandlerRef) {

							blockID := strconv.Itoa(epochIndex) + ":" +
								leadersSequence[resultAsStruct.CurrentLeader] + ":" +
								strconv.Itoa(resultAsStruct.LastBlockProposition.Index)

							sameBlockID := blockID == resultAsStruct.LastBlockProposition.Afp.BlockId

							sameHash := resultAsStruct.LastBlockProposition.Hash == resultAsStruct.LastBlockProposition.Afp.BlockHash

							proposedLeaderHasBiggerIndex := resultAsStruct.CurrentLeader > LAST_LEADER_PROPOSITION.LeaderIndex

							if sameBlockID && sameHash && proposedLeaderHasBiggerIndex {
								upgradeCh <- resultAsStruct
							}

						}
					}

				}(descriptor)
			}

			wg.Wait()

			close(resultsCh)
			close(upgradeCh)

			for result := range resultsCh {
				LAST_LEADER_PROPOSITION.QuorumAgreements[result.PubKey] = result.Sig
			}

			for upgradeProposition := range upgradeCh {

				if upgradeProposition.CurrentLeader > LAST_LEADER_PROPOSITION.LeaderIndex {

					LAST_LEADER_PROPOSITION.LeaderIndex = upgradeProposition.CurrentLeader

					// In this case - clear the quorum agreements to try grab proofs for leader with bigger index

					LAST_LEADER_PROPOSITION.QuorumAgreements = make(map[string]string)

				}

			}

			if len(LAST_LEADER_PROPOSITION.QuorumAgreements) >= majority {

				aggregatedEpochFinalizationProof := structures.AggregatedEpochFinalizationProof{
					LastLeader:                   uint(epochFinishPropositionRequest.CurrentLeader),
					LastIndex:                    uint(epochFinishPropositionRequest.LastBlockProposition.Index),
					LastHash:                     epochFinishPropositionRequest.LastBlockProposition.Hash,
					HashOfFirstBlockByLastLeader: epochFinishPropositionRequest.AfpForFirstBlock.BlockHash,
					Proofs:                       LAST_LEADER_PROPOSITION.QuorumAgreements,
				}

				// Make final verification before store to make sure it's indeed a valid proof

				if common_functions.VerifyAggregatedEpochFinalizationProof(&aggregatedEpochFinalizationProof, epochHandlerRef.Quorum, majority, epochFullId) {

					valueAsBytes, _ := json.Marshal(aggregatedEpochFinalizationProof)

					globals.EPOCH_DATA.Put([]byte("AEFP:"+strconv.Itoa(epochIndex)), valueAsBytes, nil)

				}

			}

		}

		globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RUnlock()

		time.Sleep(1 * time.Second)

	}

}
