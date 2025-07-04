import os
import hashlib
from pathlib import Path
from typing import Dict, List, Any
import toml

from kv_storage import SimpleSQLiteDB

from structures.transaction import Transaction
from structures.threads_metadata_handlers import EpochHandler,ApprovementThreadMetadataHandler,GenerationThreadMetadataHandler


def sha256(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()


def resolve_database(name: str) -> SimpleSQLiteDB:
    db_path: str = os.path.join(os.environ.get(CHAINDATA_PATH,''), f"{name}.db")
    return SimpleSQLiteDB(db_path)


# Read the main path

CHAINDATA_PATH: str = os.environ.get('CHAINDATA_PATH','')

if not CHAINDATA_PATH:
    raise RuntimeError("CHAINDATA_PATH environment variable is not set")

genesis_path = os.path.join(CHAINDATA_PATH, "genesis.toml")

if not os.path.isfile(genesis_path):
    raise FileNotFoundError(f"Genesis file not found at {genesis_path}")

with open(genesis_path, "r") as f:
    BLOCKCHAIN_GENESIS = toml.load(f)

# Read the core major version

with open('version.txt', 'r') as vf:
    CORE_MAJOR_VERSION: int = int(vf.read().strip())


MEMPOOL: Dict[str, Transaction]

CONFIGURATION: Dict[str, Any] = {}

GLOBAL_CACHES: Dict[str, Any] = {
    "APPROVEMENT_THREAD_CACHE": {},  # type: Dict[str, Any]
    "FINALIZATION_PROOFS": {},  # type: Dict[str, Dict[str, str]]
    "TEMP_CACHE": {}  # type: Dict[str, Any]
}



# Initialize Generation Thread handler instance
GENERATION_THREAD = GenerationThreadMetadataHandler(
    epoch_full_id=sha256(
        "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef" + BLOCKCHAIN_GENESIS["NETWORK_ID"]
    ) + "#-1",
    prev_hash="0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
    next_index=0
)

# Initialize Approvement Thread handler instance
APPROVEMENT_THREAD = ApprovementThreadMetadataHandler(
    core_major_version=-1,
    network_parameters={},
    epoch=EpochHandler(),  # Make sure EpochHandler has a default constructor
    cache={}
)


# Databases

BLOCKS_DB = resolve_database("BLOCKS")

EPOCH_DATA_DB = resolve_database("EPOCH_DATA")

APPROVEMENT_THREAD_METADATA_DB = resolve_database("APPROVEMENT_THREAD_METADATA")

FINALIZATION_VOTING_STATS_DB = resolve_database("FINALIZATION_VOTING_STATS")