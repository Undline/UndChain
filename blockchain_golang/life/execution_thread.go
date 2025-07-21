package life

import (
	"encoding/json"
	"strconv"

	"github.com/VladChernenko/UndchainCore/block"
	"github.com/VladChernenko/UndchainCore/common_functions"
	"github.com/VladChernenko/UndchainCore/globals"
	"github.com/VladChernenko/UndchainCore/structures"
	"github.com/VladChernenko/UndchainCore/utils"
)

func ExecutionThread() {

	for {

		globals.EXECUTION_THREAD_METADATA_HANDLER.RWMutex.RLock()

		epochHandlerRef := &globals.EXECUTION_THREAD_METADATA_HANDLER.Handler

		currentEpochIsFresh := utils.EpochStillFresh(epochHandlerRef)

		// Struct is {currentLeader,currentToVerify,infoAboutFinalBlocksInThisEpoch:{poolPubKey:{index,hash}}}
		//alignmentData := globals.EXECUTION_THREAD_METADATA_HANDLER.Handler.CurrentEpochAlignmentData

		shouldMoveToNextEpoch := false

		if epochHandlerRef.LegacyEpochAlignmentData.Activated {

			infoFromAefpAboutLastBlocksByPools := epochHandlerRef.LegacyEpochAlignmentData.InfoAboutLastBlocksInEpoch

			var localExecMetadataForLeader, metadataFromAefpForLeader structures.ExecutionStatsPerPool

			dataExists := false

			for {

				indexOfLeaderToExec := epochHandlerRef.LegacyEpochAlignmentData.CurrentToExecute

				pubKeyOfLeader := epochHandlerRef.EpochDataHandler.LeadersSequence[indexOfLeaderToExec]

				localExecMetadataForLeader = epochHandlerRef.ExecutionData[pubKeyOfLeader]

				metadataFromAefpForLeader, dataExists = infoFromAefpAboutLastBlocksByPools[pubKeyOfLeader]

				if !dataExists {

					metadataFromAefpForLeader = structures.NewExecutionStatsTemplate()
				}

				finishedToExecBlocksByThisLeader := localExecMetadataForLeader.Index == metadataFromAefpForLeader.Index

				if finishedToExecBlocksByThisLeader {

					itsTheLastBlockInSequence := len(epochHandlerRef.EpochDataHandler.LeadersSequence) == indexOfLeaderToExec+1

					if itsTheLastBlockInSequence {

						break

					} else {

						epochHandlerRef.LegacyEpochAlignmentData.CurrentToExecute++

						continue

					}

				}

				/*

					Next:

					1) Check connection with pool or point of blocks distribution

					2) Fetch blocks

					3) Execute


				*/

			}

			allBlocksWereExecutedInLegacyEpoch := len(epochHandlerRef.EpochDataHandler.LeadersSequence) == epochHandlerRef.LegacyEpochAlignmentData.CurrentToExecute+1

			finishedToExecBlocksByLastLeader := localExecMetadataForLeader.Index == metadataFromAefpForLeader.Index

			if allBlocksWereExecutedInLegacyEpoch && finishedToExecBlocksByLastLeader {

				shouldMoveToNextEpoch = true
			}

		} else if currentEpochIsFresh && epochHandlerRef.CurrentEpochAlignmentData.Activated {

			// Take the pool by it's position

			currentEpochAlignmentData := &epochHandlerRef.CurrentEpochAlignmentData

			leaderPubkeyToExecBlocks := epochHandlerRef.EpochDataHandler.LeadersSequence[currentEpochAlignmentData.CurrentToExecute]

			execStatsOfLeader := epochHandlerRef.ExecutionData[leaderPubkeyToExecBlocks] // {index,hash}

			infoAboutLastBlockByThisLeader, exists := currentEpochAlignmentData.InfoAboutLastBlocksInEpoch[leaderPubkeyToExecBlocks] // {index,hash}

			if exists && execStatsOfLeader.Index == infoAboutLastBlockByThisLeader.Index {

				// Move to next one

				epochHandlerRef.CurrentEpochAlignmentData.CurrentToExecute++

				if !currentEpochIsFresh {

					TryToFinishCurrentEpoch(&epochHandlerRef.EpochDataHandler)

				}

				// TODO: Here we need to skip the following logic and start next iteration
				// TODO: Cope with mutexes here
				continue

			}

			// Try check if we have established a WSS channel to fetch blocks

			// Now, when we have connection with some entity which has an ability to give us blocks via WS(s) tunnel

		}

		if !currentEpochIsFresh && !epochHandlerRef.LegacyEpochAlignmentData.Activated {

			TryToFinishCurrentEpoch(&epochHandlerRef.EpochDataHandler)

		}

		if shouldMoveToNextEpoch {

			SetupNextEpoch(&epochHandlerRef.EpochDataHandler)

		}

	}

}

