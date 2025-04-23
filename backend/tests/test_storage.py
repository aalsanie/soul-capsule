from backend.compression import create_capsule
from backend.storage import save_capsule, load_capsule

def test_save_and_load():
    capsule = create_capsule("Test save-load.")
    save_capsule(capsule)
    loaded = load_capsule(capsule.id)
    assert loaded is not None
    assert loaded.id == capsule.id