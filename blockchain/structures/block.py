import json
import hashlib
import time
from dataclasses import dataclass
from typing import Dict, List

from proofs import AggregatedLeaderRotationProof, AggregatedEpochFinalizationProof
from transaction import Transaction


def get_utc_timestamp_millis():
    return int(time.time() * 1000)


def generate_signature(private_key: str, message: str) -> str:
    # stub
    return f"sig({message[:10]}...)"

def verify_signature(message: str, pubkey: str, signature: str) -> bool:
    # stub
    return signature.startswith("sig(")


@dataclass
class DelayedTxsBatch:
    epochIndex: int
    delayedTransactions: List[Dict[str, str]]
    proofs: Dict[str, str]


@dataclass
class ExtraData:
    rest: Dict[str, str]
    aefpForPreviousEpoch: AggregatedEpochFinalizationProof
    delayedTxsBatch: DelayedTxsBatch
    aggregatedLeadersRotationProofs: Dict[str, AggregatedLeaderRotationProof] # leader -> proof


@dataclass
class Block:
    creator: str
    time: int
    epoch: str
    transactions: List[Transaction]
    extra_data: ExtraData
    index: int
    prev_hash: str
    sig: str = ""

    def get_hash(self,network_id) -> str:
        jsoned_transactions = json.dumps([t.__dict__ for t in self.transactions], sort_keys=True)
        data_to_hash = (
            self.creator +
            str(self.time) +
            jsoned_transactions +
            network_id +
            self.epoch +
            str(self.index) +
            self.prev_hash
        )
        return hashlib.sha256(data_to_hash.encode()).hexdigest()

    def sign_block(self,private_key):
        self.sig = generate_signature(private_key, self.get_hash())

    def verify_signature(self) -> bool:
        return verify_signature(self.get_hash(), self.creator, self.sig)