from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric.dh import DHPrivateKey
from cryptography.hazmat.primitives.asymmetric.dsa import DSAPrivateKey
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.asymmetric.ed448 import Ed448PrivateKey
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.asymmetric.x448 import X448PrivateKey
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

    def generate_keys(self) -> Tuple[ec.EllipticCurvePrivateKey, ec.EllipticCurvePublicKey]:
        '''
        Generate the elliptic curve key pair
        '''
        private_key: ec.EllipticCurvePrivateKey = ec.generate_private_key(self.curve, default_backend())
        public_key: ec.EllipticCurvePublicKey = private_key.public_key()
        return private_key, public_key
    
    def save_keys(self, private_key: ec.EllipticCurvePrivateKey, public_key: ec.EllipticCurvePublicKey, file_name: str, directory: str = '.') -> str:
        '''
        Saves the private / public key pair to PEM files. Encrypts the
        private key using a passphrase and a salt.

        Returns:
            str: Message indicating that the save happened successfully.
        '''
        passphrase: bytes = getpass.getpass(prompt="Please enter a pass phrase to encrypt the private key: ").encode()
        salt: bytes = generate_salt()

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100_000,
            backend=default_backend()
        )
        key = kdf.derive(passphrase)

        encrypted_private_key: bytes = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(key)
        )

        public_key_bytes: bytes = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        private_key_path: str = f'{directory}\\{file_name}_private_key.PEM'
        with open(private_key_path, 'wb') as private_key_file:
            private_key_file.write(encrypted_private_key)

        public_key_path: str = f'{directory}\\{file_name}_public_key.PEM'
        with open(public_key_path, 'wb') as public_key_file:
            public_key_file.write(public_key_bytes)

        # Need to save the salt
        salt_path = f'{directory}\\{file_name}_salt.bin'
        with open(salt_path, 'wb') as salty_file:
            salty_file.write(salt)

        return f'{file_name} wallet keys have been saved in directory: {directory}'
    
    def load_private_key(self, filepath: str, salt_filepath: str) -> ec.EllipticCurvePrivateKey:
        '''
        Load the specified private key passed in by filename.

        Returns:
            Private key in bytes
        '''
        passphrase: bytes = getpass.getpass(prompt='Please enter the passphrase for the private key: ').encode()

        # Load the salt
        with open(salt_filepath, 'rb') as salty_file:
            salt = salty_file.read()

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100_000,
            backend=default_backend()
        )
        key: bytes = kdf.derive(passphrase)

        with open(filepath, 'rb') as key_file:
            private_key: DHPrivateKey | Ed25519PrivateKey | Ed448PrivateKey | RSAPrivateKey | DSAPrivateKey | ec.EllipticCurvePrivateKey | X25519PrivateKey | X448PrivateKey = serialization.load_pem_private_key(
                key_file.read(),
                password=key,
                backend=default_backend()
            )
        return private_key # type: ignore
    
    def load_public_key(self, filepath: str) -> ec.EllipticCurvePublicKey:
        '''
        Loads a public key from the filepath passed in.

        Returns:
            The public key in bytes
        '''
        with open(filepath, 'rb') as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )
        return public_key # type: ignore
    
    