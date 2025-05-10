
import pytest
from backend.ai.emotion import LocalEmotionClassifier

def test_emotion_basic():
    emotioner = LocalEmotionClassifier()
    input_text = "I'm really sad and lonely right now."
    result = emotioner.classify(input_text)
    assert isinstance(result, dict)
    assert "sadness" in [k.lower() for k in result.keys()]
    assert all(isinstance(v, float) for v in result.values())
