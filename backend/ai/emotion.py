
from transformers import pipeline

class LocalEmotionClassifier:
    def __init__(self, model_name='j-hartmann/emotion-english-distilroberta-base'):
        try:
            self.pipe = pipeline("text-classification", model=model_name, return_all_scores=True)
        except Exception as e:
            raise RuntimeError(f"Failed to load emotion classifier '{model_name}': {e}")

    def classify(self, text: str) -> dict:
        if not text.strip():
            return {}
        try:
            raw_scores = self.pipe(text)[0]
            return {item['label']: round(item['score'], 4) for item in raw_scores}
        except Exception as e:
            raise RuntimeError(f"Emotion classification failed: {e}")
