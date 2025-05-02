import tempfile
import os
import shutil
import pytest

from fastapi.testclient import TestClient
from backend.main import app
from backend.storage_sqlite import set_db_path, init_db


@pytest.fixture
def test_client():
    fd, tmp_db_path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    set_db_path(tmp_db_path)
    init_db()

    capsules_dir = "capsules"
    if os.path.exists(capsules_dir):
        shutil.rmtree(capsules_dir)
    os.makedirs(capsules_dir, exist_ok=True)

    with TestClient(app) as client:
        yield client

    if os.path.exists(tmp_db_path):
        os.remove(tmp_db_path)


def test_decompress_modes(test_client):
    response = test_client.post("/capsule", json={"raw_input": "The wind feels like home."})
    assert response.status_code == 200
    capsule_id = response.json()["id"]

    decompress_response = test_client.get(f"/capsule/{capsule_id}/decompress?mode=full")
    assert decompress_response.status_code == 200
    print("DEBUG RESPONSE JSON:", decompress_response.json())
    assert decompress_response.json()["raw_input"] == "The wind feels like home."
