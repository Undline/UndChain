import enum
from typing import List, Tuple
from user import User
from console_colors import Console_Colors as cli
from chain_rules import known_validator

class NetworkState(enum.Enum):
    DISCOVERY = 1
    TIME_SYNC = 2
    READY = 3
    BUSY = 4
    LOW_TRUST = 5

class Validator(User):
    def __init__(self) -> None:
        '''
        We initialize into the discovery state, since when the validator is 
        coming online we are always searching for other validators. We then iterate
        through each chain to determine which one we should participate in. 
        '''

        super().__init__()
        self.state: NetworkState = NetworkState.DISCOVERY
        self.chains: List[Tuple[int, int]] = self.chain_select()

        # Iterate through each chain and see if you are a known validator
        for chain in self.chain_select():
            self.discover(chain)

    def chain_select(self) -> List[Tuple[int, int]]:
        '''
        This method is used to determine which chain you wish to work on. So that
        you not having to select it every time you come online we will save the list
        of chains you are working on and go off that. 

        Returns a list of chain IDs from your preference
        '''

        # Just return the main chain ID with the test network ID
        return [(0, 0)]


    def discover(self, chain_ID: tuple[int, int]) -> None:
        '''
        This method is designed to be ran if you are in discovery mode so you can
        find other validators on the network and connect to them
        '''
        if self.state == NetworkState.DISCOVERY:
            print(f'{cli.MAGENTA}Searching for Validators...{cli.RESET}')
            if known_validator(self.get_account(), chain_ID):
                print(f'Awesome! I\'m part of the cool kids club. Reach out to the other known validators and wait for unknown validators to come on-line.')
        pass

if __name__ == '__main__':
    validator_instance = Validator()
    
