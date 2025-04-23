import json
import os
from backend.models import CapsuleResponse
from backend.config import CAPSULE_DIR

os.makedirs(CAPSULE_DIR, exist_ok=True)

def _get_path(capsule_id: str) -> str:
    return os.path.join(CAPSULE_DIR, f"{capsule_id}.json")

def save_capsule(capsule: CapsuleResponse):
    with open(_get_path(capsule.id), 'w') as f:
        json.dump(capsule.dict(), f, default=str)

def load_capsule(capsule_id: str) -> CapsuleResponse | None:
    path = _get_path(capsule_id)
    if not os.path.exists(path):
        return None
    with open(path) as f:
        data = json.load(f)
    return CapsuleResponse(**data)

def list_capsules() -> list[CapsuleResponse]:
    capsules = []
    for filename in os.listdir(CAPSULE_DIR):
        if filename.endswith(".json"):
            with open(os.path.join(CAPSULE_DIR, filename)) as f:
                data = json.load(f)
                capsules.append(CapsuleResponse(**data))
    return capsules