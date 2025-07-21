package structures

type ResponseStatus struct {
	Status string
}

type QuorumMemberData struct {
	PubKey, Url string
}

type FirstBlockResult struct {
	FirstBlockCreator, FirstBlockHash string
}

type FirstBlockDataForNextEpoch struct {
	FirstBlockResult
	Aefp *AggregatedEpochFinalizationProof
}

type FirstBlockAssumption struct {
	IndexOfFirstBlockCreator int                         `json:"indexOfFirstBlockCreator"`
	AfpForSecondBlock        AggregatedFinalizationProof `json:"afpForSecondBlock"`
}

type DelayedTransactionsBatch struct {
	EpochIndex          int                 `json:"epochIndex"`
	DelayedTransactions []map[string]string `json:"delayedTransactions"`
	Proofs              map[string]string   `json:"proofs"`
}

type ExecutionStatsPerPool struct {
	Index          int
	Hash           string
	FirstBlockHash string
}

func NewExecutionStatsTemplate() ExecutionStatsPerPool {

	return ExecutionStatsPerPool{
		Index:          -1,
		Hash:           "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
		FirstBlockHash: "",
	}

}
