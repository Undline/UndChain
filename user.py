''' 
Putting this here as a place holder since I know I will need to refactor common
user methods. The ones I have in here are probably not permanent
'''

from typing import Tuple
import hashlib

class User:
    def __init__(self):
        # Example of creating SHA-256 hash of some data and converting it to a hex string
        self.public_key: str = hashlib.sha256(b'public_key_data').hexdigest()
        self.username: str = '@test'

    def get_account(self) -> Tuple[str, str]:
        """
        Get the account details for this user. Returns the following items:
        - Public Key Hash (str)
        - Username (str)        
        """

        return self.public_key, self.username
    
    def sign(self) -> str:
        """
        Returns the user's signature that is used in all transactions.
        """

        return 'My Signature'
