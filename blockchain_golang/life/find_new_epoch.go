package life

import (
	"context"
	"encoding/binary"
	"encoding/json"
	"io"
	"net/http"
	"strconv"
	"strings"
	"time"

	"github.com/KlyntarNetwork/Web1337Golang/crypto_primitives/ed25519"
	"github.com/VladChernenko/UndchainCore/common_functions"
	"github.com/VladChernenko/UndchainCore/globals"
	"github.com/VladChernenko/UndchainCore/structures"
	"github.com/VladChernenko/UndchainCore/system_contracts"
	"github.com/VladChernenko/UndchainCore/utils"
	"github.com/syndtr/goleveldb/leveldb"
)

type FirstBlockDataWithAefp struct {
	FirstBlockCreator, FirstBlockHash string

	Aefp *structures.AggregatedEpochFinalizationProof
}

var AEFP_AND_FIRST_BLOCK_DATA FirstBlockDataWithAefp

func ExecuteDelayedTransaction(delayedTransaction map[string]string) {

	if delayedTxType, ok := delayedTransaction["type"]; ok {

		// Now find the handler

		if funcHandler, ok := system_contracts.DELAYED_TRANSACTIONS_MAP[delayedTxType]; ok {

			funcHandler(delayedTransaction)

		}

	}

}

func fetchAefp(ctx context.Context, url string, quorum []string, majority int, epochFullID string, resultCh chan<- *structures.AggregatedEpochFinalizationProof) {

	req, err := http.NewRequestWithContext(ctx, "GET", url, nil)

	if err != nil {
		return
	}

	resp, err := http.DefaultClient.Do(req)

	if err != nil {
		return
	}
	defer resp.Body.Close()

	body, _ := io.ReadAll(resp.Body)

	var aefp *structures.AggregatedEpochFinalizationProof

	err = json.Unmarshal(body, aefp)

	if err == nil {

		if common_functions.VerifyAggregatedEpochFinalizationProof(aefp, quorum, majority, epochFullID) {

			select {

			case resultCh <- aefp:
			case <-ctx.Done():

			}

		}

	}

}

