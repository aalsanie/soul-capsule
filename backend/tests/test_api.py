from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_post_and_get_capsule():
    response = client.post("/capsule", json={"raw_input": "Hello, world."})
    assert response.status_code == 200
    capsule = response.json()
    capsule_id = capsule['id']

    get_response = client.get(f"/capsule/{capsule_id}")
    assert get_response.status_code == 200
    assert get_response.json()['id'] == capsule_id