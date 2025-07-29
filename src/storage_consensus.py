'''
StorageConsensus Module

This module handles the consensus logic around distributed storage validation.
It is NOT responsible for raw storage or file handling — those are part of the
Storage or Sector modules. Instead, StorageConsensus is responsible for coordinating
the rules and behaviors that ensure partners are storing data truthfully over time.

Key Responsibilities:
- Orchestrates and verifies challenge/response flows between partners.
- Interfaces with validators to issue deterministic, zero-value job-based challenges.
- Validates Merkle proofs (when escalated), including root matching and path validation.
- Tracks per-sector modification history tied to job file IDs and timestamps.
- Differentiates between mutable and immutable storage types.
- Assigns and enforces reputation score adjustments based on outcome of challenges.
- Delegates all final failure decisions to the validator after partner-vs-partner disputes.
- Abstracts sector size and supports future scaling (e.g., 4GB → 4TB).
- Avoids direct file access — expects partners to return signatures and hashes only.

Important Notes:
- All validator-issued challenges are formalized as job files with 0 MTR value.
- Partners must not challenge sectors they hold themselves.
- Challenge assignments are deterministic (seeded from the previous block hash).
- This module assumes all proofs and mutations are cryptographically signed.

This is a trust-minimized enforcement layer designed to ensure network-wide honesty
in a decentralized storage market. It prioritizes validator efficiency and scales
without central dependencies.
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

            for file_id in job.get("affected", []):
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

        state = {}
        for job in sorted(self.mutations, key=lambda x: x["timestamp"]):
            if job["timestamp"] > timestamp:
                break
            for file_id in job.get("affected", []):
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