'''
SectorManager

Tracks per-sector state changes on a partner node between validator confirmations.
Its primary job is to monitor which files exist in the sector, record all
mutations (writes, updates, deletions), and allow reconstruction of sector
state at any given timestamp.

This is critical for validating storage challenges and ensuring a partner
can prove they handled mutations honestly before a validator confirmed the new Merkle root.

Once the validator confirms the new root, old mutation records can be safely
cleared using `commit_checkpoint()` to conserve memory.
'''

import hashlib
from typing import List, Dict, Optional

class SectorManager:
    def __init__(self, sector_id: str, version: int = 1):
        self.sector_id = sector_id
        self.version = version
        self.files: Dict[str, str] = {}  # file_id -> mock content
        self.mutations: List[Dict] = []  # committed mutations (chronological)
        self.sector_size_limit = self.get_configured_sector_size()
        self.last_confirmed_root: Optional[str] = None

    def get_configured_sector_size(self) -> int:
        '''
        Pretends to read this value from run rules or validator config. Must
        update this later to pull from that file!
        '''

        return 4 * 1024 ** 3  # 4 GB

    def apply_mutation(self, job: dict) -> None:
        '''
        Applies a mutation (write/update/delete) to the current state
        and logs it in mutation history.
        job must include: timestamp, user, action, job_id, affected
        '''

        required_fields = ["job_id", "timestamp", "user_pubkey", "action", "affected"]
        for field in required_fields:
            if field not in job:
                raise ValueError(f"Missing required field in job: {field}")

        for file_id in job["affected"]:
            if job["action"] == "write" or job["action"] == "update":
                self.files[file_id] = f"data::{job['timestamp']}::{file_id}"
            elif job["action"] == "delete":
                self.files.pop(file_id, None)
        self.mutations.append(job)

    def get_state_at(self, timestamp: int) -> Dict[str, str]:
        '''
        Reconstructs the sector state as of the given timestamp
        by replaying mutations up to that point.
        '''

        state: Dict[str, str] = {}
        for job in sorted(self.mutations, key=lambda x: x["timestamp"]):
            if job["timestamp"] > timestamp:
                break
            for file_id in job["affected"]:
                if job["action"] == "write" or job["action"] == "update":
                    state[file_id] = f"data::{job['timestamp']}::{file_id}"
                elif job["action"] == "delete":
                    state.pop(file_id, None)
        return state

    def calculate_merkle_root(self, state: Optional[Dict[str, str]] = None) -> str:
        '''
        Computes a simulated Merkle root by hashing the sorted file:content pairs.
        This is a placeholder for later tree-based implementations.
        '''

        if state is None:
            state = self.files
        flat = "".join(f"{k}:{v}" for k, v in sorted(state.items()))
        return hashlib.sha256(flat.encode()).hexdigest()

    def commit_checkpoint(self, root_hash: str, confirmed_time: int) -> None:
        '''
        Confirms that all mutations up to 'confirmed_time' are permanent and verifiable.
        Clears mutation history prior to that point to reduce memory footprint.
        '''

        self.last_confirmed_root = root_hash
        self.mutations = [m for m in self.mutations if m["timestamp"] > confirmed_time]
    
if __name__ == "__main__":
    import pprint

    sm = SectorManager(sector_id="sector_001")

    # Simulate some job files
    job1 = {
        "job_id": "job-001",
        "timestamp": 1723451000,
        "user_pubkey": "0xBOB",
        "action": "write",
        "affected": ["bob_notes.txt"]
    }

    job2 = {
        "job_id": "job-002",
        "timestamp": 1723451100,
        "user_pubkey": "0xSALLY",
        "action": "write",
        "affected": ["sally_resume.pdf"]
    }

    job3 = {
        "job_id": "job-003",
        "timestamp": 1723451200,
        "user_pubkey": "0xBOB",
        "action": "update",
        "affected": ["bob_notes.txt"]
    }

    job4 = {
        "job_id": "job-004",
        "timestamp": 1723451300,
        "user_pubkey": "0xSALLY",
        "action": "delete",
        "affected": ["sally_resume.pdf"]
    }

    # Apply mutations in order
    sm.apply_mutation(job1)
    sm.apply_mutation(job2)
    sm.apply_mutation(job3)
    sm.apply_mutation(job4)

    # Sanity: Show current state
    print("\n--- Current Sector State ---")
    pprint.pprint(sm.files)

    # Sanity: Show mutation history
    print("\n--- Mutation Log ---")
    pprint.pprint(sm.mutations)

    # Merkle root of current state
    current_root = sm.calculate_merkle_root()
    print(f"\nMerkle Root (Current): {current_root}")

    # Reconstruct sector state BEFORE Sally’s delete
    ts_challenge = 1723451250
    print(f"\n--- Reconstructed State @ {ts_challenge} ---")
    snapshot = sm.get_state_at(ts_challenge)
    pprint.pprint(snapshot)

    snapshot_root = sm.calculate_merkle_root(snapshot)
    print(f"\nMerkle Root (Snapshot @ {ts_challenge}): {snapshot_root}")

    # Commit state up to Sally's delete and clear earlier mutations
    print(f"\n--- Committing Checkpoint @ {ts_challenge} ---")
    sm.commit_checkpoint(snapshot_root, confirmed_time=ts_challenge)

    # Show remaining mutations (should only include job-004)
    print("\n--- Remaining Mutations After Commit ---")
    pprint.pprint(sm.mutations)

    # Merkle root should still match the current one (unchanged files)
    print(f"\nMerkle Root (Post-Commit): {sm.calculate_merkle_root()}")

