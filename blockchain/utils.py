import hashlib
import time


def sha256(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

def get_utc_timestamp() -> int:
    return int(time.time() * 1000)