func ExecuteBlock(block *block.Block) {

	if globals.EXECUTION_THREAD_METADATA_HANDLER.Handler.ExecutionData[block.Creator].Hash == block.PrevHash {
		// Stub
	}

}

func ExecuteTransaction(tx *structures.Transaction) {}

/*
The following 3 functions are responsible of final sequence alignment before we finish
with epoch X and move to epoch X+1
*/
func FindInfoAboutLastBlocks(epochHandler *structures.EpochDataHandler, aefp *structures.AggregatedEpochFinalizationProof) {

	emptyTemplate := make(map[string]structures.ExecutionStatsPerPool)

	infoAboutFinalBlocksByPool := make(map[string]map[string]structures.ExecutionStatsPerPool)

	// Start the cycle in reverse order from <aefp.lastLeader>

	lastLeaderPubkey := epochHandler.LeadersSequence[aefp.LastLeader]

	emptyTemplate[lastLeaderPubkey] = structures.ExecutionStatsPerPool{
		Index: int(aefp.LastIndex),
		Hash:  aefp.LastHash,
	}

	infoAboutLastBlocksByPreviousPool := make(map[string]structures.ExecutionStatsPerPool)

	for position := aefp.LastLeader; position > 0; position-- {

		leaderPubKey := epochHandler.LeadersSequence[position]

		// In case we know that pool on this position created 0 block - don't return from function and continue the cycle iterations

		if infoAboutLastBlocksByPreviousPool[leaderPubKey].Index == -1 {

			continue

		} else {

			// Get the first block in this epoch by this pool

			firstBlockInThisEpochByPool := common_functions.GetBlock(epochHandler.Id, leaderPubKey, 0, epochHandler)

			if firstBlockInThisEpochByPool == nil {

				return

			}

			// In this block we should have ALRPs for all the previous pools

			alrpChainIsOk, infoAboutFinalBlocks := common_functions.ExtendedCheckAlrpChainValidity(
				firstBlockInThisEpochByPool, epochHandler, int(position), true,
			)

			if alrpChainIsOk {

				infoAboutFinalBlocksByPool[leaderPubKey] = infoAboutFinalBlocks

				infoAboutLastBlocksByPreviousPool = infoAboutFinalBlocks

			}

		}

	}

	for _, poolPubKey := range epochHandler.LeadersSequence {

		if finalBlocksData, ok := infoAboutFinalBlocksByPool[poolPubKey]; ok {

			for poolPub, alrpData := range finalBlocksData {

				if _, exists := emptyTemplate[poolPub]; !exists {

					emptyTemplate[poolPub] = alrpData

				}

			}

		}

	}

	globals.EXECUTION_THREAD_METADATA_HANDLER.Handler.LegacyEpochAlignmentData.InfoAboutLastBlocksInEpoch = emptyTemplate

	/*


		   After execution of this function we have:

		   [0] globals.EXECUTION_THREAD_METADATA_HANDLER.Handler.EpochDataHandler.LeadersSequence with structure: [Pool0A,Pool1A,....,PoolNA]

		   Using this chains we'll finish the sequence alignment process

		   [1] globals.EXECUTION_THREAD_METADATA_HANDLER.Handler.LegacyEpochAlignmentData.InfoAboutLastBlocksInEpoch with structure:

		   {

		       Pool0A:{index,hash},
		       Pool1A:{index,hash},
		       ....,
		       PoolNA:{index,hash}

		   }

		   ___________________________________ So ___________________________________

		   Using the order in LeadersSequence - finish the execution based on index:hash pairs

		   Example:

		   	1) We have LeadersSequence: [Validator12, Validator3 , Validator7]

			2) Take the data from globals.EXECUTION_THREAD_METADATA_HANDLER.Handler.LegacyEpochAlignmentData.InfoAboutLastBlocksInEpoch

			3) Imagine it looks like this:

			{

		       Validator12:{index:14,hash:"0xaaaa"},
		       Validator7:{index:35,hash:"0xbbbb"},
		       ....,
		       Validator3:{index:10,hash:"0xcccc"}

		    }

			4) Using data about last block height and its hash - complete the execution process in this sequence:

			1. Validator 12 - execute untill index=14
			2. Validator3 - execute untill index=35
			3. Validator7 - execute untill index=10

			Exec untill block 14 of Validator12, then move to blocks by Validator3 - execute from 0 to 35
			Finally move to Validator7 and execute from index 0 to 10


	*/

}

