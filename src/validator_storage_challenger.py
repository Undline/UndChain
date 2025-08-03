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
from reliability_manager import ReliabilityManager, ReliabilitySignal

class ValidatorStorageChallenger:
    def __init__(self, validator_id: str, reliability_manager: ReliabilityManager):
        self.validator_id = validator_id
        self.reliability_manager = reliability_manager
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
        job_id: str
    ) -> Dict:
        '''
        Accepts a partner-issued challenge and verifies the reported hash
        against the expected sector content. Updates reliability scores.
        '''

        segment = expected_content[target_offset:target_offset + target_length]
        expected_hash = sha256(segment.encode()).hexdigest()
        passed = (expected_hash == reported_hash)

        # Determine reliability signals
        accused_signal = ReliabilitySignal.CHALLENGE_SUCCEEDED if passed else ReliabilitySignal.CHALLENGE_FAILED
        reporter_signal = ReliabilitySignal.VALIDATOR_UPHELD_REPORT if passed else ReliabilitySignal.VALIDATOR_DISMISSED_REPORT

        accused_result = self.reliability_manager.apply_signal(accused_partner, accused_signal, job_id)
        reporter_result = self.reliability_manager.apply_signal(reporter_partner, reporter_signal, job_id)

        decision = {
            "challenge_id": challenge_id,
            "sector_id": sector_id,
            "accused_partner": accused_partner,
            "reporter_partner": reporter_partner,
            "job_id": job_id,
            "expected_hash": expected_hash,
            "reported_hash": reported_hash,
            "status": "pass" if passed else "fail",
            "reliability_change": {
                accused_partner: accused_result,
                reporter_partner: reporter_result
            }
        }

        self.received_challenges.append({
            "challenge_id": challenge_id,
            "sector_id": sector_id,
            "from": reporter_partner,
            "against": accused_partner,
            "job_id": job_id
        })

        self.decision_log.append(decision)
        return decision

# Test block
if __name__ == "__main__":
    from reliability_manager import ReliabilityManager  # Adjust path if needed

    validator = ValidatorStorageChallenger(
        validator_id="VALIDATOR-001",
        reliability_manager=ReliabilityManager()
    )

    print("🔧 Generating 4GB sector content (this may take a moment)...")
    mock_sector_data = "A" * (4 * 1024 ** 3)

    offset = 123456
    length = 32
    segment = mock_sector_data[offset:offset + length]
    valid_hash = sha256(segment.encode()).hexdigest()
    fake_hash = "badf00d" + valid_hash[7:]

    result_pass = validator.accept_challenge(
        challenge_id="CHAL-0001",
        sector_id="sector_X1",
        target_offset=offset,
        target_length=length,
        reported_hash=valid_hash,
        expected_content=mock_sector_data,
        accused_partner="@PartnerB",
        reporter_partner="@PartnerA",
        job_id="JOB-0001"
    )

    result_fail = validator.accept_challenge(
        challenge_id="CHAL-0002",
        sector_id="sector_X1",
        target_offset=offset,
        target_length=length,
        reported_hash=fake_hash,
        expected_content=mock_sector_data,
        accused_partner="@PartnerC",
        reporter_partner="@PartnerA",
        job_id="JOB-0002"
    )

    print("\n✅ VALID CHALLENGE RESULT:")
    for k, v in result_pass.items():
        print(f"{k}: {v}")

    print("\n❌ INVALID CHALLENGE RESULT:")
    for k, v in result_fail.items():
        print(f"{k}: {v}")
