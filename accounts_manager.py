import os
import tomllib
import tomli_w
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

    def create_account(self, username: str) -> str:
        '''
        Create a new account with a given username; we generate a 
        key pair and saves it to a file.

        Returns:
            str: Path to the created account directory
        '''
        account_path: str = os.path.join(self.accounts_dir, username)
        if os.path.exists(account_path):
            raise ValueError(f"ERROR: Account {username} already exists")
        
        os.makedirs(account_path)

        private_key, public_key = CryptoFactory.generate_keys()

        self.save_keys(username, private_key, public_key, account_path)

        account_info: Dict[str, str] = {
            'username': username,
            'public_key': CryptoFactory.view_public_key(public_key)
        }

        with open(os.path.join(account_path, 'account_info.toml'), 'wb') as file:
            tomli_w.dump(account_info, file)


        return account_path
    
    def save_keys(self, username: str, private_key, public_key, directory: str) -> None:
        '''
        Saves the key pair in the same folder as the username
        '''
        CryptoFactory.get_crypto_handler().save_keys(private_key, public_key, file_name=username, directory=directory)

    def load_account(self, username: str) -> Dict[str, str]:
        '''
        Loads account information for the specified username.

        Returns:
            Dict: Account information in a dictionary format
        '''
        account_path: str = os.path.join(self.accounts_dir, username)
        if not os.path.exists(account_path):
            raise ValueError(f'Account {username} does not exist')
        
        with open(os.path.join(account_path, 'account_info.toml'), 'rb') as file:
            account_info: Dict[str, str] = tomllib.load(file)

        return account_info
    
    def list_accounts(self) -> Tuple[str, ...]:
        '''
        List all accounts saved on the local system.

        Returns:
            Tuple[str]: List of user account names
        '''
        # This folder should only have folders with user names listed
        return tuple(os.listdir(self.accounts_dir))
    
    def delete_account(self, username: str) -> str:
        '''
        Deletes the specified account. Other than testing purposes
        I don't see a reason why a user would delete their account
        unless they had the keys backed-up elsewhere (YOU WILL LOSE
        ALL ACCESS TO THE ACCOUNT OTHERWISE)

        Returns:
            str: Confirmation the account was deleted.
        '''
        account_path: str = os.path.join(self.accounts_dir, username)
        if not os.path.exists(account_path):
            raise ValueError(f'Account {username} does not exist')
        
        for root, dirs, files in os.walk(account_path, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(account_path)

        return f'Account {username} has been deleted.'
    
    def username_request_message(self, username: str) -> str:
        '''
        Creates a message to send to the validator to request this username
        for the provided public key.

        Returns:
            str: This is the message that will be sent to the validator
        '''
        account_info: Dict[str, str] = self.load_account(username)
        public_key: str = account_info['public_key']

        message: str = f'[Username_Request] {username}:{public_key}'

        return message
    
    def rename_account(self, old_username: str, new_username:str) -> str:
        '''
        Renames the specified old_username with the new username. This is 
        used when a username request is denied and the user has to pick a 
        new one.

        Returns:
            str: Confirmation the file has been renamed.
        '''
        old_account_path: str = os.path.join(self.accounts_dir, old_username)
        new_account_path: str = os.path.join(self.accounts_dir, new_username)

        if not os.path.exists(old_account_path):
            raise ValueError(f'Account {old_username} does NOT exist.')
        if os.path.exists(new_account_path):
            raise ValueError(f'Username: {new_username} already exists.')
        
        os.rename(old_account_path, new_account_path)

        account_info_path: str = os.path.join(new_account_path, 'account_info.toml')
        with open(account_info_path, 'rb') as file:
            account_info: Dict[str, str] = tomllib.load(file)

        account_info['username'] = new_username
        with open(account_info_path, 'wb') as file:
            tomli_w.dump(account_info, file)

        return f'Account {old_username} has been renamed to {new_username}'

# Example use / unit tests
if __name__ == '__main__':
    manager = AccountManager()

    # Create a new account
    account_path: str = manager.create_account('Jane')
    print(f'Created an account at: {account_path}')

    print('-' * 44)

    # Load Account
    account: Dict[str, str] = manager.load_account('Jane')
    print(f'Loaded account info for test_user: \n{account}')

    print('-' * 44)

    # List all user accounts
    accounts: Tuple[str, ...] = manager.list_accounts()
    print(f'Accounts: {accounts}')

    print('-' * 44)

    # Username request message
    request: str = manager.username_request_message(username='Jane')
    print(f'Message sent: \n{request}')

    print('-' * 44)

    # Rename the account
    rename: str = manager.rename_account(old_username='Jane', new_username='Bob')
    print(f'{rename}')

    print('-' * 44)

    # Delete user account
    delete_result: str = manager.delete_account('Bob')
    print(delete_result)

    print('-' * 44)

    # List accounts to show it was deleted
    accounts = manager.list_accounts()
    print(f'Accounts after deletion: {accounts}')