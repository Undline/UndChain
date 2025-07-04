package structures

type AggregatedFinalizationProof struct {
	PrevBlockHash string            `json:"prevBlockHash"`
	BlockId       string            `json:"blockId"`
	BlockHash     string            `json:"blockHash"`
	Proofs        map[string]string `json:"proofs"`
}

type AggregatedEpochFinalizationProof struct {
	LastLeader                   uint              `json:"lastLeader"`
	LastIndex                    uint              `json:"lastIndex"`
	LastHash                     string            `json:"lastHash"`
	HashOfFirstBlockByLastLeader string            `json:"hashOfFirstBlockByLastLeader"`
	Proofs                       map[string]string `json:"proofs"`
}

type AggregatedLeaderRotationProof struct {
	FirstBlockHash string            `json:"firstBlockHash"`
	SkipIndex      int               `json:"skipIndex"`
	SkipHash       string            `json:"skipHash"`
	Proofs         map[string]string `json:"proofs"`
}

type AlrpSkeleton struct {
	AfpForFirstBlock AggregatedFinalizationProof
	SkipData         PoolVotingStat
	Proofs           map[string]string // quorumMemberPubkey => signature
}

func NewAlrpSkeletonTemplate() *AlrpSkeleton {

	return &AlrpSkeleton{

		AfpForFirstBlock: AggregatedFinalizationProof{},
		SkipData:         NewPoolVotingStatTemplate(),
		Proofs:           make(map[string]string),
	}

}
