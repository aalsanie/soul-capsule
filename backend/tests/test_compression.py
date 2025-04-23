from backend.compression import create_capsule

def test_create_capsule():
    raw = "I feel like I'm writing my own map while lost."
    capsule = create_capsule(raw)
    assert capsule.raw_input == raw
    assert 0 < len(capsule.emotion_vector) <= 3
    assert capsule.generated_summary.startswith("I feel")