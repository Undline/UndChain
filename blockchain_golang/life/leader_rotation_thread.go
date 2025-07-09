package life

import (
	"encoding/json"
	"fmt"
	"time"

	"github.com/VladChernenko/UndchainCore/globals"
	"github.com/VladChernenko/UndchainCore/structures"
	"github.com/VladChernenko/UndchainCore/utils"
)

func timeIsOutForCurrentLeader(approvementThread *structures.ApprovementThreadMetadataHandler) bool {

	// Function to check if time frame for current leader is done and we have to move to next pool in sequence

	leaderShipTimeframe := approvementThread.NetworkParameters.LeadershipTimeframe

	currentIndex := int64(approvementThread.EpochDataHandler.CurrentLeaderIndex)

	return utils.GetUTCTimestampInMilliSeconds() >= int64(approvementThread.EpochDataHandler.StartTimestamp)+(currentIndex+1)*leaderShipTimeframe

}

func LeaderRotationThread() {

	for {

		globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RLock()

		epochHandlerRef := &globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.EpochDataHandler

		haveNextCandidate := epochHandlerRef.CurrentLeaderIndex+1 < len(epochHandlerRef.LeadersSequence)

		if haveNextCandidate && timeIsOutForCurrentLeader(&globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler) {

			storedEpochIndex := epochHandlerRef.Id

			globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RUnlock()

			globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.Lock()

			threadMetadataHandlerRef := &globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler

			if storedEpochIndex == threadMetadataHandlerRef.EpochDataHandler.Id {

				threadMetadataHandlerRef.EpochDataHandler.CurrentLeaderIndex++

				// Store the updated AT

				jsonedHandler, errMarshal := json.Marshal(threadMetadataHandlerRef)

				if errMarshal != nil {

					fmt.Printf("Failed to marshal AT state: %v", errMarshal)

					panic("Impossible to marshal approvement thread state")

				}

				if err := globals.APPROVEMENT_THREAD_METADATA.Put([]byte("AT"), jsonedHandler, nil); err != nil {

					fmt.Printf("Failed to store AT state: %v", err)

					panic("Impossible to store the approvement thread state")

				}

			}

			globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.Unlock()

		} else {

			globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RUnlock()

		}

		time.Sleep(200 * time.Millisecond)

	}

}
