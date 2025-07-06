from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey,
)
from cryptography.hazmat.primitives import serialization

def generate_key_pair() -> tuple[str, str]:

    private_key = Ed25519PrivateKey.generate()
    public_key = private_key.public_key()

    private_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PrivateFormat.Raw,
        encryption_algorithm=serialization.NoEncryption(),
    )
    public_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PublicFormat.Raw,
    )

    return private_bytes.hex(), public_bytes.hex()


def sign_message(private_key_hex: str, message: str) -> str:

    private_bytes = bytes.fromhex(private_key_hex)
    private_key = Ed25519PrivateKey.from_private_bytes(private_bytes)
    signature = private_key.sign(message.encode('utf-8'))
    return signature.hex()


def verify_signature(public_key_hex: str, message: str, signature_hex: str) -> bool:

    public_bytes = bytes.fromhex(public_key_hex)
    public_key = Ed25519PublicKey.from_public_bytes(public_bytes)
    signature = bytes.fromhex(signature_hex)

    try:
        public_key.verify(signature, message.encode('utf-8'))
        return True
    except Exception:
        return False


def main():
    # Generate key pair
    priv, pub = generate_key_pair()
    print("🔐 Ed25519 key pair generated")
    print("Private key:", priv)
    print("Public key :", pub)

    # Original message
    msg = "Secret message"
    print("\n📨 Message:", msg)

    # Sign the message
    sig = sign_message(priv, msg)
    print("✍️ Signature:", sig)

    # Verify the signature
    valid = verify_signature(pub, msg, sig)
    print("✅ Signature is valid!" if valid else "❌ Signature is invalid!")


if __name__ == "__main__":
    main()