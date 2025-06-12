import os
import json
import globals
from structures.threads_metadata_handlers import GenerationThreadMetadataHandler, ApprovementThreadMetadataHandler
from utils import sha256


def prepare_blockchain():

    # Create directory for chaindata if it does not exist
    if not os.path.exists(globals.CHAINDATA_PATH):
        try:
            os.makedirs(globals.CHAINDATA_PATH, mode=0o755, exist_ok=True)
        except OSError as e:
            print(f"failed to create CHAINDATA directory: {e}")
        return

    # Load GT - Generation Thread handler
    data = globals.BLOCKS_DB.get("GT")

    if data is not None:
        try:
            gt_dict = json.loads(data)
            gt_handler = GenerationThreadMetadataHandler.from_dict(gt_dict)
            globals.GENERATION_THREAD_METADATA_HANDLER = gt_handler
        except Exception as e:
            print(f"failed to unmarshal GENERATION_THREAD: {e}")
            return
    
    # Load AT - Approvement Thread handler
    data = globals.APPROVEMENT_THREAD_METADATA_DB.get("AT")

    if data is not None:
        try:
            at_dict = json.loads(data)
            at_handler = ApprovementThreadMetadataHandler.from_dict(at_dict)
            if at_handler.Cache is None:
                at_handler.Cache = {}
            globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler = at_handler
        except Exception as e:
            print(f"failed to unmarshal APPROVEMENT_THREAD: {e}")
            return


    # Initialize genesis state if version is -1
    if globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.CoreMajorVersion == -1:
        
        set_genesis_to_state()

        try:
            serialized = json.dumps(
                globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.to_dict()
            )
            globals.APPROVEMENT_THREAD_METADATA_DB.put("AT", serialized)
        except Exception as e:
            print(f"failed to save APPROVEMENT_THREAD: {e}")
            return




def set_genesis_to_state():
    pass # stub