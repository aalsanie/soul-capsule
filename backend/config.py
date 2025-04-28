import os

def get_capsule_dir() -> str:
    """Dynamically fetch the capsule storage directory. for tests to be fully isolated"""
    return os.getenv("CAPSULE_DIR", "capsules")
