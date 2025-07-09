package websocket

import (
	"encoding/json"
	"slices"
	"strconv"
	"strings"
	"sync"

	"github.com/KlyntarNetwork/Web1337Golang/crypto_primitives/ed25519"
	"github.com/VladChernenko/UndchainCore/common_functions"
	"github.com/VladChernenko/UndchainCore/globals"
	"github.com/VladChernenko/UndchainCore/structures"
	"github.com/VladChernenko/UndchainCore/utils"
	"github.com/lxzan/gws"
)

// Only one block creator can request proof for block at a choosen period of time T
var BLOCK_CREATOR_REQUEST_MUTEX = sync.Mutex{}

func GetFinalizationProof(parsedRequest WsFinalizationProofRequest, connection *gws.Conn) {

	globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RLock()

	defer globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RUnlock()

	epochHandler := &globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.EpochDataHandler

	epochIndex := epochHandler.Id

	epochFullID := epochHandler.Hash + "#" + strconv.Itoa(epochIndex)

	itsLeader := epochHandler.LeadersSequence[epochHandler.CurrentLeaderIndex] == parsedRequest.Block.Creator

	if itsLeader {

		localVotingDataForPool := structures.NewPoolVotingStatTemplate()

		localVotingDataRaw, err := globals.FINALIZATION_VOTING_STATS.Get([]byte(strconv.Itoa(epochIndex)+":"+parsedRequest.Block.Creator), nil)

		if err == nil {

			json.Unmarshal(localVotingDataRaw, &localVotingDataForPool)

		}

		proposedBlockHash := parsedRequest.Block.GetHash()

		itsSameChainSegment := localVotingDataForPool.Index < int(parsedRequest.Block.Index) || localVotingDataForPool.Index == int(parsedRequest.Block.Index) && proposedBlockHash == localVotingDataForPool.Hash && parsedRequest.Block.Epoch == epochFullID

		if itsSameChainSegment {

			proposedBlockId := strconv.Itoa(epochIndex) + ":" + parsedRequest.Block.Creator + ":" + strconv.Itoa(int(parsedRequest.Block.Index))

			previousBlockIndex := int(parsedRequest.Block.Index - 1)

			var futureVotingDataToStore structures.PoolVotingStat

			positionOfBlockCreatorInLeadersSequence := slices.Index(epochHandler.LeadersSequence, parsedRequest.Block.Creator)

			if parsedRequest.Block.VerifySignature() && !utils.SignalAboutEpochRotationExists(epochIndex) {

				BLOCK_CREATOR_REQUEST_MUTEX.Lock()

				defer BLOCK_CREATOR_REQUEST_MUTEX.Unlock()

				if localVotingDataForPool.Index == int(parsedRequest.Block.Index) {

					futureVotingDataToStore = localVotingDataForPool

				} else {

					futureVotingDataToStore = structures.PoolVotingStat{

						Index: previousBlockIndex,

						Hash: parsedRequest.PreviousBlockAfp.BlockHash,

						Afp: parsedRequest.PreviousBlockAfp,
					}

				}

				if parsedRequest.Block.Index == 0 {

					aefpIsOk := false

					if epochIndex == 0 {

						aefpIsOk = true

					} else {

						var legacyEpochHandler structures.EpochDataHandler

						prevEpochIndex := epochHandler.Id - 1

						legacyEpochHandlerRaw, err := globals.EPOCH_DATA.Get([]byte("EPOCH_HANDLER:"+strconv.Itoa(prevEpochIndex)), nil)

						if err == nil {

							errParse := json.Unmarshal(legacyEpochHandlerRaw, &legacyEpochHandler)

							aefpFromBlock := parsedRequest.Block.ExtraData.AefpForPreviousEpoch

							if errParse == nil {

								legacyEpochFullID := legacyEpochHandler.Hash + "#" + strconv.Itoa(legacyEpochHandler.Id)

								legacyMajority := common_functions.GetQuorumMajority(&legacyEpochHandler)

								aefpIsOk = epochHandler.Id == 0 || common_functions.VerifyAggregatedEpochFinalizationProof(

									aefpFromBlock,

									legacyEpochHandler.Quorum,

									legacyMajority,

									legacyEpochFullID,
								)

							}

						}

					}

					//_________________________________________2_________________________________________

					// Verify the ALRP chain validity here

					alrpChainIsOk := common_functions.CheckAlrpChainValidity(

						&parsedRequest.Block, epochHandler, positionOfBlockCreatorInLeadersSequence,
					)

					if !aefpIsOk || !alrpChainIsOk {

						// Prevent proof generation

						return

					}

				} else {

					// This branch related to case when block index is > 0 (so it's not the first block by pool)

					previousBlockId := strconv.Itoa(epochIndex) + ":" + parsedRequest.Block.Creator + ":" + strconv.Itoa(previousBlockIndex)

					// Check if AFP inside related to previous block AFP

					if previousBlockId == parsedRequest.PreviousBlockAfp.BlockId && common_functions.VerifyAggregatedFinalizationProof(&parsedRequest.PreviousBlockAfp, epochHandler) {

						// In case it's request for the third block, we'll receive AFP for the second block which includes .prevBlockHash field
						// This will be the assumption of hash of the first block in epoch

						if parsedRequest.Block.Index == 2 {

							keyBytes := []byte("FIRST_BLOCK_ASSUMPTION:" + strconv.Itoa(epochIndex))

							_, err := globals.EPOCH_DATA.Get(keyBytes, nil)

							// We need to store first block assumption only in case we don't have it yet

							if err != nil {

								assumption := structures.FirstBlockAssumption{

									IndexOfFirstBlockCreator: positionOfBlockCreatorInLeadersSequence,

									AfpForSecondBlock: parsedRequest.PreviousBlockAfp,
								}

								valBytes, _ := json.Marshal(assumption)

								globals.EPOCH_DATA.Put(keyBytes, valBytes, nil)

							}

						}

					} else {

						return

					}

				}

				// Store the block and return finalization proof

				blockBytes, err := json.Marshal(parsedRequest.Block)

				if err == nil {

					// 1. Store the block

					err = globals.BLOCKS.Put([]byte(proposedBlockId), blockBytes, nil)

					if err == nil {

						afpBytes, err := json.Marshal(parsedRequest.PreviousBlockAfp)

						if err == nil {

							// 2. Store the AFP for previous block

							errStore := globals.EPOCH_DATA.Put([]byte("AFP:"+proposedBlockId), afpBytes, nil)

							votingStatBytes, errParse := json.Marshal(futureVotingDataToStore)

							if errStore == nil && errParse == nil {

								// 3. Store the voting stats

								err := globals.FINALIZATION_VOTING_STATS.Put([]byte(strconv.Itoa(epochIndex)+":"+parsedRequest.Block.Creator), votingStatBytes, nil)

								if err == nil {

									// Only after we stored the these 3 components = generate signature (finalization proof)

									dataToSign, prevBlockHash := "", ""

									if parsedRequest.Block.Index == 0 {

										prevBlockHash = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"

									} else {

										prevBlockHash = parsedRequest.PreviousBlockAfp.BlockHash

									}

									dataToSign += prevBlockHash + proposedBlockId + proposedBlockHash + epochFullID

									response := WsFinalizationProofResponse{
										Voter:             globals.CONFIGURATION.PublicKey,
										FinalizationProof: ed25519.GenerateSignature(globals.CONFIGURATION.PrivateKey, dataToSign),
										VotedForHash:      proposedBlockHash,
									}

									jsonResponse, err := json.Marshal(response)

									if err == nil {

										connection.WriteMessage(gws.OpcodeText, jsonResponse)

									}

								}

							}

						}

					}

				}

			}

		}

	}

}

