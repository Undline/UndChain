from abc import ABC, abstractmethod
from typing import Tuple, Any

class CryptoHandler(ABC):
    '''
    This is an abstract class that handles all of the 
    cryptography needs for UndChain. This was made so that
    UndChain can change it's cryptographic algorithm without
    a complete re-write... Ideally
    '''

    @abstractmethod
    def generate_keys(self) -> Tuple[Any, Any]:
        '''
        Generates a public / private key pair

        Returns:
            Tuple[Any, Any]: Generated Private and Public keys.
        '''
        pass

    @abstractmethod
    def serialize_public_key(self, public_key: Any) -> str:
        '''
        Serializes the public key to a PEM format

        Returns:
            str: The public key in PEM format.
        '''

    @abstractmethod
    def save_keys(self, private_key: Any, public_key: Any, file_name: str, directory: str = '.') -> str:
        '''
        Saves the private and public keys to a PEM file. Encrypts the private key.

        Returns:
            bool: A message indicating the keys were saved successfully.
        '''
        pass

    @abstractmethod
    def load_private_key(self, filepath: str, salt_filepath: str) -> Any:
        '''
        Loads an encrypted private key from a PEM file.

        Returns:
            Any: The private key
        '''

    @abstractmethod
    def load_public_key(self, filepath: str) -> Any:
        '''
        Loads a public key from the PEM file.

        Returns:
            Any: Public Key
        '''
        pass

    @abstractmethod
    def sign_message(self, private_key: Any, message: bytes) -> bytes:
        '''
        Signs a message using the private key.

        Returns:
            bytes: The signature in bytes
        '''
        pass

    @abstractmethod
    def verify_signature(self, public_key: Any, message: bytes, signature: bytes) -> bool:
        '''
        Verifies that the message received (in bytes) 
        was signed by the originator using their private key.

        Returns:
            bool: If signature is valid return true
        '''
        pass

    @abstractmethod
    def symmetric_encrypt_message(self, public_key: Any, message: bytes) -> Tuple[bytes, bytes, bytes, bytes]:
        '''
        Encrypts a message using the provided public key for AES symmetric encryption.

        Returns:
            Tuple[bytes, bytes, bytes, bytes]: The cipher text, ephemeral public key, nonce, and authentication tag
        '''
        pass

    @abstractmethod
    def symmetric_decrypt_message(self, private_key: Any, cipher_text: bytes, ephemeral_public_key_bytes: bytes, nonce: bytes, tag: bytes) -> bytes:
        '''
        Decrypts a message using the provided private key
        and AES for symmetric decryption.

        Returns:
            bytes: The decrypted message.
        '''
        pass

    @abstractmethod
    def derive_symmetric_key(self, private_key: Any, public_key: Any) -> bytes:
        '''
        Derive a symmetric key from the shared secret key exchange.

        Returns:
            bytes: The Derived symmetric key.
        '''
        pass

    @abstractmethod
    def asymmetric_encrypt_message(self, public_key: Any, message: bytes) -> Tuple[bytes, bytes, bytes,bytes]:
        '''
        Encrypts a message with the provided public key (asymmetric encryption)

        Returns:
            Tuple[bytes, bytes, bytes]: The encrypted message, ephemeral public key, and nonce.
        '''
        pass

    @abstractmethod
    def asymmetric_decrypt_message(self, private_key: Any, encrypted_message: bytes, ephemeral_public_key_bytes: bytes, nonce: bytes, tags: bytes) -> bytes:
        '''
        Decrypt a message using the private key (asymmetric encryption)

        Returns:
            bytes: Decrypted message in bytes.
        '''
        pass
