import os
import shutil
import time
import unittest
from src.accounts_manager import AccountManager

'''
Run these tests using:
python -m unittest discover -s tests
'''

class TestAccountsManager(unittest.TestCase):
    def setUp(self) -> None:
        self.manager = AccountManager(accounts_dir='test_accounts')
        if os.path.exists('test_accounts'):
            shutil.rmtree('test_accounts')

    def tearDown(self) -> None:
        if os.path.exists('test_accounts'):
            shutil.rmtree('test_accounts')

    def run(self, result=None) -> None:
        # Need to override the run method to time each test
        start_time = time.time()
        super().run(result)
        end_time = time.time()
        duration = end_time - start_time
        print(f'{self.id()} took {duration:.6f} seconds')

    def test_create_account(self) -> None:
        account_path = self.manager.create_account('user1')
        self.assertTrue(os.path.exists(account_path))
        account_info = self.manager.load_account('user1')
        self.assertEqual(account_info['username'], 'user1')

    def test_load_non_existent_account(self) -> None:
        with self.assertRaises(ValueError):
            self.manager.load_account('does_not_exist')

    def test_save_keys(self) -> None:
        self.manager.create_account('user1')
        account_info = self.manager.load_account('user1')
        self.assertEqual(account_info['username'], 'user1')

    def test_username_request_message(self) -> None:
        self.manager.create_account('user1')
        request_message = self.manager.username_request_message('user1')
        self.assertIn('[Username_Request]', request_message)

    def test_rename_account(self) -> None:
        self.manager.create_account('user1')
        rename_result = self.manager.rename_account('user1', 'user2')
        self.assertEqual(rename_result, 'Account user1 has been renamed to user2')
        account_info = self.manager.load_account('user2')
        self.assertEqual(account_info['username'], 'user2')
        with self.assertRaises(ValueError):
            self.manager.load_account('user1')

    def test_delete_account(self) -> None:
        self.manager.create_account('user1')
        deletion_result = self.manager.delete_account('user1')
        self.assertEqual(deletion_result, 'Account user1 has been deleted.')
        with self.assertRaises(ValueError):
            self.manager.load_account('user1')

    def test_list_accounts(self) -> None:
        self.manager.create_account('user1')
        self.manager.create_account('user2')
        accounts = self.manager.list_accounts()
        self.assertIn('user1', accounts)
        self.assertIn('user2', accounts)

if __name__ == '__main__':
    unittest.main()