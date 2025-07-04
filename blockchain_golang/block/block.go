package block

import (
	"encoding/json"
	"strconv"

	"github.com/KlyntarNetwork/Web1337Golang/crypto_primitives/ed25519"
	"github.com/VladChernenko/UndchainCore/globals"
	"github.com/VladChernenko/UndchainCore/structures"
	"github.com/VladChernenko/UndchainCore/utils"
)

type ExtraData struct {
	Rest                            map[string]string                                    `json:"rest"`
	AefpForPreviousEpoch            *structures.AggregatedEpochFinalizationProof         `json:"aefpForPreviousEpoch"`
	DelayedTransactionsBatch        structures.DelayedTransactionsBatch                  `json:"delayedTxsBatch"`
	AggregatedLeadersRotationProofs map[string]*structures.AggregatedLeaderRotationProof `json:"aggregatedLeadersRotationProofs"`
}

type Block struct {
	Creator      string                   `json:"creator"`
	Time         int64                    `json:"time"`
	Epoch        string                   `json:"epoch"`
	Transactions []structures.Transaction `json:"transactions"`
	ExtraData    ExtraData                `json:"extraData"`
	Index        int                      `json:"index"`
	PrevHash     string                   `json:"prevHash"`
	Sig          string                   `json:"sig"`
}

func NewBlock(transactions []structures.Transaction, extraData ExtraData, epochFullID string) *Block {
	return &Block{
		Creator:      globals.CONFIGURATION.PublicKey,
		Time:         utils.GetUTCTimestampInMilliSeconds(),
		Epoch:        epochFullID,
		Transactions: transactions,
		ExtraData:    extraData,
		Index:        globals.GENERATION_THREAD_METADATA_HANDLER.NextIndex,
		PrevHash:     globals.GENERATION_THREAD_METADATA_HANDLER.PrevHash,
		Sig:          "",
	}
}

func (block *Block) GetHash() string {

	jsonedTransactions, _ := json.Marshal(block.Transactions)

	networkID := globals.GENESIS.NetworkId

	dataToHash := block.Creator + strconv.FormatInt(block.Time, 10) + string(jsonedTransactions) + networkID + block.Epoch + strconv.FormatUint(uint64(block.Index), 10) + block.PrevHash

	return utils.Blake3(dataToHash)

}

func (block *Block) SignBlock() {

	block.Sig = ed25519.GenerateSignature(globals.CONFIGURATION.PrivateKey, block.GetHash())

}

func (block *Block) VerifySignature() bool {

	return ed25519.VerifySignature(block.GetHash(), block.Creator, block.Sig)

}
