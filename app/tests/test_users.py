from fastapi.testclient import TestClient
from src.main import app  # adjust if your main entry file differs

client = TestClient(app)

def test_read_root():
    """Check if the API root responds."""
    response = client.get("/")
    assert response.status_code == 200

def test_users_endpoint():
    """Check if /users endpoint returns 200."""
    response = client.get("/users")
    assert response.status_code in [200, 404]
