
# Capsule Security Model

Welcome to the security architecture of Soul Capsule. Here, we believe in real ownership: your memories, your mind, your responsibility.

This document describes **how capsules are protected**, **how to encrypt and decrypt**, and the **philosophy behind it**.

## 🔒 Core Security Principles

- **Local-First**: Capsules are encrypted and decrypted only on your machine. No server. No cloud.
- **Password-Protected**: Only someone with your private password can unlock a capsule.
- **Strong Encryption**: Capsules use AES-256-GCM encryption with PBKDF2 password-based key derivation.
- **No Backdoors**: If you lose the password, the capsule is permanently unrecoverable. No recovery links. No master keys.

## 🔑 How Capsule Encryption Works

Each encrypted `.enc` capsule file contains:

| Part | Size | Purpose |
|:---|:---|:---|
| Salt | 16 bytes | Random salt for password key derivation |
| IV (Nonce) | 12 bytes | Initialization vector for AES encryption |
| Ciphertext | Variable | Encrypted capsule JSON |
| Auth Tag | 16 bytes | Verifies authenticity (tamper-proof) |

Encryption steps:
1. Generate random **salt** and **IV**.
2. Derive a secret key from your password using **PBKDF2** (HMAC-SHA256, 100k iterations).
3. Encrypt the capsule JSON using **AES-256-GCM**.
4. Save `[salt][iv][ciphertext][tag]` into a single `.enc` file.

## 📚 How to Encrypt a Capsule

Use `encrypt_capsule.py`:

```bash
python encrypt_capsule.py
```

You will:
- Provide capsule details.
- Provide your password.
- Get an encrypted `.enc` file inside the `capsules/` directory.

## 🔀 How to Decrypt a Capsule

Use `decrypt_capsule.py`:

```bash
python decrypt_capsule.py
```

You will:
- Provide the encrypted file path.
- Provide your password.
- Get the original capsule JSON printed to the console.

## ⚡ Important Reminders

- **Back up your password safely.** Without it, decryption is impossible.
- **Encrypt new capsules immediately** if they're sensitive.
- **Stay local.** Never upload capsules to shared/cloud locations unless you know what you're doing.

## 💎 Philosophy: Memory as a Treasure

In Soul Capsule, we believe your memories are not "data." They're treasures.
We treat them with the highest level of respect, security, and ownership.

A capsule is not just a file. It's a piece of you.

Lock it wisely. Unlock it only with intention.

---

**Soul Capsule**: Your mind. Your memories. Your freedom.
