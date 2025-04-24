from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_decompress_modes():
    response = client.post("/capsule", json={"raw_input": "The wind feels like home."})
    assert response.status_code == 200
    capsule_id = response.json()["id"]

    for mode in ["poem", "summary", "reflection"]:
        r = client.get(f"/capsule/{capsule_id}/decompress?mode={mode}")
        assert r.status_code == 200
        assert r.json()["mode"] == mode
        assert isinstance(r.json()["output"], str)