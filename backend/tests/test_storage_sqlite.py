import tempfile
import pytest
import os
import shutil

from fastapi.testclient import TestClient
from backend.main import app
from backend.storage_sqlite import set_db_path, init_db


@pytest.fixture
def test_client():
    # Step 1: Create a temp DB file
    fd, tmp_db_path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    set_db_path(tmp_db_path)

    # Step 2: Initialize the DB schema
    init_db()

    # Step 3: Create fresh "capsules" dir
    capsules_dir = "capsules"
    if os.path.exists(capsules_dir):
        shutil.rmtree(capsules_dir)
    os.makedirs(capsules_dir, exist_ok=True)

    with TestClient(app) as client:
        yield client

    # Cleanup AFTER client closes
    if os.path.exists(tmp_db_path):
        os.remove(tmp_db_path)


def test_sqlite_capsule_lifecycle(test_client):
    response = test_client.post("/capsule", json={"raw_input": "The sky is blue and full of dreams."})
    assert response.status_code == 200
    capsule_id = response.json()["id"]

    get_response = test_client.get(f"/capsule/{capsule_id}")
    assert get_response.status_code == 200
    assert get_response.json()["raw_input"] == "The sky is blue and full of dreams."


def test_sqlite_filter_style(test_client):
    test_client.post("/capsule", json={"raw_input": "Dreams and dust."})
    test_client.post("/capsule", json={"raw_input": "Clouds and memories."})

    response = test_client.get("/capsule")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
