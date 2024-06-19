from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

import os
import getpass
from crypto_handler import CryptoHandler
from typing import Tuple

def generate_salt(length: int = 16) -> bytes:
    '''
    Generates a random salt used to secure private key

    Returns:
        bytes: The generated salt value
    '''
    return os.urandom(length)

class ECDSAHandler(CryptoHandler):
    '''
    ECSDA implementation of the CryptoHandler base class.
    '''

    def __init__(self, curve: ec.EllipticCurve = ec.SECP521R1(), hash_algorithm= hashes.SHA512) -> None:
        '''
        Initialize the ECSDAHandler with the specific elliptic curve and hash algorithm.
        '''
        self.curve: ec.EllipticCurve = curve
        self.hash_algorithm = hash_algorithm

    