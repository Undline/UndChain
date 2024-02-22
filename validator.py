import enum
from user import User
from console_colors import Console_Colors as cc

class NetworkState(enum.Enum):
    DISCOVERY = 1
    TIME_SYNC = 2
    READY = 3
    BUSY = 4
    LOW_TRUST = 5

class Validator(User):
    def __init__(self) -> None:
        """When the validator class initializes, default to a discovery state."""
        super().__init__()
        self.state = NetworkState.DISCOVERY
        self.discover()

    def discover(self):
        '''
        This method is designed to be ran if you are in discovery mode so you can
        find other validators on the network and connect to them
        '''
        if self.state == NetworkState.DISCOVERY:
            print(f'{cc.MAGENTA}Ehh... Dark and cold 😨 I need friends...{cc.RESET}')
        pass

if __name__ == '__main__':
    validator_instance = Validator()
    print(validator_instance.get_account())
    print(validator_instance.sign())
    print(validator_instance.state) 
    
