package life

import (
	"encoding/json"
	"net/http"
	"time"

	"github.com/VladChernenko/UndchainCore/block"
	"github.com/VladChernenko/UndchainCore/common_functions"
	"github.com/VladChernenko/UndchainCore/globals"
	"github.com/VladChernenko/UndchainCore/structures"
	"github.com/VladChernenko/UndchainCore/utils"
)

type TargetResponse struct {
	ProposedIndexOfLeader            int                                    `json:"proposedIndexOfLeader"`
	FirstBlockByCurrentLeader        block.Block                            `json:"firstBlockByCurrentLeader"`
	AfpForSecondBlockByCurrentLeader structures.AggregatedFinalizationProof `json:"afpForSecondBlockByCurrentLeader"`
}

func SequenceAlignmentThread() {

	/*

	   [+] In this function we should time by time ask for ALRPs from quorum to understand of how to continue block sequence

	   [+] Use VT.TEMP_INFO_ABOUT_LAST_BLOCKS_BY_PREVIOUS_POOLS


	   Based on current epoch in APPROVEMENT_THREAD - build the temporary info about index/hashes of pools to keep work on verification thread

	*/

	for {

		globals.EXECUTION_THREAD_METADATA_HANDLER.RWMutex.RLock()

		epochHandlerRef := &globals.EXECUTION_THREAD_METADATA_HANDLER.Handler.EpochHandler

		localVersionOfCurrentLeader := globals.EXECUTION_THREAD_METADATA_HANDLER.Handler.AlignmentData.CurrentLeader

		quorumMembers := common_functions.GetQuorumUrlsAndPubkeys(&globals.EXECUTION_THREAD_METADATA_HANDLER.Handler.EpochHandler)

		randomTarget := utils.GetRandomFromSlice(quorumMembers)

		// Now send request to random quorum member

		client := &http.Client{
			Timeout: 5 * time.Second,
		}

		resp, err := client.Get(randomTarget.Url)

		if err != nil {
			return
		}
		defer resp.Body.Close()

		if resp.StatusCode != http.StatusOK {
			return
		}

		var targetResponse TargetResponse

		if err := json.NewDecoder(resp.Body).Decode(&targetResponse); err == nil {

			if localVersionOfCurrentLeader <= targetResponse.ProposedIndexOfLeader && targetResponse.FirstBlockByCurrentLeader.Index == 0 {

				// Verify the AFP for second block(with index 1 in epoch) to make sure that block 0(first block in epoch) was 100% accepted

				afp := &targetResponse.AfpForSecondBlockByCurrentLeader
				firstBlock := &targetResponse.FirstBlockByCurrentLeader
				proposedIndex := targetResponse.ProposedIndexOfLeader

				sameHash := afp.PrevBlockHash == firstBlock.GetHash()
				validProof := common_functions.VerifyAggregatedFinalizationProof(afp, epochHandlerRef)

				if sameHash && validProof {
					// Verify all the ALRPs in block header
					// TODO: Verify that blockcreator pubkey is equal to epochHandler.LeadersSequence[proposedIndex]
					if common_functions.CheckAlrpChainValidity(firstBlock, epochHandlerRef, proposedIndex) {
						//
					}
				}

			}

		}

		globals.EXECUTION_THREAD_METADATA_HANDLER.RWMutex.RUnlock()

		// Add some delay

		time.Sleep(time.Second)

	}

}
