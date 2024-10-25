from run_rules import RunRules
from typing import Any, Dict, List, Optional, TypedDict

from logging import Logger
from logger_util import setup_logger
logger: Logger = setup_logger('ValidatorCore', 'validator_core.log')

class PartnerSubscription(TypedDict):
    utility: str
    busy: bool

class ValidatorCore:
    """
    Core logic class for managing validator operations, partner subscriptions, 
    perception scores, the ledger, and UnaS.
    """

    def __init__(self) -> None:
        """
        Initialize the core structures used by validators, including the validator queue,
        partner subscription list, perception scores, ledger (blockchain), and UnaS.
        """
        self.validator_queue: List[Dict[str, Any]] = []  # Queue of validator public keys waiting for tasks
        self.partner_subscription_list: Dict[str, PartnerSubscription] = {}  # {partner_key: {utility, busy}}
        self.perception_scores: Dict[str, int] = {}  # Maps user public keys to perception scores
        self.ledger: List[Dict[str, str]] = []  # Placeholder for blockchain structure (linked list-like)
        self.unas: Dict[str, str] = {}  # UnaS mapping usernames to public keys (UndChain Naming Service)
        self.minimum_perception_score= 444 # TODO: Need to grab this from the run rules file

    def add_validator_to_queue(self, public_key: str, latency: float, capacity: int, uptime: float, perception_score: float) -> Optional[int]:
        '''
        Adds a validator to the queue with its metrics and returns its 1-based position.
        Returns None if the validator's perception score is below the threshold.
        '''

        if perception_score < self.minimum_perception_score:
            logger.warning(f"Validator {public_key} was not added. Perception score ({perception_score}) is below the minimum threshold ({self.minimum_perception_score}).")
            return None

        validator_data: dict[str, Any] = {
            "public_key": public_key,
            "latency": latency,
            "capacity": capacity,
            "uptime": uptime,
            "perception_score": perception_score
        }

        self.validator_queue.append(validator_data)
        return len(self.validator_queue)


    def subscribe_partner(self, partner_key: str, utility: str) -> None:
        """
        Subscribe a partner to a utility service and mark them as available.
        :param partner_key: Partner's public key.
        :param utility: The utility type (storage, computation, access).
        """
        self.partner_subscription_list[partner_key] = {"utility": utility, "busy": False}

    def set_partner_busy(self, partner_key: str, busy: bool) -> None:
        """
        Set the busy status of a partner.
        :param partner_key: Partner's public key.
        :param busy: Boolean indicating whether the partner is busy.
        """
        if partner_key in self.partner_subscription_list:
            self.partner_subscription_list[partner_key]["busy"] = busy

    def get_available_partners(self, utility: str) -> List[str]:
        """
        Retrieve a list of partners available for a specific utility.
        :param utility: The utility type (storage, computation, access).
        :return: List of partner public keys available for the utility.
        """
        return [
            key for key, data in self.partner_subscription_list.items() 
            if data["utility"] == utility and not data["busy"]
        ]

    def update_perception_score(self, user_key: str, score: int) -> None:
        """
        Update the perception score of a user.
        :param user_key: The user's public key.
        :param score: The updated perception score.
        """
        self.perception_scores[user_key] = score

    def get_perception_score(self, user_key: str) -> Optional[int]:
        """
        Retrieve the perception score of a user.
        :param user_key: The user's public key.
        :return: The perception score or None if the user is not found.
        """
        return self.perception_scores.get(user_key)

    def add_block_to_ledger(self, block_data: Dict[str, str]) -> None:
        """
        Add a new block to the ledger (blockchain).
        :param block_data: The block's transaction data.
        """
        self.ledger.append(block_data)

    def map_unas_name(self, username: str, public_key: str) -> None:
        """
        Map a username to a public key in the UnaS.
        :param username: The user's chosen alias.
        :param public_key: The user's public key.
        """
        self.unas[username] = public_key

    def get_unas_mapping(self, username: str) -> Optional[str]:
        """
        Retrieve the public key associated with a username in the UnaS.
        :param username: The user's chosen alias.
        :return: The associated public key or None if not found.
        """
        return self.unas.get(username)

    def compare_hashes(self, hash_1: str, hash_2: str) -> bool:
        """
        Compare two hash values for equality.
        :param hash_1: First hash value.
        :param hash_2: Second hash value.
        :return: Boolean indicating whether the hashes are equal.
        """
        return hash_1 == hash_2

# Test the ValidatorCore functionalities
if __name__ == "__main__":
    core = ValidatorCore()

    # Test validator queue functionality
    position1 = core.add_validator_to_queue("validator_1_pub_key", latency=10.0, capacity=100, uptime=0.99, perception_score=500)
    position2 = core.add_validator_to_queue("validator_2_pub_key", latency=12.0, capacity=80, uptime=0.97, perception_score=450)
    
    # Output validator queue with positions
    print("Validator Queue:", core.validator_queue)
    print(f"Position of validator_1: {position1}")
    print(f"Position of validator_2: {position2}")

    # Test validator with low perception score
    low_score_position = core.add_validator_to_queue("validator_4_pub_key", latency=15.0, capacity=90, uptime=0.98, perception_score=200)
    print("Position of validator_4 with low perception score:", low_score_position)  # Should be None

    # Test partner subscription and availability
    core.subscribe_partner("partner_1_pub_key", "storage")
    core.subscribe_partner("partner_2_pub_key", "computation")
    print("Available partners for storage:", core.get_available_partners("storage"))
    
    core.set_partner_busy("partner_1_pub_key", True)
    print("Available partners for storage after setting partner_1 busy:", core.get_available_partners("storage"))

    # Test perception scores
    core.update_perception_score("user_1_pub_key", 85)
    print("Perception score of user_1:", core.get_perception_score("user_1_pub_key"))

    # Test UnaS functionality
    core.map_unas_name("user1", "user_1_pub_key")
    print("Public key for user1:", core.get_unas_mapping("user1"))

    # Test ledger/blockchain
    block_data: Dict[str, str] = {"transaction": "user1 pays user2"}
    core.add_block_to_ledger(block_data)
    print("Ledger:", core.ledger)

    # Add another validator and get their position in the queue
    validator_public_key = "validator_3_pub_key"
    position3 = core.add_validator_to_queue(validator_public_key, latency=9.0, capacity=110, uptime=0.995, perception_score=480)
    print(f"Validator {validator_public_key} was added at position {position3}")


