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
    
    def serialize_public_key(self, public_key: ec.EllipticCurvePublicKey) -> str:
        '''
        Serializes the public key in PEM format

        Returns:
            str: The public key in PEM format
        '''
        public_key_pem: str = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')
        return public_key_pem
    
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
    
    def sign_message(self, private_key: ec.EllipticCurvePrivateKey, message: bytes) -> bytes:
        '''
        This is used for signing messages using the EC private key.

        Returns:
            bytes: The signature
        '''
        signature = private_key.sign(
            message,
            ec.ECDSA(self.hash_algorithm())
        )
        return signature
    
    def verify_signature(self, public_key: ec.EllipticCurvePublicKey, message: bytes, signature: bytes) -> bool:
        '''
        Verifies a signature using the EC public key.

        Returns:
            bool: True if the signature is valid
        '''
        try:
            public_key.verify(
                signature,
                message,
                ec.ECDSA(self.hash_algorithm())
            )
            return True
        except:
            return False
        
    def derive_symmetric_key(self, private_key: ec.EllipticCurvePrivateKey, public_key: ec.EllipticCurvePublicKey) -> bytes:
        '''
        Derive a symmetric key from a shared secret using a DH key exchange. Used
        by both the sender and receiver. This is used in both encrypt and decrypt
        symmetric message.

        Returns:
            bytes: The derived symmetric key
        '''
        shared_secret: bytes = private_key.exchange(ec.ECDH(), public_key)

        derived_key: bytes = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'handshake data',
            backend=default_backend()
        ).derive(shared_secret)
        # NOTE: Need to read up more on this

        return derived_key
    
    def symmetric_encrypt_message(self, public_key: ec.EllipticCurvePublicKey, message: bytes) -> Tuple[bytes, bytes, bytes, bytes]:
        '''
        Encrypts a message using the public key and AES for symmetric encryption. This 
        is used during the DH exchange

        Returns:
            Tuple[bytes, bytes, bytes, bytes]: The cipher text, ephemeral key, nonce and authentication tag
        '''
        ephemeral_private_key = ec.generate_private_key(public_key.curve, default_backend())
        ephemeral_public_key = ephemeral_private_key.public_key()

        derived_key: bytes = self.derive_symmetric_key(ephemeral_private_key, public_key)

        nonce = os.urandom(12)
        encryptor = Cipher(
            algorithms.AES(derived_key),
            modes.GCM(nonce),
            backend=default_backend()
        ).encryptor()
        ciphertext = encryptor.update(message) + encryptor.finalize()

        return ciphertext, ephemeral_public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
            ), nonce, encryptor.tag
    
    def symmetric_decrypt_message(self, private_key: ec.EllipticCurvePrivateKey, cipher_text: bytes, ephemeral_public_key_bytes: bytes, nonce: bytes, tag: bytes) -> bytes:
        '''
        Decrypt a message using the provided ECDSA private key and AES symmetric decryption. DH

        Returns:
            bytes: The decrypted message
        '''
        ephemeral_public_key = serialization.load_pem_public_key(
            ephemeral_public_key_bytes,
            backend=default_backend()
        )
        
        derived_key: bytes = self.derive_symmetric_key(private_key, ephemeral_public_key) # type: ignore
        
        decryptor = Cipher(
            algorithms.AES(derived_key),
            modes.GCM(nonce, tag),
            backend=default_backend()
        ).decryptor()
        decrypted_message: bytes = decryptor.update(cipher_text) + decryptor.finalize()

        return decrypted_message
    
    def asymmetric_encrypt_message(self, public_key: ec.EllipticCurvePublicKey, message: bytes) -> Tuple[bytes, bytes, bytes, bytes]:
        '''
        Encrypt a message using the provided public key

        Returns:
            Tuple[bytes, bytes, bytes]: The encrypted message, ephemeral public key, and nonce.
        '''
        ephemeral_private_key = ec.generate_private_key(public_key.curve, default_backend())
        ephemeral_public_key = ephemeral_private_key.public_key()

        shared_secret = ephemeral_private_key.exchange(ec.ECDH(), public_key)
        derived_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'handshake data',
            backend=default_backend()
        ).derive(shared_secret)

        nonce = os.urandom(12)
        encryptor = Cipher(
            algorithms.AES(derived_key),
            modes.GCM(nonce),
            backend=default_backend()
        ).encryptor()
        ciphertext = encryptor.update(message) + encryptor.finalize()
        tag = encryptor.tag

        return ciphertext, ephemeral_public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ), nonce, tag
    
    def asymmetric_decrypt_message(self, private_key: ec.EllipticCurvePrivateKey, encrypted_message: bytes, ephemeral_public_key_bytes: bytes, nonce: bytes, tag: bytes) -> bytes:
        '''
        Decrypts a message using the provided private key along with the 
        ephemeral key sent by originator

        Returns:
            bytes: Decrypted message in bytes.
        '''
        ephemeral_public_key = serialization.load_pem_public_key(
            ephemeral_public_key_bytes,
            backend=default_backend()
        )
        
        shared_secret = private_key.exchange(ec.ECDH(), ephemeral_public_key) # type: ignore
        derived_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'handshake data',
            backend=default_backend()
        ).derive(shared_secret)
        
        decryptor = Cipher(
            algorithms.AES(derived_key),
            modes.GCM(nonce, tag),
            backend=default_backend()
        ).decryptor()
        decrypted_message = decryptor.update(encrypted_message) + decryptor.finalize()

        return decrypted_message
    
