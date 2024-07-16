import os
import tomllib
from typing import Tuple, Dict
from crypto_factory import CryptoFactory

class AccountManager:
    '''
    This class is meant to create, maintain and load accounts
    (key pairs) that are used for UndChain.
    '''
    def __init__(self, accounts_dir: str = 'accounts') -> None:
        self.accounts_dir: str = accounts_dir
        if not os.path.exists(accounts_dir):
            os.makedirs(accounts_dir)

    def create_accounts(self, username: str) -> str:
        '''
        Create a new account with a given username; we generate a 
        key pair and saves it to a file.

        Returns:
            str: Path to the created account directory
        '''
        account_path: str = os.path.join(self.accounts_dir, username)
        if os.path.exists(account_path):
            raise ValueError("Account already exists")
        
        os.makedirs(account_path)

        private_key, public_key = CryptoFactory.generate_keys()

        self.save_keys(username, private_key, public_key, account_path)

        account_info: Dict[str, str] = {
            'username': username,
            'public_key': CryptoFactory.view_public_key(public_key)
        }

        # Need to find a library that saves toml files from dictionaries
        

        return account_path
    
    def save_keys(self, username: str, private_key, public_key, directory: str) -> None:
        '''
        Saves the key pair in the same folder as the username
        '''
        CryptoFactory.get_crypto_handler().save_keys(private_key, public_key, file_name=username, directory=directory)