func TryToFinishCurrentEpoch(epochHandler *structures.EpochDataHandler) {

	epochIndex := epochHandler.Id

	nextEpochIndex := epochIndex + 1

	var nextEpochData *structures.EpochDataHandler

	if nextEpochData != nil {

		nextEpochDataTemplate := structures.EpochDataHandler{

			Id: nextEpochIndex,

			Hash: nextEpochData.Hash,

			Quorum: nextEpochData.Quorum,

			LeadersSequence: nextEpochData.LeadersSequence,
		}

		// Find the first blocks for epoch X+1

		var firstBlockDataOnNextEpoch structures.FirstBlockResult

		rawHandler, dbErr := globals.EPOCH_DATA.Get([]byte("FIRST_BLOCKS_IN_NEXT_EPOCH:"+strconv.Itoa(epochIndex)), nil)

		if dbErr == nil {

			json.Unmarshal(rawHandler, &firstBlockDataOnNextEpoch)

		}

		if firstBlockDataOnNextEpoch.FirstBlockCreator == "" {

			findResult := common_functions.GetFirstBlockInEpoch(&nextEpochDataTemplate, "EXECUTION")

			if findResult != nil {

				firstBlockDataOnNextEpoch.FirstBlockCreator = findResult.FirstBlockCreator

				firstBlockDataOnNextEpoch.FirstBlockHash = findResult.FirstBlockHash

			}

			// Store the info about first blocks on next epoch

			serializedData, serialErr := json.Marshal(firstBlockDataOnNextEpoch)

			if serialErr == nil {

				globals.EPOCH_DATA.Put([]byte("FIRST_BLOCKS_IN_NEXT_EPOCH:"+strconv.Itoa(epochIndex)), serializedData, nil)

			}

		}

		//____________After we get the first blocks for epoch X+1 - get the AEFP from it and build the data for VT to finish epoch X____________

		// firstBlockInThisEpoch := common_functions.GetBlock(nextEpochIndex, firstBlockDataOnNextEpoch.FirstBlockCreator, 0)

	}

}

func SetupNextEpoch(epochHandler *structures.EpochDataHandler) {

	// epochFullID := epochHandler.Hash + "#" + strconv.Itoa(epochHandler.Id)

	// currentEpochIndex := epochHandler.Id

	// nextEpochIndex := currentEpochIndex + 1

	// var nextEpochData *structures.EpochDataHandler // TODO: Take from DB

	// if nextEpochData != nil {

	// 	dbBatch := new(leveldb.Batch)

	// 	// TODO: Exec delayed txs here

	// }

}
