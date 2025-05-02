import tempfile
import pytest
import os
import shutil

from fastapi.testclient import TestClient
from backend.main import app
from backend.storage_sqlite import set_db_path, init_db


@pytest.fixture
def test_client():
    # Step 1: Create a temp DB file (NOT a directory)
    fd, tmp_db_path = tempfile.mkstemp(suffix=".db")
    os.close(fd)  # Close the file handle immediately (only need the path)
    set_db_path(tmp_db_path)

    # Step 2: Initialize the DB schema
    init_db()

    # Step 3: Create a fresh "capsules" dir
    capsules_dir = "capsules"
    if os.path.exists(capsules_dir):
        shutil.rmtree(capsules_dir)
    os.makedirs(capsules_dir, exist_ok=True)

    # Step 4: Create the TestClient INSIDE the fixture AFTER DB is ready
    with TestClient(app) as client:
        yield client

    # Cleanup: remove the temp DB file AFTER client is closed
    if os.path.exists(tmp_db_path):
        os.remove(tmp_db_path)


def test_post_and_get_capsule(test_client):
    response = test_client.post("/capsule", json={"raw_input": "Hello, world."})
    assert response.status_code == 200
    capsule = response.json()
    capsule_id = capsule['id']

    get_response = test_client.get(f"/capsule/{capsule_id}")
    assert get_response.status_code == 200
    assert get_response.json()['id'] == capsule_id


def test_filter_capsules(test_client):
    test_client.post("/capsule", json={"raw_input": "The sky feels heavy."})
    test_client.post("/capsule", json={"raw_input": "I feel at peace when I hear rain."})

    response = test_client.get("/capsule")
    assert response.status_code == 200
    assert len(response.json()) == 2

    response = test_client.get("/capsule?limit=1")
    assert response.status_code == 200
    assert len(response.json()) == 1
