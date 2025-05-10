#!/bin/bash

echo "🔧 Setting up SoulCapsule Local AI Environment..."

# Step 1: Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Step 2: Upgrade pip and install required packages
pip install --upgrade pip
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install transformers

# Step 3: Preload Hugging Face models into local cache
echo "📦 Downloading t5-small (summarizer)..."
python3 -c "
from transformers import pipeline
pipe = pipeline('summarization', model='t5-small')
pipe('This is a dummy text to trigger download.')
"

echo "📦 Downloading emotion-distilroberta (emotion classifier)..."
python3 -c "
from transformers import pipeline
pipe = pipeline('text-classification', model='j-hartmann/emotion-english-distilroberta-base', return_all_scores=True)
pipe('Trigger download by fake inference.')
"

echo "✅ All models downloaded and ready in HuggingFace cache."
echo "🧠 Local AI backend is ready for development."
