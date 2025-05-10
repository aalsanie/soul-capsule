
import pytest
from backend.ai.summarizer import LocalSummarizer

def test_summarizer_basic():
    summarizer = LocalSummarizer()
    input_text = "SoulCapsule is a system that compresses human thought into expressive, stylized memory fragments using AI."
    summary = summarizer.summarize(input_text)
    assert isinstance(summary, str)
    assert len(summary.strip()) > 0
