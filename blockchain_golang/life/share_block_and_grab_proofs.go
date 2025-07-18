package life

import (
	"context"
	"encoding/json"
	"fmt"
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
	"github.com/gorilla/websocket"

	ws_structures "github.com/VladChernenko/UndchainCore/websocket"
)

var PROOFS_GRABBER_MUTEX = sync.RWMutex{}

type ProofsGrabber struct {
	EpochId             int
	AcceptedIndex       int
	AcceptedHash        string
	AfpForPrevious      structures.AggregatedFinalizationProof
	HuntingForBlockId   string
	HuntingForBlockHash string
}

var WEBSOCKET_CONNECTIONS = make(map[string]*websocket.Conn) // quorumMember => websocket handler

var FINALIZATION_PROOFS_CACHE = make(map[string]string) // quorumMember => finalization proof signa

var PROOFS_GRABBER = ProofsGrabber{
	EpochId: -1,
}

var BLOCK_TO_SHARE *block.Block = &block.Block{
	Index: -1,
}

var QUORUM_WAITER_FOR_FINALIZATION_PROOFS *utils.QuorumWaiter

func runFinalizationProofsGrabbing(epochHandler *structures.EpochDataHandler) {

	// Call SendAndWait here
	// Once received 2/3 votes for block - continue

	PROOFS_GRABBER_MUTEX.Lock()

	defer PROOFS_GRABBER_MUTEX.Unlock()

	epochFullId := epochHandler.Hash + "#" + strconv.Itoa(epochHandler.Id)

	blockIndexToHunt := strconv.Itoa(PROOFS_GRABBER.AcceptedIndex + 1)

	blockIdForHunting := strconv.Itoa(epochHandler.Id) + ":" + globals.CONFIGURATION.PublicKey + ":" + blockIndexToHunt

	blockIdThatInPointer := strconv.Itoa(epochHandler.Id) + ":" + globals.CONFIGURATION.PublicKey + ":" + strconv.Itoa(BLOCK_TO_SHARE.Index)

	majority := common_functions.GetQuorumMajority(epochHandler)

	if blockIdForHunting != blockIdThatInPointer {

		blockDataRaw, errDB := globals.BLOCKS.Get([]byte(blockIdForHunting), nil)

		if errDB == nil {

			if parseErr := json.Unmarshal(blockDataRaw, BLOCK_TO_SHARE); parseErr != nil {
				return
			}

		} else {
			return
		}

	}

	blockHash := BLOCK_TO_SHARE.GetHash()

	PROOFS_GRABBER.HuntingForBlockId = blockIdForHunting

	PROOFS_GRABBER.HuntingForBlockHash = blockHash

	if len(FINALIZATION_PROOFS_CACHE) < majority {

		// Build message - then parse to JSON

		message := ws_structures.WsFinalizationProofRequest{
			Route:            "get_finalization_proof",
			Block:            *BLOCK_TO_SHARE,
			PreviousBlockAfp: PROOFS_GRABBER.AfpForPrevious,
		}

		if messageJsoned, err := json.Marshal(message); err == nil {

			// Create max delay

			ctx, cancel := context.WithTimeout(context.Background(), 3*time.Second)
			defer cancel()

			responses, ok := QUORUM_WAITER_FOR_FINALIZATION_PROOFS.SendAndWait(ctx, messageJsoned, epochHandler.Quorum, WEBSOCKET_CONNECTIONS, majority)

			if !ok {
				return
			}

			for _, raw := range responses {

				var parsedFinalizationProof ws_structures.WsFinalizationProofResponse

				if err := json.Unmarshal(raw, &parsedFinalizationProof); err == nil {

					// Now verify proof and parse requests

					if parsedFinalizationProof.VotedForHash == PROOFS_GRABBER.HuntingForBlockHash {

						// Verify the finalization proof

						dataThatShouldBeSigned := PROOFS_GRABBER.AcceptedHash + PROOFS_GRABBER.HuntingForBlockId + PROOFS_GRABBER.HuntingForBlockHash + epochFullId

						finalizationProofIsOk := slices.Contains(epochHandler.Quorum, parsedFinalizationProof.Voter) && ed25519.VerifySignature(dataThatShouldBeSigned, parsedFinalizationProof.Voter, parsedFinalizationProof.FinalizationProof)

						if finalizationProofIsOk {

							FINALIZATION_PROOFS_CACHE[parsedFinalizationProof.Voter] = parsedFinalizationProof.FinalizationProof

						}

					}

				}

			}

		}

	}

	if len(FINALIZATION_PROOFS_CACHE) >= majority {

		aggregatedFinalizationProof := structures.AggregatedFinalizationProof{

			PrevBlockHash: PROOFS_GRABBER.AcceptedHash,

			BlockId: blockIdForHunting,

			BlockHash: blockHash,

			Proofs: FINALIZATION_PROOFS_CACHE,
		}

		keyBytes := []byte("AFP:" + blockIdForHunting)

		valueBytes, _ := json.Marshal(aggregatedFinalizationProof)

		// Store AFP locally

		globals.EPOCH_DATA.Put(keyBytes, valueBytes, nil)

		// Repeat procedure for the next block and store the progress

		proofGrabberKeyBytes := []byte(strconv.Itoa(epochHandler.Id) + ":PROOFS_GRABBER")

		proofGrabberValueBytes, marshalErr := json.Marshal(PROOFS_GRABBER)

		if marshalErr == nil {

			proofsGrabberStoreErr := globals.FINALIZATION_VOTING_STATS.Put(proofGrabberKeyBytes, proofGrabberValueBytes, nil)

			if proofsGrabberStoreErr == nil {

				PROOFS_GRABBER.AfpForPrevious = aggregatedFinalizationProof

				PROOFS_GRABBER.AcceptedIndex++

				PROOFS_GRABBER.AcceptedHash = PROOFS_GRABBER.HuntingForBlockHash

				msg := fmt.Sprintf(
					"%sApproved height for epoch %s%d %sis %s%d %s(%.3f%% agreements)",
					utils.RED_COLOR,
					utils.CYAN_COLOR,
					epochHandler.Id,
					utils.RED_COLOR,
					utils.CYAN_COLOR,
					PROOFS_GRABBER.AcceptedIndex-1,
					utils.GREEN_COLOR,
					float64(len(FINALIZATION_PROOFS_CACHE))/float64(len(epochHandler.Quorum))*100,
				)

				utils.LogWithTime(msg, utils.WHITE_COLOR)

				// Delete finalization proofs that we don't need more

				FINALIZATION_PROOFS_CACHE = make(map[string]string)

			} else {
				return
			}

		} else {
			return
		}

	}

}