func GetLeaderRotationProof(parsedRequest WsLeaderRotationProofRequest, connection *gws.Conn) {

	globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RLock()

	defer globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RUnlock()

	epochHandler := &globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.EpochDataHandler

	epochIndex := epochHandler.Id

	epochFullID := epochHandler.Hash + "#" + strconv.Itoa(epochIndex)

	poolToRotate := epochHandler.LeadersSequence[parsedRequest.IndexOfPoolToRotate]

	if epochHandler.CurrentLeaderIndex > parsedRequest.IndexOfPoolToRotate {

		localVotingData := structures.NewPoolVotingStatTemplate()

		localVotingDataRaw, err := globals.FINALIZATION_VOTING_STATS.Get([]byte(strconv.Itoa(epochIndex)+":"+poolToRotate), nil)

		if err == nil {

			json.Unmarshal(localVotingDataRaw, &localVotingData)

		}

		propSkipData := parsedRequest.SkipData

		if localVotingData.Index > propSkipData.Index {

			// Try to return with AFP for the first block

			firstBlockID := strconv.Itoa(epochHandler.Id) + ":" + poolToRotate + ":0"

			afpForFirstBlockBytes, err := globals.EPOCH_DATA.Get([]byte("AFP:"+firstBlockID), nil)

			if err == nil {

				var afpForFirstBlock structures.AggregatedFinalizationProof

				err := json.Unmarshal(afpForFirstBlockBytes, &afpForFirstBlock)

				if err == nil {

					responseData := WsLeaderRotationProofResponseUpgrade{
						Voter:            globals.CONFIGURATION.PublicKey,
						ForPoolPubkey:    poolToRotate,
						Status:           "UPGRADE",
						AfpForFirstBlock: afpForFirstBlock,
						SkipData:         localVotingData,
					}

					jsonResponse, err := json.Marshal(responseData)

					if err == nil {

						connection.WriteMessage(gws.OpcodeText, jsonResponse)

					}

				}

			}

		} else {

			//________________________________________________ Verify the proposed AFP ________________________________________________

			afpIsOk := false

			parts := strings.Split(propSkipData.Afp.BlockId, ":")

			if len(parts) != 3 {
				return
			}

			indexOfBlockInAfp, err := strconv.Atoi(parts[2])

			if err != nil {
				return
			}

			if propSkipData.Index > -1 && propSkipData.Hash == propSkipData.Afp.BlockHash && propSkipData.Index == indexOfBlockInAfp {

				afpIsOk = common_functions.VerifyAggregatedFinalizationProof(&propSkipData.Afp, epochHandler)

			} else {

				afpIsOk = true
			}

			if afpIsOk {

				dataToSignForLeaderRotation, firstBlockAfpIsOk := "", false

				if parsedRequest.SkipData.Index == -1 {

					dataToSignForLeaderRotation := "LEADER_ROTATION_PROOF:" + poolToRotate

					dataToSignForLeaderRotation += ":0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef:-1"

					dataToSignForLeaderRotation += ":0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef:" + epochFullID

					firstBlockAfpIsOk = true

				} else if parsedRequest.SkipData.Index >= 0 {

					blockIdOfFirstBlock := strconv.Itoa(epochIndex) + ":" + poolToRotate + ":0"

					blockIdsTheSame := parsedRequest.AfpForFirstBlock.BlockId == blockIdOfFirstBlock

					if blockIdsTheSame && common_functions.VerifyAggregatedFinalizationProof(&parsedRequest.AfpForFirstBlock, epochHandler) {

						firstBlockHash := parsedRequest.AfpForFirstBlock.BlockHash

						dataToSignForLeaderRotation := "LEADER_ROTATION_PROOF:" + poolToRotate

						dataToSignForLeaderRotation += ":" + firstBlockHash

						dataToSignForLeaderRotation += ":" + strconv.Itoa(propSkipData.Index)

						dataToSignForLeaderRotation += ":" + propSkipData.Hash

						dataToSignForLeaderRotation += ":" + epochFullID

						firstBlockAfpIsOk = true

					}

				}

				// If proof is ok - generate LRP(leader rotation proof)

				if firstBlockAfpIsOk {

					leaderRotationProofMessage := WsLeaderRotationProofResponseOk{

						Voter: globals.CONFIGURATION.PublicKey,

						ForPoolPubkey: poolToRotate,

						Status: "OK",

						Sig: ed25519.GenerateSignature(globals.CONFIGURATION.PrivateKey, dataToSignForLeaderRotation),
					}

					jsonResponse, err := json.Marshal(leaderRotationProofMessage)

					if err == nil {

						connection.WriteMessage(gws.OpcodeText, jsonResponse)

					}

				}

			}

		}

	}

}
