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
    
# Example Usage of the factory
if __name__ == '__main__':
    private_key, public_key = CryptoFactory.generate_keys()

    print(f'Public Key (PEM): {CryptoFactory.serialize_public_key(public_key)}')