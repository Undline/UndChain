import os
import hashlib
from pathlib import Path
from typing import Dict, List, Any

from klyntar_core import BLOCKCHAIN_GENESIS
from kv_storage import SimpleSQLiteDB
from structures.transaction import Transaction
from utils import sha256

# Read the core major version

with open('version.txt', 'r') as vf:
    CORE_MAJOR_VERSION: int = int(vf.read().strip())


def resolve_database(name: str) -> SimpleSQLiteDB:
    db_path: str = os.path.join(os.environ.get('CHAINDATA_PATH', ''), f"{name}.db")
    return SimpleSQLiteDB(db_path)


MEMPOOL: Dict[str, Transaction]

GLOBAL_CACHES: Dict[str, Any] = {
    "APPROVEMENT_THREAD_CACHE": {},  # type: Dict[str, Any]
    "FINALIZATION_PROOFS": {},  # type: Dict[str, Dict[str, str]]
    "TEMP_CACHE": {}  # type: Dict[str, Any]
}

WORKING_THREADS: Dict[str, Dict[str, Any]] = {
    "GENERATION_THREAD": {
        "epochFullId": sha256("0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef" + BLOCKCHAIN_GENESIS['NETWORK_ID'])+"#-1",
        "epochIndex": 0,
        "prevHash": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
        "nextIndex": 0
    },
    "APPROVEMENT_THREAD": {
        "CORE_MAJOR_VERSION": -1,
        "NETWORK_PARAMETERS": {},  # type: Dict[str, Any]
        "EPOCH": {}  # type: Dict[str, Any]
    }
}


# Databases
BLOCKCHAIN_DATABASES: Dict[str, SimpleSQLiteDB] = {
    "BLOCKS": resolve_database("BLOCKS"),
    "EPOCH_DATA": resolve_database("EPOCH_DATA"),
    "APPROVEMENT_THREAD_METADATA": resolve_database("APPROVEMENT_THREAD_METADATA"),
    "FINALIZATION_VOTING_STATS": resolve_database("FINALIZATION_VOTING_STATS")
}
