package structures

type EpochDataHandler struct {
	Id                 int                 `json:"id"`
	Hash               string              `json:"hash"`
	PoolsRegistry      map[string]struct{} `json:"poolsRegistry"`
	Quorum             []string            `json:"quorum"`
	LeadersSequence    []string            `json:"leadersSequence"`
	StartTimestamp     uint64              `json:"startTimestamp"`
	CurrentLeaderIndex int                 `json:"currentLeaderIndex"`
}

type NextEpochDataHandler struct {
	NextEpochHash            string              `json:"nextEpochHash"`
	NextEpochPoolsRegistry   map[string]struct{} `json:"nextEpochPoolsRegistry"`
	NextEpochQuorum          []string            `json:"nextEpochQuorum"`
	NextEpochLeadersSequence []string            `json:"nextEpochLeadersSequence"`
	DelayedTransactions      []map[string]string `json:"delayedTransactions"`
}
