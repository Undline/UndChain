''' 
Putting this here as a place holder since I know I will need to refactor common
user methods. The ones I have in here are probably not permanent
'''

import hashlib

class User:
    def __init__(self):
        # Example of creating SHA-256 hash of some data and converting it to a hex string
        self.public_key = hashlib.sha256(b'public_key_data').hexdigest()
        self.username = '@test'

    def get_account(self) -> list:
        """
        Get the account details for this user. Returns a list with the following items:
        - Public Key Hash (str)
        - Username (str)        
        """
        return [self.public_key, self.username]
    
    def sign(self) -> str:
        """
        Returns the user's signature that is used in all transactions.
        """
        return 'Hello there'
