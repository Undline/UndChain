from enum import Enum
from typing import Dict, List, Optional


class ReliabilitySignal(Enum):
    CHALLENGE_SUCCEEDED = 10
    CHALLENGE_FAILED = -15
    MALICIOUS_BEHAVIOR = -100
    VALIDATOR_UPHELD_REPORT = 25
    VALIDATOR_DISMISSED_REPORT = -5
    USERNAME_PURCHASED = 250
    SUBSCRIPTION_PURCHASED = 500


class ReliabilityManager:
    '''
    ReliabilityManager

    This module manages the XP and Level system for all users on the Modulr network.
    Reliability is modeled as a level-based XP system that mimics real-life trust:
    it is slow to gain and quick to lose. This class provides the mechanism to 
    initialize users, apply XP/reliability signals, and track progress over time.

    Scores are stored locally by validators but ultimately persisted in the network's
    storage layer. This class does not handle consensus—it only provides the
    transformation logic for XP and level changes based on events.

    Features:
    - XP-level system (Level 1 to 100)
    - XP resets to 0 after level-up
    - Positive and negative reliability signals
    - History tracking (configurable max length)
    - Job-based signal uniqueness
    - Output is advisory, to be validated via consensus
    '''

    def __init__(self, max_history: int = 25):
        self.user_data: Dict[str, Dict] = {}
        self.level_table = self._build_level_table()
        self.max_history = max_history

    def _build_level_table(self) -> Dict[int, int]:
        '''
        Builds the XP requirement table for levels 1–100.
        '''

        table = {}
        base = 100
        increment = 20
        for lvl in range(1, 101):
            table[lvl] = base + (lvl - 1) * increment
        return table

    def initialize_user(self, user_id: str) -> None:
        '''
        Initializes a new user with default XP, level, and empty history.
        '''

        if user_id not in self.user_data:
            self.user_data[user_id] = {
                "xp": 0,
                "level": 1,
                "history": [],
                "seen_jobs": set()  # Prevents duplicate job penalty
            }

    def apply_signal(self, user_id: str, signal: ReliabilitySignal, job_id: str, reporter: Optional[str] = None) -> Dict:
        '''
        Applies a reliability signal to a user and updates their XP/level.
        '''

        self.initialize_user(user_id)
        current = self.user_data[user_id]

        if job_id in current["seen_jobs"]:
            return {
                "status": "ignored",
                "reason": "duplicate_job_id",
                "user_id": user_id,
                "job_id": job_id
            }

        current["seen_jobs"].add(job_id)
        xp_gain = signal.value
        new_xp = current["xp"] + xp_gain
        level_up = False

        if new_xp >= self.level_table[current["level"]]:
            new_xp = new_xp - self.level_table[current["level"]]
            current["level"] += 1
            level_up = True
        elif new_xp < 0:
            if current["level"] > 1:
                current["level"] -= 1
                new_xp = max(0, self.level_table[current["level"]] + new_xp)
            else:
                new_xp = 0

        event = {
            "user_id": user_id,
            "job_id": job_id,
            "signal": signal.name,
            "reporter": reporter,
            "old_xp": current["xp"],
            "new_xp": new_xp,
            "level_up": level_up,
            "level": current["level"],
            "status": "applied"
        }

        current["xp"] = new_xp
        current["history"].append(event)
        current["history"] = current["history"][-self.max_history:]

        return event

    def get_user_summary(self, user_id: str) -> Dict:
        '''
        Returns full profile summary for a user.
        '''

        self.initialize_user(user_id)
        data = self.user_data[user_id]
        return {
            "user_id": user_id,
            "level": data["level"],
            "xp": data["xp"],
            "history": list(data["history"])
        }

    def get_level(self, user_id: str) -> int:
        '''
        Returns current level of a user.
        '''

        return self.user_data.get(user_id, {}).get("level", 1)

    def get_xp(self, user_id: str) -> int:
        '''
        Returns current XP of a user.
        '''

        return self.user_data.get(user_id, {}).get("xp", 0)

    def get_history(self, user_id: str) -> List[Dict]:
        '''
        Returns the XP signal history of a user.
        '''
        
        return self.user_data.get(user_id, {}).get("history", [])


# Simulated Local Test
manager = ReliabilityManager()

user = "@Bob"
manager.initialize_user(user)

print("\n--- Initial User State ---")
print(manager.get_user_summary(user))

print("\n--- Applying Signals ---")
print(manager.apply_signal(user, ReliabilitySignal.CHALLENGE_SUCCEEDED, job_id="job-001", reporter="@Alice"))
print(manager.apply_signal(user, ReliabilitySignal.VALIDATOR_UPHELD_REPORT, job_id="job-002", reporter="@Alice"))
print(manager.apply_signal(user, ReliabilitySignal.MALICIOUS_BEHAVIOR, job_id="job-003", reporter="@Alice"))
print(manager.apply_signal(user, ReliabilitySignal.MALICIOUS_BEHAVIOR, job_id="job-003", reporter="@Alice"))  # Duplicate, should be ignored

print("\n--- Final User Summary ---")
print(manager.get_user_summary(user))
