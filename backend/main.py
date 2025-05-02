from fastapi import FastAPI, HTTPException, Query
from typing import Optional
from backend.models import CapsuleRequest, CapsuleResponse
from backend.compression import create_capsule
from backend.storage import save_capsule, load_capsule, list_capsules
from backend.decompression import decompress_capsule
from backend.storage_sqlite import (
    init_db,
    save_capsule_sqlite,
    load_capsule_sqlite,
    list_capsules_sqlite
)

app = FastAPI(title="SoulCapsule API")

USE_SQLITE = True

@app.on_event("startup")
def on_startup():
    if USE_SQLITE:
        init_db()

@app.post("/capsule", response_model=CapsuleResponse)
def compress_capsule(request: CapsuleRequest):
    capsule = create_capsule(request.raw_input)
    if USE_SQLITE:
        save_capsule_sqlite(capsule)
    else:
        save_capsule(capsule)
    return capsule

@app.get("/capsule/{capsule_id}", response_model=CapsuleResponse)
def get_capsule(capsule_id: str):
    capsule = load_capsule_sqlite(capsule_id) if USE_SQLITE else load_capsule(capsule_id)
    if not capsule:
        raise HTTPException(status_code=404, detail="Capsule not found")
    return capsule

@app.get("/capsule", response_model=list[CapsuleResponse])
def get_all_capsules(
        style: Optional[str] = None,
        emotion: Optional[str] = None,
        limit: Optional[int] = Query(default=None, gt=0)
):
    if USE_SQLITE:
        return list_capsules_sqlite(style, emotion, limit)
    capsules = list_capsules()
    if style:
        capsules = [c for c in capsules if c.style == style]
    if emotion:
        capsules = [c for c in capsules if emotion in c.emotion_vector]
    if limit:
        capsules = capsules[:limit]
    return capsules

@app.get("/capsule/{capsule_id}/decompress")
def decompress_capsule_route(capsule_id: str, mode: str = "full"):
    capsule = load_capsule_sqlite(capsule_id) if USE_SQLITE else load_capsule(capsule_id)
    if capsule is None:
        raise HTTPException(status_code=404, detail="Capsule not found")

    if mode == "full":
        return capsule.dict()  # Return the full capsule as JSON

    return {"mode": mode, "output": "Unsupported decompression mode."}

