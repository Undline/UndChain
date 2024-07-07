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

    _crypto_handler = ECDSAHandler()

    @staticmethod
    def set_crypto_handler(handler: CryptoHandler) -> None:
        '''
        This allows us to change the handler at run time if
        needed. Could be used when we pivot over to a new
        encryption scheme.
        '''
        CryptoFactory._crypto_handler = handler

