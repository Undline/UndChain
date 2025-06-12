from dataclasses import dataclass, field
from typing import Any, Dict

@dataclass
class Transaction:
    v: int
    fee: str
    creator: str
    sig: str
    tx_type: str
    sig_type: str
    nonce: int
    payload: Dict[str, Any] = field(default_factory=dict)