from dataclasses import dataclass, field
from typing import Dict

@dataclass
class AggregatedFinalizationProof:
    prevBlockHash: str
    blockId: str
    blockHash: str
    proofs: Dict[str, str]

@dataclass
class AggregatedEpochFinalizationProof:
    lastLeader: int
    lastIndex: int
    lastHash: str
    hashOfFirstBlockByLastLeader: str
    proofs: Dict[str, str]


@dataclass
class AggregatedLeaderRotationProof:
    firstBlockHash: str
    skipIndex: int
    skipHash: str
    proofs: Dict[str, str]


@dataclass
class PoolVotingStat:
    index: int = -1
    hash: str = "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
    afp: AggregatedFinalizationProof = field(default_factory=lambda: AggregatedFinalizationProof(
        prevBlockHash="",
        blockId="",
        blockHash="",
        proofs={}
    ))


def new_pool_voting_stat_template() -> PoolVotingStat:
    return PoolVotingStat()


@dataclass
class AlrpSkeleton:
    afpForFirstBlock: AggregatedFinalizationProof = field(default_factory=lambda: AggregatedFinalizationProof("", "", "", {}))
    skipData: PoolVotingStat = field(default_factory=lambda: new_pool_voting_stat_template())
    proofs: Dict[str, str] = field(default_factory=dict)


def new_alrp_skeleton_template() -> AlrpSkeleton:
    return AlrpSkeleton()
