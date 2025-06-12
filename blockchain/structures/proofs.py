from dataclasses import dataclass, field
from typing import Dict

@dataclass
class AggregatedFinalizationProof:
    prev_block_hash: str
    block_id: str
    block_hash: str
    proofs: Dict[str, str]

@dataclass
class AggregatedEpochFinalizationProof:
    last_leader: int
    last_index: int
    last_hash: str
    hash_of_first_block_by_last_leader: str
    proofs: Dict[str, str]


@dataclass
class AggregatedLeaderRotationProof:
    first_block_hash: str
    skip_index: int
    skip_hash: str
    proofs: Dict[str, str]


@dataclass
class PoolVotingStat:
    index: int = -1
    hash: str = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
    afp: AggregatedFinalizationProof = field(default_factory=lambda: AggregatedFinalizationProof(
        prev_block_hash="",
        block_id="",
        block_hash="",
        proofs={}
    ))


def new_pool_voting_stat_template() -> PoolVotingStat:
    return PoolVotingStat()


@dataclass
class AlrpSkeleton:
    afp_for_first_block: AggregatedFinalizationProof = field(default_factory=lambda: AggregatedFinalizationProof("", "", "", {}))
    skip_data: PoolVotingStat = field(default_factory=lambda: new_pool_voting_stat_template())
    proofs: Dict[str, str] = field(default_factory=dict)


def new_alrp_skeleton_template() -> AlrpSkeleton:
    return AlrpSkeleton()
