import os
import json
import global_vars
from structures.threads_metadata_handlers import GenerationThreadMetadataHandler, ApprovementThreadMetadataHandler
from utils import sha256


def prepare_blockchain():

    # Create directory for chaindata if it does not exist
    if not os.path.exists(global_vars.CHAINDATA_PATH):
        try:
            os.makedirs(global_vars.CHAINDATA_PATH, mode=0o755, exist_ok=True)
        except OSError as e:
            print(f"failed to create CHAINDATA directory: {e}")
        return

    # Load GT - Generation Thread handler
    data = global_vars.BLOCKS_DB.get("GT")

    if data is not None:
        try:
            gt_dict = json.loads(data)
            gt_handler = GenerationThreadMetadataHandler.from_dict(gt_dict)
            global_vars.GENERATION_THREAD_METADATA_HANDLER = gt_handler
        except Exception as e:
            print(f"failed to unmarshal GENERATION_THREAD: {e}")
            return
    
    # Load AT - Approvement Thread handler
    data = global_vars.APPROVEMENT_THREAD_METADATA_DB.get("AT")

    if data is not None:
        try:
            at_dict = json.loads(data)
            at_handler = ApprovementThreadMetadataHandler.from_dict(at_dict)
            if at_handler.Cache is None:
                at_handler.Cache = {}
            global_vars.APPROVEMENT_THREAD_METADATA_HANDLER.Handler = at_handler
        except Exception as e:
            print(f"failed to unmarshal APPROVEMENT_THREAD: {e}")
            return


    # Initialize genesis state if version is -1
    if global_vars.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.CoreMajorVersion == -1:
        
        set_genesis_to_state()

        try:
            serialized = json.dumps(
                global_vars.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.to_dict()
            )
            global_vars.APPROVEMENT_THREAD_METADATA_DB.put("AT", serialized)
        except Exception as e:
            print(f"failed to save APPROVEMENT_THREAD: {e}")
            return




def set_genesis_to_state():
    pass # stub