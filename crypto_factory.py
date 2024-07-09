from typing import Any, Tuple
from crypto_handler import CryptoHandler
from ecdsa_handler import ECDSAHandler

class CryptoFactory:

    '''
    Combining the factory pattern with a singleton and
    setting the default handler so that we don't have
    to when implementing this function. This is being
    done to simplify implementation of new handlers in 
    the future as we pivot to different encryption 
    protocols.
    '''

    # Ensure we have a handler active by default
    _crypto_handler: CryptoHandler = ECDSAHandler()

    @staticmethod
    def set_crypto_handler(handler: CryptoHandler) -> None:
        '''
        This allows us to change the handler at run time if
        needed. Could be used when we pivot over to a new
        encryption scheme.
        '''
        CryptoFactory._crypto_handler = handler

    @staticmethod
    def get_crypto_handler() -> CryptoHandler:
        if CryptoFactory._crypto_handler is None:
            raise ValueError(f'ERROR: Crypto handler is not set. It must have been set to none elsewhere in the code.')
        return CryptoFactory._crypto_handler
    
    @staticmethod
    def generate_keys() -> Tuple[Any, Any]:
        return CryptoFactory.get_crypto_handler().generate_keys()
    
    @staticmethod
    def serialize_public_key(public_key: Any) -> str:
        return CryptoFactory.get_crypto_handler().serialize_public_key(public_key)
    
    @staticmethod
    def save_keys(private_key: Any, public_key: Any, filename: str, directory: str = '.') -> str:
        return CryptoFactory.get_crypto_handler().save_keys(private_key, public_key, filename, directory)
    
    @staticmethod
    def load_private_key(filepath: str, salt_file_path: str) -> Any:
        return CryptoFactory.get_crypto_handler().load_private_key(filepath, salt_file_path)
    
    @staticmethod
    def load_public_key(filepath: str) -> Any:
        return CryptoFactory.get_crypto_handler().load_public_key(filepath)
    
    @staticmethod
    def sign_message(private_key: Any, message: bytes) -> bytes:
        return CryptoFactory.get_crypto_handler().sign_message(private_key, message)
    
    @staticmethod
    def verify_signature(public_key: Any, message: bytes, signature: bytes) -> bool:
        return CryptoFactory.get_crypto_handler().verify_signature(public_key, message, signature)
    

    
# Example Usage of the factory
if __name__ == '__main__':
    private_key, public_key = CryptoFactory.generate_keys()

    print(f'Public Key (PEM):\n\n{CryptoFactory.serialize_public_key(public_key)}')

    print('-' * 44)

    hot_wallet_result: str = CryptoFactory.save_keys(private_key, public_key, filename='hot', directory='test')

    print(f'{hot_wallet_result}')

    print('-' * 44)

    private_key = CryptoFactory.load_private_key(filepath='test\\hot_private_key.pem', salt_file_path='test\\hot_salt.bin')
    public_key = CryptoFactory.load_public_key(filepath='test\\hot_public_key.pem')

    print(f'Private Key Object = {private_key}')
    print(f'Public Key Object= {public_key}')

    print('-' * 44)

    test_message = b'This is a quick test to check if the handlers are working as intended'
    signature: bytes = CryptoFactory.sign_message(private_key, test_message)
    print(f'Message Signature: {signature}\n')

    is_valid: bool = CryptoFactory.verify_signature(public_key, test_message, signature)
    print(f'The signature returned: {is_valid}')

    print('-' * 44)

    