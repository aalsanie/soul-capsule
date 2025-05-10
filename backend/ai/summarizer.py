
from transformers import pipeline

class LocalSummarizer:
    def __init__(self, model_name='t5-small'):
        try:
            self.pipe = pipeline("summarization", model=model_name)
        except Exception as e:
            raise RuntimeError(f"Failed to load summarizer model '{model_name}': {e}")

    def summarize(self, text: str, max_length=50, min_length=10) -> str:
        if not text.strip():
            return ""
        try:
            result = self.pipe(text, max_length=max_length, min_length=min_length, do_sample=False)
            return result[0]['summary_text']
        except Exception as e:
            raise RuntimeError(f"Summarization failed: {e}")