func BlocksSharingAndProofsGrabingThread() {

	for {

		globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RLock()

		epochHandlerRef := &globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.EpochDataHandler

		currentLeaderPubKey := epochHandlerRef.LeadersSequence[epochHandlerRef.CurrentLeaderIndex]

		if currentLeaderPubKey != globals.CONFIGURATION.PublicKey || !utils.EpochStillFresh(&globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler) {

			globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RUnlock()

			time.Sleep(1 * time.Second)

			continue

		}

		PROOFS_GRABBER_MUTEX.RLock()

		if PROOFS_GRABBER.EpochId != epochHandlerRef.Id {

			PROOFS_GRABBER_MUTEX.RUnlock()

			PROOFS_GRABBER_MUTEX.Lock()

			// Try to get stored proofs grabber from db

			dbKey := []byte(strconv.Itoa(epochHandlerRef.Id) + ":PROOFS_GRABBER")

			if rawGrabber, err := globals.FINALIZATION_VOTING_STATS.Get(dbKey, nil); err == nil {

				json.Unmarshal(rawGrabber, &PROOFS_GRABBER)

			} else {

				// Assign initial value of proofs grabber for each new epoch

				PROOFS_GRABBER = ProofsGrabber{

					EpochId: epochHandlerRef.Id,

					AcceptedIndex: -1,

					AcceptedHash: "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
				}

			}

			// And store new descriptor

			if serialized, err := json.Marshal(PROOFS_GRABBER); err == nil {

				globals.FINALIZATION_VOTING_STATS.Put(dbKey, serialized, nil)

			}

			PROOFS_GRABBER_MUTEX.Unlock()

			// Also, open connections with quorum here. Create QuorumWaiter etc.

			utils.OpenWebsocketConnectionsWithQuorum(epochHandlerRef.Quorum, WEBSOCKET_CONNECTIONS)

			// Create new QuorumWaiter

			QUORUM_WAITER_FOR_FINALIZATION_PROOFS = utils.NewQuorumWaiter(len(epochHandlerRef.Quorum))

		} else {

			PROOFS_GRABBER_MUTEX.RUnlock()

		}

		runFinalizationProofsGrabbing(epochHandlerRef)

		globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RUnlock()

	}

}
