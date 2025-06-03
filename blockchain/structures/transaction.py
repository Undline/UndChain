from dataclasses import dataclass, field
from typing import Any, Dict

@dataclass
class Transaction:
    v: int
    fee: str
    creator: str
    sig: str
    txType: str
    sigType: str
    nonce: int
    payload: Dict[str, Any] = field(default_factory=dict)