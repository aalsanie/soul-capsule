from backend.models import CapsuleResponse

def decompress_capsule(capsule: CapsuleResponse, mode: str) -> str:
    text = capsule.raw_input
    summary = capsule.generated_summary
    emotion = capsule.emotion_vector

    if mode == "poem":
        lines = [f"{summary}", "", "In quiet tones the thought appears,", "A whisper carved through fleeting years."]
        return "\n".join(lines)
    elif mode == "summary":
        return f"- Summary: {summary}\n- Style: {capsule.style}\n- Key emotions: {', '.join(emotion.keys())}"
    elif mode == "reflection":
        return (
            f"I remember when I wrote this: \"{text}\"\n"
            f"It felt {capsule.style}, filled with {', '.join(emotion.keys())}."
        )
    else: return "Unsupported decompression mode."