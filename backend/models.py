from pydantic import BaseModel
from datetime import datetime
from typing import Dict

class CapsuleRequest(BaseModel):
    raw_input: str

class CapsuleResponse(BaseModel):
    id: str
    raw_input: str
    emotion_vector: Dict[str, float]
    style: str
    generated_summary: str
    timestamp: datetime