from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_list_menus_returns_array_with_fields():
    r = client.get("/menus")
    assert r.status_code == 200
    data = r.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert "id" in data[0] and "name" in data[0]
