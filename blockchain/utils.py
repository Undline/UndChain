import hashlib
import time
from structures.threads_metadata_handlers import ApprovementThreadMetadataHandler
from globals import CORE_MAJOR_VERSION

def sha256(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

def get_utc_timestamp() -> int:
    return int(time.time() * 1000)

def is_my_core_version_old(thread: ApprovementThreadMetadataHandler) -> bool:
    thread.coreMajorVersion > CORE_MAJOR_VERSION

def epoch_still_fresh(thread: ApprovementThreadMetadataHandler) -> bool:
    thread.epoch.startTimestamp+thread.networkParameters.get("EPOCH_TIME") > get_utc_timestamp()