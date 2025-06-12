import hashlib
import time
from structures.threads_metadata_handlers import EpochHandler, ApprovementThreadMetadataHandler
from globals import CORE_MAJOR_VERSION

def sha256(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

def get_utc_timestamp() -> int:
    return int(time.time() * 1000)

def is_my_core_version_old(thread: ApprovementThreadMetadataHandler) -> bool:
    thread.core_major_version > CORE_MAJOR_VERSION

def epoch_still_fresh(thread: ApprovementThreadMetadataHandler) -> bool:
    thread.epoch.start_timestamp+thread.network_parameters.get("EPOCH_TIME") > get_utc_timestamp()


def get_from_approvement_thread_state(validator_id: str):
    pass


def set_leaders_sequence(thread: ApprovementThreadMetadataHandler, epoch_seed: str):
    pass

def get_quorum_majority(thread: ApprovementThreadMetadataHandler) -> int:
    pass


def get_quorum_urls_and_pubkeys(thread: ApprovementThreadMetadataHandler):
    pass


def get_current_epoch_quorum(epoch_handler: EpochHandler) -> List[str]:
    pass