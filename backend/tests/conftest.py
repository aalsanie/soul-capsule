import shutil
import tempfile
import pytest
from fastapi.testclient import TestClient
from importlib import reload
import backend.main as main_module

@pytest.fixture(scope="function", autouse=True)
def temp_capsule_dir(monkeypatch):
    temp_dir = tempfile.mkdtemp()
    monkeypatch.setenv("CAPSULE_DIR", temp_dir)

    reload(main_module)  # Reload the app after monkeypatching

    yield temp_dir

    shutil.rmtree(temp_dir)

@pytest.fixture
def client():
    return TestClient(main_module.app)
