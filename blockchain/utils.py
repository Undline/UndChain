import hashlib
import time

from structures.threads_metadata_handlers import EpochHandler, ApprovementThreadMetadataHandler
from blockchain.global_vars import CORE_MAJOR_VERSION
from structures.misc import QuorumMemberData

def sha256(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

def get_utc_timestamp() -> int:
    return int(time.time() * 1000)

def is_my_core_version_old(thread: ApprovementThreadMetadataHandler) -> bool:
    return thread.core_major_version > CORE_MAJOR_VERSION

def epoch_still_fresh(thread: ApprovementThreadMetadataHandler) -> bool:
    return thread.epoch.start_timestamp+thread.network_parameters.get("EPOCH_TIME") > get_utc_timestamp()

def get_quorum_majority(thread: ApprovementThreadMetadataHandler) -> int:
    
    quorum_size = len(thread.epoch.quorum)

    majority = (2 * quorum_size) // 3 + 1

    return quorum_size if majority > quorum_size else majority


def get_quorum_urls_and_pubkeys(thread: ApprovementThreadMetadataHandler) -> list[QuorumMemberData]:
    
    quorum_data = []

    for pubkey in thread.epoch.quorum:
        pool_storage = get_from_approvement_thread_state(f"{pubkey}(POOL)_STORAGE_POOL")
        quorum_data.append(QuorumMemberData(PubKey=pubkey, Url=pool_storage.pool_url))

    return quorum_data



def get_from_approvement_thread_state(validator_id: str):
    pass


def set_leaders_sequence(thread: ApprovementThreadMetadataHandler, epoch_seed: str):
    pass

def get_current_epoch_quorum(epoch_handler: EpochHandler) -> List[str]:
    pass