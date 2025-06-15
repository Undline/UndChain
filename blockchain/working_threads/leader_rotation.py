import asyncio
from structures.threads_metadata_handlers import ApprovementThreadMetadataHandler
from utils import get_utc_timestamp

def time_is_out_for_current_leader(thread: ApprovementThreadMetadataHandler) -> bool:
    leadership_timeframe = thread.network_parameters.get("LEADERSHIP_TIMEFRAME")
    current_leader_index = thread.epoch.current_leader_index

    return get_utc_timestamp() >= thread.epoch.start_timestamp+(current_leader_index+1)*leadership_timeframe


async def leader_rotation():
    while True:
        print("Message from thread 4")
        await asyncio.sleep(3)