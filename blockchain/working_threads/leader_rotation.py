import asyncio
from structures.threads_metadata_handlers import ApprovementThreadMetadataHandler

def time_is_out_for_current_leader(thread: ApprovementThreadMetadataHandler) -> bool:
    leadership_timeframe = thread.network_parameters.get("LEADERSHIP_TIMEFRAME")
    current_leader_index = thread.epoch.current_leader_index

async def leader_rotation():
    while True:
        print("Message from thread 4")
        await asyncio.sleep(3)