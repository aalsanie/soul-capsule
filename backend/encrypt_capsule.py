
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import json

def encrypt_capsule(capsule, password, output_path):
    backend = default_backend()
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
        backend=backend
    )
    key = kdf.derive(password.encode())

    iv = os.urandom(12)
    encryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv),
        backend=backend
    ).encryptor()

    plaintext = json.dumps(capsule).encode('utf-8')
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    with open(output_path, "wb") as f:
        f.write(salt + iv + ciphertext + encryptor.tag)

if __name__ == "__main__":
    capsule_data = {
        "id": "your-id-here",
        "raw_input": "your-raw-text-here",
        "emotion_vector": {"example": 0.5},
        "style": "example-style",
        "generated_summary": "your-summary-here",
        "timestamp": "your-timestamp-here"
    }
    output_file = "capsules/your-capsule-id.json.enc"
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    password = input("Enter encryption password: ")
    encrypt_capsule(capsule_data, password, output_file)
    print(f"Encrypted capsule saved to {output_file}")
