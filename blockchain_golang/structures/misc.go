package structures

type ResponseStatus struct {
	Status string
}

type QuorumMemberData struct {
	PubKey, Url string
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
