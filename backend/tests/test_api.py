from fastapi.testclient import TestClient
from backend.main import app
import os
import shutil
import time

client = TestClient(app)

def clear_capsules():
    capsules_dir = "capsules"
    if os.path.exists(capsules_dir):
        shutil.rmtree(capsules_dir)
    os.makedirs(capsules_dir, exist_ok=True)

def test_post_and_get_capsule():
    response = client.post("/capsule", json={"raw_input": "Hello, world."})
    assert response.status_code == 200
    capsule = response.json()
    capsule_id = capsule['id']

    get_response = client.get(f"/capsule/{capsule_id}")
    assert get_response.status_code == 200
    assert get_response.json()['id'] == capsule_id

def test_filter_capsules(client):
    client.post("/capsule", json={"raw_input": "The sky feels heavy."})
    client.post("/capsule", json={"raw_input": "I feel at peace when I hear rain."})

    time.sleep(0.2)  # ← Add small delay to ensure filesystem writes finish!

    response = client.get("/capsule")
    assert response.status_code == 200
    assert len(response.json()) == 2

    response = client.get("/capsule?limit=1")
    assert response.status_code == 200
    assert len(response.json()) == 1