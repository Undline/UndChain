'''
ValidatorStorageChallenger

Accepts storage challenges raised by partners and verifies them by simulating
or reconstructing expected file state. If the partner being challenged fails
the integrity check (e.g., wrong Merkle root or hash), an escalation is triggered.

This module represents the validator-side enforcement mechanism for the
storage consensus protocol.
'''

from hashlib import sha256
from typing import Dict, List


class ValidatorStorageChallenger:
    def __init__(self, validator_id: str):
        self.validator_id = validator_id
        self.received_challenges: List[Dict] = []
        self.decision_log: List[Dict] = []

    def accept_challenge(
        self,
        challenge_id: str,
        sector_id: str,
        target_offset: int,
        target_length: int,
        reported_hash: str,
        expected_content: str,
        accused_partner: str,
        reporter_partner: str,
        timestamp: int,
    ) -> Dict:
        '''
        Accepts a partner-issued challenge and verifies the reported hash
        against the simulated data slice.

        Returns a decision dict, logs it internally.
        '''

        segment = expected_content[target_offset:target_offset + target_length]
        expected_hash = sha256(segment.encode()).hexdigest()

        passed = (expected_hash == reported_hash)

        decision = {
            "challenge_id": challenge_id,
            "sector_id": sector_id,
            "accused_partner": accused_partner,
            "reporter_partner": reporter_partner,
            "timestamp": timestamp,
            "expected_hash": expected_hash,
            "reported_hash": reported_hash,
            "status": "pass" if passed else "fail",
            "reliability_recommendation": {
                accused_partner: +0 if passed else -10,
                reporter_partner: +1 if passed else -2
            }
        }

        self.received_challenges.append({
            "challenge_id": challenge_id,
            "sector_id": sector_id,
            "from": reporter_partner,
            "against": accused_partner,
            "timestamp": timestamp
        })

        self.decision_log.append(decision)
        return decision

if __name__ == "__main__":
    '''
    Test to check if we pass a good challenge and flag a failed challenge
    '''
    
    validator = ValidatorStorageChallenger(validator_id="VALIDATOR-001")

    print("🔧 Generating 4GB sector content (this may take a moment)...")
    mock_sector_data = "A" * (4 * 1024 ** 3)  # 4GB of 'A'

    target_offset = 123456
    target_length = 32

    valid_segment = mock_sector_data[target_offset:target_offset + target_length]
    valid_hash = sha256(valid_segment.encode()).hexdigest()
    fake_hash = "badf00d" + valid_hash[7:]

    # Valid challenge
    result1 = validator.accept_challenge(
        challenge_id="CHAL-0001",
        sector_id="sector_X1",
        target_offset=target_offset,
        target_length=target_length,
        reported_hash=valid_hash,
        expected_content=mock_sector_data,
        accused_partner="PartnerB",
        reporter_partner="PartnerA",
        timestamp=1723452000
    )

    # Invalid challenge
    result2 = validator.accept_challenge(
        challenge_id="CHAL-0002",
        sector_id="sector_X1",
        target_offset=target_offset,
        target_length=target_length,
        reported_hash=fake_hash,
        expected_content=mock_sector_data,
        accused_partner="PartnerC",
        reporter_partner="PartnerA",
        timestamp=1723452100
    )

    print("\n✅ VALID CHALLENGE RESULT:")
    for k, v in result1.items():
        print(f"{k}: {v}")

    print("\n❌ INVALID CHALLENGE RESULT:")
    for k, v in result2.items():
        print(f"{k}: {v}")