# Test usage
if __name__ == '__main__':
    handler = ECDSAHandler()

    # Generate Keys
    private_key, public_key = handler.generate_keys()

    print(f'Public key (PEM):\n\n{handler.serialize_public_key(public_key)}')

    print('-' * 44)

    #Save keys
    hot_wallet_result: str = handler.save_keys(private_key=private_key, public_key=public_key, file_name='hot', directory='test')
    cold_wallet_result: str = handler.save_keys(private_key=private_key, public_key=public_key, file_name='cold', directory='test')

    print(hot_wallet_result)
    print(cold_wallet_result)

    print('-' * 44)

    #Load keys
    private_key: ec.EllipticCurvePrivateKey = handler.load_private_key('test\\hot_private_key.pem', 'test\\hot_salt.bin')
    public_key: ec.EllipticCurvePublicKey = handler.load_public_key('test\\hot_public_key.pem')

    #Sign and verify a message
    message = b'Test message'
    signature: bytes = handler.sign_message(private_key, message)
    print(f'Signature: {signature}')
    print('-' * 44)

    is_valid: bool = handler.verify_signature(public_key, message, signature)
    print(f'Signature valid: {is_valid}')
    print('-' * 44)

    # Encrypt and decrypt a message
    encrypted_message, ephemeral_public_key_bytes, nonce, tag = handler.symmetric_encrypt_message(public_key, message)

    print(f'Encrypted message: {encrypted_message}')
    print(f'Ephemeral public key: {ephemeral_public_key_bytes}')
    print(f'Nonce: {nonce}')
    print(f'Tag: {tag}')
    print('-' * 44)

    decrypted_message: bytes = handler.symmetric_decrypt_message(private_key, encrypted_message, ephemeral_public_key_bytes, nonce, tag)
    print(f'Decrypted message: {decrypted_message}')

    print('-' * 44)

    # Asymmetric encryption and decryption
    asymmetric_encrypted_message, ephemeral_public_key_bytes, nonce, tag = handler.asymmetric_encrypt_message(public_key, message)
    print(f'Asymmetric Encrypted message: {asymmetric_encrypted_message}')

    asymmetric_decrypted_message = handler.asymmetric_decrypt_message(private_key, asymmetric_encrypted_message, ephemeral_public_key_bytes, nonce, tag) # type: ignore
    print(f'Asymmetric Decrypted message: {asymmetric_decrypted_message}')
