package structures

type PoolVotingStat struct {
	Index int                         `json:"index"`
	Hash  string                      `json:"hash"`
	Afp   AggregatedFinalizationProof `json:"afp"`
}

func NewPoolVotingStatTemplate() PoolVotingStat {

	return PoolVotingStat{
		Index: -1,
		Hash:  "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
		Afp:   AggregatedFinalizationProof{},
	}

}
