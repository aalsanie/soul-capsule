from uuid import uuid4
from datetime import datetime
import random

def generate_id() -> str:
    return str(uuid4())

def current_timestamp():
    return datetime.utcnow()

def mock_emotion_vector():
    emotions = ["joy", "sadness", "anger", "peace", "curiosity"]
    return {e: round(random.uniform(0.1, 0.9), 2) for e in emotions[:3]}

def mock_style(text: str) -> str:
    return "fragmented" if len(text) < 100 else "narrative"

def summarize_text(text: str) -> str:
    return text[:50] + "..."