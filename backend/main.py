from fastapi import FastAPI, HTTPException
from backend.models import CapsuleRequest, CapsuleResponse
from backend.compression import create_capsule
from backend.storage import save_capsule, load_capsule, list_capsules
from backend.decompression import decompress_capsule

app = FastAPI(title="SoulCapsule API")

@app.post("/capsule", response_model=CapsuleResponse)
def compress_capsule(request: CapsuleRequest):
    capsule = create_capsule(request.raw_input)
    save_capsule(capsule)
    return capsule

@app.get("/capsule/{capsule_id}", response_model=CapsuleResponse)
def get_capsule(capsule_id: str):
    capsule = load_capsule(capsule_id)
    if not capsule:
        raise HTTPException(status_code=404, detail="Capsule not found")
    return capsule

@app.get("/capsule", response_model=list[CapsuleResponse])
def get_all_capsules():
    return list_capsules()

@app.get("/capsule/{capsule_id}/decompress")
def decompress(capsule_id: str, mode: str = "summary"):
    capsule = load_capsule(capsule_id)
    if not capsule:
        raise HTTPException(status_code=404, detail="Capsule not found")
    return {"mode": mode, "output": decompress_capsule(capsule, mode)}