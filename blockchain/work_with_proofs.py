from structures.block import Block
from structures.threads_metadata_handlers import EpochHandler

def get_block(epoch_index: int, block_creator: str, block_index: int) -> Block:
    pass


def verify_aggregated_epoch_finalization_proof() -> bool:
    pass


def verify_aggregated_finalization_proof() -> bool:
    pass

def verify_aggregated_leader_rotation_proof() -> bool:
    pass

def check_alrp_chain_validity() -> bool:
    pass


def get_verified_aggregated_finalization_proof_by_block_id(block_id:str) -> bool:
    pass

def get_first_block_in_epoch(epoch_handler: EpochHandler) -> Block:
    pass
