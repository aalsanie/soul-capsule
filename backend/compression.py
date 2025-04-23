from backend.models import CapsuleResponse
from backend.utils import generate_id, current_timestamp, mock_emotion_vector, mock_style, summarize_text

def create_capsule(raw_input: str) -> CapsuleResponse:
    return CapsuleResponse(
        id=generate_id(),
        raw_input=raw_input,
        emotion_vector=mock_emotion_vector(),
        style=mock_style(raw_input),
        generated_summary=summarize_text(raw_input),
        timestamp=current_timestamp()
    )