func EpochRotationThread() {

	for {

		globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RLock()

		if !utils.EpochStillFresh(&globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler) {

			epochHandlerRef := &globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.EpochDataHandler

			epochFullID := epochHandlerRef.Hash + "#" + strconv.Itoa(epochHandlerRef.Id)

			if !utils.SignalAboutEpochRotationExists(epochHandlerRef.Id) {

				// If epoch is not fresh - send the signal to persistent db that we finish it - not to create AFPs, ALRPs anymore
				keyValue := []byte("EPOCH_FINISH:" + strconv.Itoa(epochHandlerRef.Id))

				globals.FINALIZATION_VOTING_STATS.Put(keyValue, []byte("TRUE"), nil)

			}

			if utils.SignalAboutEpochRotationExists(epochHandlerRef.Id) {

				majority := common_functions.GetQuorumMajority(epochHandlerRef)

				quorumMembers := common_functions.GetQuorumUrlsAndPubkeys(epochHandlerRef)

				haveEverything := AEFP_AND_FIRST_BLOCK_DATA.Aefp != nil && AEFP_AND_FIRST_BLOCK_DATA.FirstBlockHash != ""

				if !haveEverything {

					// 1. Find AEFPs

					if AEFP_AND_FIRST_BLOCK_DATA.Aefp == nil {

						// Try to find locally first

						keyValue := []byte("AEFP:" + strconv.Itoa(epochHandlerRef.Id))

						aefpRaw, err := globals.EPOCH_DATA.Get(keyValue, nil)

						var aefp structures.AggregatedEpochFinalizationProof

						errParse := json.Unmarshal(aefpRaw, &aefp)

						if err == nil && errParse == nil {

							AEFP_AND_FIRST_BLOCK_DATA.Aefp = &aefp

						} else {

							// Ask quorum for AEFP

							resultCh := make(chan *structures.AggregatedEpochFinalizationProof, 1)
							ctx, cancel := context.WithCancel(context.Background())

							for _, quorumMember := range quorumMembers {
								go fetchAefp(ctx, quorumMember.Url, epochHandlerRef.Quorum, majority, epochFullID, resultCh)
							}

							select {

							case value := <-resultCh:
								AEFP_AND_FIRST_BLOCK_DATA.Aefp = value
								cancel()
							case <-time.After(2 * time.Second):
								cancel()
							}
						}
					}

					// 2. Find first block in epoch
					if AEFP_AND_FIRST_BLOCK_DATA.FirstBlockHash == "" {

						firstBlockData := common_functions.GetFirstBlockInEpoch(epochHandlerRef, "APPROVEMENT")

						if firstBlockData != nil {

							AEFP_AND_FIRST_BLOCK_DATA.FirstBlockCreator = firstBlockData.FirstBlockCreator

							AEFP_AND_FIRST_BLOCK_DATA.FirstBlockHash = firstBlockData.FirstBlockHash

						}

					}

				}

				if AEFP_AND_FIRST_BLOCK_DATA.Aefp != nil && AEFP_AND_FIRST_BLOCK_DATA.FirstBlockHash != "" {

					// 1. Fetch first block
					firstBlock := common_functions.GetBlock(epochHandlerRef.Id, AEFP_AND_FIRST_BLOCK_DATA.FirstBlockCreator, 0, epochHandlerRef)

					// 2. Compare hashes

					if firstBlock != nil && firstBlock.GetHash() == AEFP_AND_FIRST_BLOCK_DATA.FirstBlockHash {

						// 3. Verify that quorum agreed batch of delayed transactions
						latestBatchIndex := int64(0)

						latestBatchIndexRaw, err := globals.APPROVEMENT_THREAD_METADATA.Get([]byte("LATEST_BATCH_INDEX"), nil)

						if err == nil {
							latestBatchIndex = int64(binary.BigEndian.Uint64(latestBatchIndexRaw))
						}

						var delayedTransactionsToExecute []map[string]string

						jsonedDelayedTxs, _ := json.Marshal(firstBlock.ExtraData.DelayedTransactionsBatch.DelayedTransactions)

						dataThatShouldBeSigned := "SIG_DELAYED_OPERATIONS:" + strconv.Itoa(epochHandlerRef.Id) + ":" + string(jsonedDelayedTxs)

						okSignatures := 0

						unique := make(map[string]bool)

						quorumMap := make(map[string]bool)

						for _, pk := range epochHandlerRef.Quorum {
							quorumMap[strings.ToLower(pk)] = true
						}

						for signerPubKey, signa := range firstBlock.ExtraData.DelayedTransactionsBatch.Proofs {

							isOK := ed25519.VerifySignature(dataThatShouldBeSigned, signerPubKey, signa)

							loweredPubKey := strings.ToLower(signerPubKey)

							if isOK && quorumMap[signerPubKey] && !unique[loweredPubKey] {

								unique[loweredPubKey] = true

								okSignatures++

							}

						}

						// 5. Finally - check if this batch has bigger index than already executed
						// 6. Only in case it's indeed new batch - execute it

						globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RUnlock()

						globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.Lock()

						if okSignatures >= majority && int64(epochHandlerRef.Id) > latestBatchIndex {

							latestBatchIndex = int64(epochHandlerRef.Id)

							delayedTransactionsToExecute = firstBlock.ExtraData.DelayedTransactionsBatch.DelayedTransactions

						}

						keyBytes := []byte("EPOCH_HANDLER:" + strconv.Itoa(epochHandlerRef.Id))

						valBytes, _ := json.Marshal(epochHandlerRef)

						globals.EPOCH_DATA.Put(keyBytes, valBytes, nil)

						var daoVotingContractCalls, allTheRestContractCalls []map[string]string

						atomicBatch := new(leveldb.Batch)

						for _, delayedTransaction := range delayedTransactionsToExecute {

							if delayedTxType, ok := delayedTransaction["type"]; ok {

								if delayedTxType == "votingAccept" {

									daoVotingContractCalls = append(daoVotingContractCalls, delayedTransaction)

								} else {

									allTheRestContractCalls = append(allTheRestContractCalls, delayedTransaction)

								}

							}

						}

						delayedTransactionsOrderByPriority := append(daoVotingContractCalls, allTheRestContractCalls...)

						// Execute delayed transactions
						for _, delayedTransaction := range delayedTransactionsOrderByPriority {

							ExecuteDelayedTransaction(delayedTransaction)

						}

						for key, value := range globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.Cache {

							valBytes, _ := json.Marshal(value)

							atomicBatch.Put([]byte(key), valBytes)

						}

						utils.LogWithTime("Dealyed txs were executed for epoch on AT: "+epochFullID, utils.GREEN_COLOR)

						//_______________________ Update the values for new epoch _______________________

						// Now, after the execution we can change the epoch id and get the new hash + prepare new temporary object

						nextEpochId := epochHandlerRef.Id + 1

						nextEpochHash := utils.Blake3(AEFP_AND_FIRST_BLOCK_DATA.FirstBlockHash)

						nextEpochQuorumSize := globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.NetworkParameters.QuorumSize

						nextEpochHandler := structures.EpochDataHandler{
							Id:                 nextEpochId,
							Hash:               nextEpochHash,
							PoolsRegistry:      epochHandlerRef.PoolsRegistry,
							Quorum:             common_functions.GetCurrentEpochQuorum(epochHandlerRef, nextEpochQuorumSize, nextEpochHash),
							LeadersSequence:    []string{},
							StartTimestamp:     epochHandlerRef.StartTimestamp + uint64(globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.NetworkParameters.EpochTime),
							CurrentLeaderIndex: 0,
						}

						common_functions.SetLeadersSequence(&nextEpochHandler, nextEpochHash)

						atomicBatch.Put([]byte("LATEST_BATCH_INDEX:"), []byte(strconv.Itoa(int(latestBatchIndex))))

						globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.EpochDataHandler = nextEpochHandler

						jsonedHandler, _ := json.Marshal(globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler)

						atomicBatch.Put([]byte("AT"), jsonedHandler)

						// Clean cache

						clear(globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.Cache)

						// Clean in-memory helpful object

						AEFP_AND_FIRST_BLOCK_DATA = FirstBlockDataWithAefp{}

						globals.APPROVEMENT_THREAD_METADATA.Write(atomicBatch, nil)

						utils.LogWithTime("Epoch on approvement thread was updated => "+nextEpochHash+"#"+strconv.Itoa(nextEpochId), utils.GREEN_COLOR)

						globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.Unlock()

						//_______________________Check the version required for the next epoch________________________

						if utils.IsMyCoreVersionOld(&globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler) {

							utils.LogWithTime("New version detected on APPROVEMENT_THREAD. Please, upgrade your node software", utils.YELLOW_COLOR)

							utils.GracefulShutdown()

						}

					} else {

						globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RUnlock()

					}

				} else {

					globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RUnlock()

				}

			} else {

				globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RUnlock()

			}

		} else {

			globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RUnlock()

		}

		time.Sleep(1 * time.Second)

	}

}
