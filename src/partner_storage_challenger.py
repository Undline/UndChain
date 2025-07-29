"""
PartnerStorageChallenger

This module coordinates peer-to-peer storage challenges between partners
in the UndChain network. It is responsible for issuing deterministic or
random offset-based challenges to verify whether other partners are
actually storing their assigned sectors.

It is distinct from validator-issued challenges, which are formalized
as job files. This class is used to reduce load on validators by enabling
honest partners to verify each other before escalation is necessary.

This does NOT handle computation or access challenge logic.
"""

import random
import hashlib
from typing import List, Dict


class PartnerStorageChallenger:
    def __init__(self, sector_size: int = 4 * 1024 ** 3):
        self.sector_size = sector_size
        self.challenge_log = []      # all issued challenges
        self.escalation_log = []     # escalation records (failures)

    def issue_challenge(self, sector_id: str, partners: List[str], seed: int) -> dict:
        """
        Issues a challenge request for a specific sector using a deterministic seed.
        Returns the challenge specification and list of recipients (excluding self).
        """
        if len(partners) < 2:
            raise ValueError("At least two distinct partners required to issue a challenge.")

        rng = random.Random(seed)
        offset = rng.randint(0, self.sector_size - 256)
        length = 25  # Fixed byte slice for now

        challenger = rng.choice(partners)
        responders = [p for p in partners if p != challenger]

        challenge = {
            "challenge_id": f"challenge-{seed}-{sector_id}",
            "sector_id": sector_id,
            "issued_by": challenger,
            "target_offset": offset,
            "target_length": length,
            "expected_responses": responders
        }

        self.challenge_log.append(challenge)
        return challenge

    def simulate_partner_response(self, partner_id: str, offset: int, length: int, sector_content: str, corrupt: bool = False) -> str:
        """
        Simulates a partner computing a hash over a segment of the sector.
        Corrupt partners will hash incorrect data for testing purposes.
        """
        data = sector_content[offset:offset + length]
        if corrupt:
            data = "INVALID" + data[7:]
        return hashlib.sha256(data.encode()).hexdigest()

    def compare_responses(self, response_dict: Dict[str, str]) -> Dict:
        """
        Given a dict of partner_id -> hash responses, detects any mismatches.
        Returns details on agreement vs disagreement.
        """
        hash_counts = {}
        for partner, result in response_dict.items():
            hash_counts.setdefault(result, []).append(partner)

        if len(hash_counts) == 1:
            return {
                "status": "valid",
                "matching_hash": next(iter(hash_counts)),
                "responders": list(response_dict.keys())
            }

        return {
            "status": "mismatch",
            "groups": hash_counts,
            "suspected_faulty": [p for h, ids in hash_counts.items() if len(ids) == 1 for p in ids]
        }

    def escalate_to_validator(self, challenge: dict, result: dict) -> None:
        """
        Simulates reporting a failed challenge to the validator.
        For now, this prints and logs the event for testing.
        """
        escalation = {
            "sector_id": challenge["sector_id"],
            "challenge_id": challenge["challenge_id"],
            "challenger": challenge["issued_by"],
            "target_offset": challenge["target_offset"],
            "suspected_faulty": result.get("suspected_faulty", []),
            "hash_groups": result.get("groups", {}),
        }

        self.escalation_log.append(escalation)

        print("\n🚨 ESCALATION TO VALIDATOR 🚨")
        print(f"Sector: {escalation['sector_id']}")
        print(f"Challenge: {escalation['challenge_id']}")
        print(f"Issued By: {escalation['challenger']}")
        print(f"Offset: {escalation['target_offset']}")
        print("Hash Disagreement:")
        for hash_val, responders in escalation["hash_groups"].items():
            print(f"  Hash: {hash_val[:16]}... from: {responders}")
        print(f"Suspected Faulty Partners: {escalation['suspected_faulty']}")


if __name__ == "__main__":
    psc = PartnerStorageChallenger()
    partners = ["A", "B", "C"]
    seed = 12345
    sector_id = "sector_X1"

    # Issue challenge
    challenge = psc.issue_challenge(sector_id, partners, seed)
    print("\nChallenge Issued:")
    print(challenge)

    # Simulate sector data (pretend content is same across all nodes)
    fake_sector_data = "A" * (4 * 1024 ** 3)
    responses = {
        p: psc.simulate_partner_response(p, challenge["target_offset"], challenge["target_length"], fake_sector_data)
        for p in challenge["expected_responses"]
    }

    # Introduce corruption in one responder
    responses["B"] = psc.simulate_partner_response("B", challenge["target_offset"], challenge["target_length"], fake_sector_data, corrupt=True)

    print("\nSimulated Responses:")
    print(responses)

    result = psc.compare_responses(responses)
    print("\nChallenge Outcome:")
    print(result)

    if result["status"] == "mismatch":
        psc.escalate_to_validator(challenge, result)

    print("\n--- Escalation Log ---")
    for e in psc.escalation_log:
        print(e)
