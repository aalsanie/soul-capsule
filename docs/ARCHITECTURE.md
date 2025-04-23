
# 🧱 SoulCapsule Architecture

This document outlines the technical architecture for SoulCapsule — a local-first, style-aware, emotion-driven compression engine for human thought.

---

## 🎯 Project Scope (MVP)

**Goal:** Capture raw human input (text, eventually voice/image), compress it into an emotionally tagged "capsule", and allow decompression into expressive forms (poem, tweet, reflection).

---

## ⚙️ Local System Requirements

| Component       | Minimum Spec               | Notes                                   |
|----------------|----------------------------|-----------------------------------------|
| CPU            | Modern (M1, i5/Ryzen 5)     | No GPU needed unless using local LLM    |
| RAM            | 8–16 GB                     | Memory efficiency is prioritized        |
| Storage        | 500MB–2GB                   | Capsule storage, embeddings, logs       |
| Network        | Optional                    | MVP can run offline                     |
| Privacy        | Local-only                  | Data never leaves the user’s machine    |

---

## ✅ System Requirements Justification

**CPU**  
- Text-based input only (no heavy ML training or image processing yet)
- External OpenAI APIs used for compression (minimal local processing)
- Local inference deferred to later stage with Ollama/Whisper/etc.

**RAM**  
- Python backend (FastAPI), text preprocessing, optional frontend
- Most operations are lightweight and async
- Memory spikes handled by batching or deferral logic

**Storage**  
- Capsule = 1–5KB each  
- 1,000 capsules = ~5MB  
- SQLite/ChromaDB < 50MB unless large embeddings or voice files stored
- Logs, audio, or metadata drive upper end (~2GB budget)

**Security & Availability**  
- Local storage only (no network traffic or cloud sync)
- Optional encrypted export module in future
- Later: versioned capsules, optional local replication (rsync or rclone support)

---

## 🧠 Core Components

### 1. Capsule Engine
Responsible for generating a compressed representation of a thought.

- Input: raw text
- Output: structured JSON capsule
- Process:
  - NLP pre-processing
  - Emotion + style tagging (mocked, later ML)
  - Capsule formatting
  - Local storage

### 2. Decompression Module
- Converts capsule into user-defined expression format:
  - Poem
  - Reflection
  - Summary
- Can also visualize emotion trends over time

### 3. Storage Layer (MVP)
- Flat JSON files
- Index built on ID + timestamp
- Future: SQLite + full-text index + vector store

---

## 🧪 Sample Capsule

```json
{
  "id": "capsule-004",
  "raw_input": "I feel like I'm writing my own map while being lost in it.",
  "emotion_vector": {
    "peace": 0.82,
    "anger": 0.36,
    "detachment": 0.49
  },
  "style": "fragmented, internal",
  "generated_summary": "Wandering through self-made paths",
  "timestamp": "2025-04-17T15:46:28Z"
}
```

---

## 🔒 Security Considerations

- Local storage only (encrypted JSON or SQLite)
- No background syncing or uploads
- Future optional backup/sync module (user-controlled)

---

## 🔮 Future Vision: Federated Capsules

> Interconnected SoulCapsule instances (peer-to-peer) could detect:
> - Shared emotional signals
> - Temporal/societal shifts
> - Emergent thought patterns across the network
>
> Without compromising individual identity.

---

## 🧭 Roadmap Highlights

- [x] Local text compression into capsule
- [ ] Voice input integration
- [ ] Decompression modes
- [ ] Style fingerprint engine
- [ ] Storage evolution: JSON → SQLite → Vector memory
- [ ] Optional encrypted backup
- [ ] Federated capsule prototype (experimental)

---

## 👤 Designed For

- Thoughtful builders  
- Creatives tracking their inner world  
- Privacy-first technologists  
- Future-facing journaling rebels
