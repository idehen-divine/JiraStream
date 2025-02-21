from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app, base_url="http://test/api/v1")