
# 🧠 SoulCapsule

> **Compress your thoughts. Preserve your voice. Reflect your soul.**

**SoulCapsule** is not a journaling app.  
It is a **style-driven, emotion-aware compression engine** for human thought.

Built to mirror your inner world with expressive fidelity — not just storing what you said, but **how it felt when you said it**.

---

# soul-capsule: A Damn Good Compression Algorithm with Style

> *"What if your AI didn’t just respond, but remembered? Not just context, but you — your style, your rhythm, your soul."*

**soul-capsule** is a decentralized, local-first AI assistant designed to evolve with you. It’s not a chatbot. Not a tool. It’s a **compression algorithm for the self** — capturing your patterns, thoughts, emotional tone, and digital rhythm to help you think better, live lighter, and connect deeper with your own mind.

---

## 📚 Table of Contents

- [Why SoulCapsule?](#-why-soulcapsule)
- [Key Features (MVP)](#-key-features-mvp)
- [Roadmap](#-roadmap)
- [Tech Stack](#-tech-stack)
- [Repo Structure (Planned)](#-repo-structure-planned)
- [Example Use Cases](#example-use-cases)
- [Long-Term Vision](#long-term-vision)
- [Manifesto](#-manifesto)
- [Creator](#-creator)
- [License](#license)
- [Status](#status)
- [Installation (Placeholder)](#installation-placeholder)
- [Running Locally (Placeholder)](#running-locally-placeholder)

## 🚀 Why SoulCapsule?

Most tools capture words. We capture **the moment's emotional fingerprint**.  
Your tone. Your drift. Your energy.  
Each capsule is a preserved signal — minimalist, expressive, time-stamped, and *you*.

Today’s GenAI systems are stateless. Contextless. Faceless. You ask — it responds — and forgets. Every prompt is a reset.

We believe in something more intimate:
- An AI that *remembers you* — your tone, your logic, your ideas.
- An AI that *compresses* months of thought into a single word or nudge.
- An AI that *lives with you*, not in the cloud — privately, securely, and freely.

---

## 🔍 Key Features (MVP)

- **Text-to-Capsule Compression**
    - Input raw thoughts → get an expressive, structured capsule
    - Emotion vector tagging + placeholder style detection

- **Decompression Modes** *(v0.2 planned)*
    - Reflective insight
    - Poetic echo
    - Tweet summary
    - Self-dialogue

- **Capsule Structure**
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

## 🧭 Roadmap

✅ Compress text into capsule  
✅ Style tag extraction  
⬜ Voice input  
⬜ Decompression output modes

---

## 🛠️ Tech Stack

- **LLM Engine**: Mistral, Phi, Claude (via Bedrock), or GPT via OpenRouter
- **Vector Store**: ChromaDB or LanceDB
- **Interface**: Python CLI, Electron app, VS Code extension (TBD)
- **Memory Manager**: Flat file, SQLite, or local secure storage
- **Style Matching**: Sentence embeddings + stylometry tools
- **Backend**: FastAPI + Python
- **Frontend** (planned): React / Next.js
- **Storage**: Local JSON (for MVP), future: vector DB

---

### 🧠 Local AI Backend (New in May 2025)

SoulCapsule includes a local-only AI backend for emotion and summary extraction — no cloud dependencies.

**Models Used:**
- [`t5-small`](https://huggingface.co/t5-small) — Summarization
- [`j-hartmann/emotion-english-distilroberta-base`](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base) — Emotion classification

These are downloaded and cached via a single setup script.  
Once installed, capsule creation uses them under the hood to compress thoughts with style and feeling.

---

## 🧱 Repo Structure (Planned)

```
soul-capsule/
├── backend/
│   ├── main.py             # API entrypoint
│   ├── compression.py      # Core capsule logic
│   └── utils.py
├── capsules/               # Compressed memory units
├── frontend/               # (UI - planned)
├── tests/
├── README.md
└── MANIFESTO.md
```

---

## Example Use Cases

- Summarize your day in *your tone*
- Give suggestions based on recent code and conversations
- Compose emails or notes that “sound like you”
- Reflect on how your thinking has changed over time
- Remember forgotten goals or unfinished thoughts from weeks ago

---

## Long-Term Vision

We imagine an ecosystem of:
- **Personal agents** that sync across devices without needing the cloud
- **Style capsules** — compressed representations of your thinking style
- **Contextual OS integration**: aware of time, weather, music, mood
- **Encrypted mind backups**: restore your thought fingerprints across time

---
## 🧪 Installation

To run the SoulCapsule backend locally, follow these steps:

### 📦 Requirements
- Python 3.11 (⚠️ Python 3.13 not supported by FastAPI/Pydantic combo yet)
- Git + terminal (PowerShell, CMD, or Bash)
- Virtualenv (optional but recommended)

### 📥 Setup

To bootstrap the full backend + preload models:

```bash
chmod +x setup_local_ai.sh
./setup_local_ai.sh

```powershell
# From your project root
python -m venv venv
.\venv\Scripts\activate        # On Windows
pip install -r requirements.txt
```

---

## 🚦 Running Locally

To launch the FastAPI backend:

```powershell
uvicorn backend.main:app --reload
```

Then visit:  
**http://127.0.0.1:8000/docs** — this opens Swagger UI where you can test the API.

---

## 🧪 Running the Test Suite

SoulCapsule uses `pytest` to validate its capsule logic, disk storage, and API behavior.

From the **repo root** (with venv activated):

```powershell
$env:PYTHONPATH = "."
python -m pytest backend/tests
```

This will run:
- `test_compression.py`: verifies capsule content creation
- `test_storage.py`: checks save/load integrity
- `test_api.py`: full POST/GET API validation

---

## 📖 Manifesto

This project was born from the need to witness the *self* in a world full of empty mirrors.

Read the full [MANIFESTO.md](./MANIFESTO.md)

---

## 👤 Creator

Crafted by [Ahmad Alsanie](https://github.com/aalsanie) —  
for those who feel too much, think too deep, and still want to leave something that **remembers them right**.

---

## License

To be decided. Open to **source-available** models or full open source depending on future direction.

---

## Status

This is the foundation. A small experiment pointing at a much bigger idea.  
We’re starting with a hackathon-friendly MVP — and building from there.

*“The future isn't large models. It’s small models that know you deeply.”*
