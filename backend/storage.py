import json
import os
from backend.models import CapsuleResponse
from backend.config import get_capsule_dir

def _get_path(capsule_id: str) -> str:
    return os.path.join(get_capsule_dir(), f"{capsule_id}.json")

# Always make sure directory exists when saving
def save_capsule(capsule: CapsuleResponse):
    os.makedirs(get_capsule_dir(), exist_ok=True)
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
    dir_path = get_capsule_dir()
    if not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
        return []
    for filename in os.listdir(dir_path):
        if filename.endswith(".json"):
            with open(os.path.join(dir_path, filename)) as f:
                data = json.load(f)
                capsules.append(CapsuleResponse(**data))
    return capsules
