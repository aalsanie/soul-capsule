# 🔐 CapsuleSync: Encrypted Backup Module for SoulCapsule

## Overview

CapsuleSync is a proposed extension for SoulCapsule to add encrypted, portable, user-defined backups of the capsule memory store. It aims to solve the key issue of **local data loss** without sacrificing SoulCapsule's local-first, privacy-first principles.

---

## Goals

- Allow **manual and scheduled** backup of capsules
- Enable **encrypted export** of all user capsules
- Support **user-defined destinations** (local, cloud, drive, repo)
- Provide CLI and future UI interfaces
- Allow **portable restore** from any machine
- Future: Enable peer-to-peer backup sync mesh (opt-in trust)

---

## Features

### Minimum Viable Features (v1)

| Feature            | Description                                                         |
|--------------------|---------------------------------------------------------------------|
| Manual backup      | Run `capsule backup` to export encrypted capsule archive            |
| Manual restore     | Run `capsule restore /path/to/backup.enc`                          |
| Encryption         | Use AES256 or GPG; user supplies passphrase or keypair             |
| Format             | `.capsulepack` = ZIP + encrypted + metadata                        |

---

### 🔜 Planned Features (v2+)

| Feature              | Description                                                         |
|----------------------|---------------------------------------------------------------------|
| Auto-schedule        | Cron-based background backup or on-exit backup                     |
| Destination targets  | Dropbox, USB, Git, iCloud, Syncthing                              |
| Capsule versioning   | Git-like commit model of capsule diffs                             |
| Sync trust mesh      | Share encrypted backups with trusted peers                         |

---

## CLI API (Proposed)

```bash
# Export encrypted backup to a local path
capsule backup --output ./backup.capsulepack --encrypt --passphrase "..."

# Restore from backup archive
capsule restore ./backup.capsulepack --decrypt --passphrase "..."

# Set up backup schedule
capsule config backup --interval=24h --target=dropbox --encrypt
```

---

## File Format

| Extension         | Format                                  | Description                          |
|------------------|------------------------------------------|--------------------------------------|
| `.capsulepack`   | Encrypted ZIP of `/capsules/*.json`      | Encrypted, optionally signed archive |

---

## Design Constraints

- **Never transmits unencrypted capsule data**
- **No cloud or peer interaction by default**
- **Encryption must happen locally**
- **Must work without internet**

---

## Implementation Notes

- Use Python libraries: `cryptography`, `zipfile`, or `gnupg`
- Define JSON schema for backup metadata
- Store encryption hint (not key) in `meta.json` inside archive

---

## Status

This is a proposal. Contributors or feedback welcome before implementation begins.

---

*CapsuleSync ensures your thoughts live on — even if your machine doesn’t.*