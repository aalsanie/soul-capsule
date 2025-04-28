
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import json

def decrypt_capsule(file_path, password):
    with open(file_path, "rb") as f:
        blob = f.read()

    salt = blob[:16]
    iv = blob[16:28]
    ciphertext = blob[28:-16]
    tag = blob[-16:]

    backend = default_backend()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
        backend=backend
    )
    key = kdf.derive(password.encode())

    decryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv, tag),
        backend=backend
    ).decryptor()

    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    capsule = json.loads(plaintext.decode('utf-8'))
    return capsule

if __name__ == "__main__":
    file_path = input("Enter encrypted capsule path: ")
    password = input("Enter decryption password: ")
    capsule = decrypt_capsule(file_path, password)
    print(json.dumps(capsule, indent=2))
