from typing import Any, Dict, LiteralString
from enum import Enum
import asyncio
from abstract_communication import AbstractCommunication
from communication_factory import CommunicationFactory
from run_rules import RunRules

from job_file import JobFile

from logging import Logger
from logger_util import setup_logger
logger: Logger = setup_logger('Validator', 'validator.log')

class ValidatorState(Enum):
    DISCOVERY = 1
    SYNC = 2
    PENDING = 3
    REDIRECT = 4
    ACTIVE = 5
    ERROR = 6

class Validator:
    def __init__(self, public_key: bytearray, rules_file: str) -> None:
        logger.info("Initializing Validator")
        self.state = ValidatorState.DISCOVERY
        self.public_key: bytearray = public_key
        self.run_rules = RunRules(rules_file)
        logger.info(f"Rules for {rules_file} have been loaded")
        self.run = False
        self.is_known_validator: bool = self.check_if_known_validator()
        self.comm = None

    async def start(self) -> None:
        '''
        This method is responsible for setting up and running
        the validator class until it is terminated.
        '''

        logger.info("Starting validator...")

        # Start the listener in the background
        self.comm = CommunicationFactory.create_communication("TCP")
        # Need to grab our IP info later
        asyncio.create_task(self.comm.start_listener("127.0.0.1", 4446)) # type: ignore 

        # look for other validators here
        await self.discover_validators()

        self.set_state(ValidatorState.SYNC)
        # Sync logic here
        self.set_state(ValidatorState.ACTIVE)

        while self.run:
            # Begin normal operations here
            ...

    async def stop(self) -> None:
        '''
        This method is responsible for ending the validator loop
        and to communicate to it's peers that it is going offline
        '''

        self.run = False
        logger.info(f"shutting down the validator.")

        try:
            await self.comm.disconnect() # type: ignore
            logger.info(f'Successfully stopped listening')
        except Exception as e:
            logger.error(f'Failed to stop validator from listening. Inside Validator:stop()')
        

    def set_state(self, new_state: ValidatorState) -> None:
        '''
        Changes the state of the validator which is used to determine
        this validators readiness on the network.
        '''

        logger.info(f"Transitioning to {new_state.name} state.")
        self.state: ValidatorState = new_state

    def handle_message(self, message: bytearray) -> None:
        '''
        Logic to handle incoming messages
        '''

        logger.info(f"Handling message: {message}")
        # Implement message handling logic here
        ...

    def send_state_update(self, recipient: bytearray) -> None:
        '''
        This method is used for appending the validators state to the
        beginning of a incoming request so that the user knows the heath
        status of this validator
        '''

        state_info: LiteralString = f"State: {self.state.name}"
        logger.info(f"Sending state update to {recipient.decode('utf-8')}: {state_info}")
        # Logic to send the state update
        ...

    def handle_error(self, error_message: str) -> None:
        '''
        Logic to handle errors and transition to the validator 
        into the ERROR state. Validator should communicate this state
        to it's peer (other validators in the pool).
        '''

        logger.error(f"Error occurred: {error_message}")
        self.set_state(ValidatorState.ERROR)
        # Implement recovery or notification logic here
        ...

    async def discover_validators(self) -> None:
        '''
        This method is for discovering other validators or listening for
        incoming requests for validators to join the pool.
        '''

        logger.info("Discovering validators asynchronously...")

        known_validators: list[str] = self.run_rules.get_known_validator_keys()
        tasks = [] # Collect tasks for connecting validators

        for validator_key in known_validators:
            if validator_key == self.public_key.decode('utf-8'):
                logger.info(f'You are a known validator {validator_key}, so we are not contacting ourselves')
                continue

            logger.info(f'Attempting to connect to validator: {validator_key}')

            # Get contact info for this validator
            contact_info: dict[str, str] = self.get_contact_info(validator_key)
            if contact_info:
                try:
                    logger.info(f'Initializing communication with {validator_key} using {contact_info["method"]}')
                    comm: AbstractCommunication | None = CommunicationFactory.create_communication(contact_info["method"])
                    tasks.append(self.connect_to_validator(comm, validator_key, contact_info))
                except Exception as e:
                    logger.error(f'Failed to connect to validator {validator_key}: {e}')
            else:
                logger.error(f'Failed to retrieve contact info for validator {validator_key}')

        # Await all of the gathered tasks
        if tasks:
            await asyncio.gather(*tasks)
        else:
            logger.info("No other validators to connect to...")

    async def connect_to_validator(self, comm, validator_key, contact_info):
        try:
            await comm.connect(bytearray(validator_key, 'utf-8'), contact_info) # type: ignore
        except Exception as e:
            logger.error(f'Failed to connect to validator {validator_key}: {e}')

    def get_contact_info(self, public_key: str) -> dict:
        '''
        Retrieves the contact information for a validator from the run rules
        based on the public key being passed in.

        Returns:
            Dictionary with the type of communication and the route
        '''
        known_validators = self.run_rules.get_known_validators()

        for validator in known_validators:
            if validator['public_key'] == public_key:
                logger.info(f'Found contact info for public key {public_key}: {validator["contact"]}')
                return validator['contact']
            
        raise ValueError(f'Validator with public key {public_key} was not found in the rin rules file.')
    
    def check_if_known_validator(self) -> bool:
        '''
        This method is responsible for determining if this validator is
        apart of the known validator class within this co-chain
        '''
        
        known_validator_keys: list[str] = self.run_rules.get_known_validator_keys()
        public_key_str: str = self.public_key.decode("utf-8")
        is_known: bool = public_key_str in known_validator_keys
        return is_known

if __name__ == "__main__":
    async def main() -> None:
        public_key = bytearray("validator_pub_key_3", "utf-8")
        validator = Validator(public_key, "UndChain.toml")
        await validator.start()

        await validator.stop()

    asyncio.run(main())
