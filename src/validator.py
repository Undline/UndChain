from logging import Logger
from logger_util import setup_logger
from enum import Enum
from run_rules import RunRules

logger: Logger = setup_logger('Validator', 'validator.log')

class ValidatorState(Enum):
    DISCOVERY = 1
    SYNC = 2
    PENDING = 3
    REDIRECT = 4
    ACTIVE = 5
    ERROR = 6

class Validator:
    def __init__(self, rules_file: str) -> None:
        logger.info("Initializing Validator")
        self.state = ValidatorState.DISCOVERY
        self.run_rules = RunRules(rules_file)
        logger.info(f"Rules for {rules_file} have been loaded")