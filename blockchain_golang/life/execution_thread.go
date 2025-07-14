package life

import (
	"github.com/VladChernenko/UndchainCore/block"
	"github.com/VladChernenko/UndchainCore/globals"
	"github.com/VladChernenko/UndchainCore/structures"
	"github.com/VladChernenko/UndchainCore/utils"
)

func ExecutionThread() {

	for {

		globals.EXECUTION_THREAD_METADATA_HANDLER.RWMutex.RLock()

		epochHandler := globals.EXECUTION_THREAD_METADATA_HANDLER.Handler

		currentEpochIsFresh := utils.EpochStillFresh(&epochHandler)

		// Struct is {currentLeader,currentToVerify,infoAboutFinalBlocksInThisEpoch:{poolPubKey:{index,hash}}}
		//alignmentData := globals.EXECUTION_THREAD_METADATA_HANDLER.Handler.CurrentEpochAlignmentData

		shouldMoveToNextEpoch := false

		if epochHandler.LegacyEpochAlignmentData.Activated {

			infoFromAefpAboutLastBlocksByPools := epochHandler.LegacyEpochAlignmentData.InfoAboutLastBlocksInEpoch

			var localExecMetadataForLeader, metadataFromAefpForLeader structures.ExecutionStatsPerPool

			dataExists := false

			for {

				indexOfLeaderToExec := epochHandler.LegacyEpochAlignmentData.CurrentToExecute

				pubKeyOfLeader := epochHandler.EpochDataHandler.LeadersSequence[indexOfLeaderToExec]

				localExecMetadataForLeader = epochHandler.ExecutionData[pubKeyOfLeader]

				metadataFromAefpForLeader, dataExists = infoFromAefpAboutLastBlocksByPools[pubKeyOfLeader]

				if !dataExists {

					metadataFromAefpForLeader = structures.NewExecutionStatsTemplate()
				}

				finishedToExecBlocksByThisLeader := localExecMetadataForLeader.Index == metadataFromAefpForLeader.Index

				if finishedToExecBlocksByThisLeader {

					itsTheLastBlockInSequence := len(epochHandler.EpochDataHandler.LeadersSequence) == indexOfLeaderToExec+1

					if itsTheLastBlockInSequence {

						break

					} else {

						epochHandler.LegacyEpochAlignmentData.CurrentToExecute++

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

			allBlocksWereExecutedInLegacyEpoch := len(epochHandler.EpochDataHandler.LeadersSequence) == epochHandler.LegacyEpochAlignmentData.CurrentToExecute+1

			finishedToExecBlocksByLastLeader := localExecMetadataForLeader.Index == metadataFromAefpForLeader.Index

			if allBlocksWereExecutedInLegacyEpoch && finishedToExecBlocksByLastLeader {

				shouldMoveToNextEpoch = true
			}

		} else if currentEpochIsFresh && epochHandler.CurrentEpochAlignmentData.Activated {

			// Take the pool by it's position

			currentEpochAlignmentData := &epochHandler.CurrentEpochAlignmentData

			leaderPubkeyToExecBlocks := epochHandler.EpochDataHandler.LeadersSequence[currentEpochAlignmentData.CurrentToExecute]

			execStatsOfLeader := epochHandler.ExecutionData[leaderPubkeyToExecBlocks] // {index,hash}

			infoAboutLastBlockByThisLeader, exists := currentEpochAlignmentData.InfoAboutLastBlocksInEpoch[leaderPubkeyToExecBlocks] // {index,hash}

			if exists && execStatsOfLeader.Index == infoAboutLastBlockByThisLeader.Index {

				// Move to next one

				epochHandler.CurrentEpochAlignmentData.CurrentToExecute++

				if !currentEpochIsFresh {

					TryToFinishCurrentEpoch(&epochHandler.EpochDataHandler)

				}

				// TODO: Here we need to skip the following logic and start next iteration
				// TODO: Cope with mutexes here
				continue

			}

			// Try check if we have established a WSS channel to fetch blocks

			// Now, when we have connection with some entity which has an ability to give us blocks via WS(s) tunnel

		}

		if !currentEpochIsFresh && !epochHandler.LegacyEpochAlignmentData.Activated {

			TryToFinishCurrentEpoch(&epochHandler.EpochDataHandler)

		}

		if shouldMoveToNextEpoch {

			SetupNextEpoch(&epochHandler.EpochDataHandler)

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
func FindInfoAboutLastBlocks(epochHandler *structures.EpochDataHandler) {}

func TryToFinishCurrentEpoch(epochHandler *structures.EpochDataHandler) {}

func SetupNextEpoch(epochHandler *structures.EpochDataHandler) {}
