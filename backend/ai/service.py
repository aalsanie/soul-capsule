from .summarizer import LocalSummarizer
from .emotion import LocalEmotionClassifier

class LocalAIService:
    def __init__(self):
        self._summarizer = LocalSummarizer()
        self._emotion_classifier = LocalEmotionClassifier()

    def summarize(self, text: str) -> str:
        return self._summarizer.summarize(text)

    def detect_emotion(self, text: str) -> dict:
        return self._emotion_classifier.classify(text)
