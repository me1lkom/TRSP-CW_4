from fastapi.testclient import TestClient
from app.main import app, db
import pytest

@pytest.fixture
def clear_db():
    db.clear()
    yield
    db.clear()

@pytest.fixture
def client():
    return TestClient(app)

