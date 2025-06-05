from dataclasses import dataclass, field
from typing import Dict, List, Any

@dataclass
class EpochHandler:
    id: int
    hash: str
    poolsRegistry: Dict[str, None]
    quorum: List[str]
    leadersSequence: List[str]
    startTimestamp: int
    currentLeaderIndex: int

@dataclass
class ApprovementThreadMetadataHandler:
    coreMajorVersion: int
    networkParameters: Dict[str, Any]
    epoch: EpochHandler
    cache: Dict[str, Any] = field(default_factory=dict)

@dataclass
class ExecutionThreadMetadataHandler:
    coreMajorVersion: int
    networkParameters: Dict[str, Any]
    epoch: EpochHandler
    cache: Dict[str, Any] = field(default_factory=dict)
    # TODO: fill with extra fields

@dataclass
class GenerationThreadMetadataHandler:
    epochFullId: str
    prevHash: str
    nextIndex: int


