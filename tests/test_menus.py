from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_list_menus_ok():
    r = client.get("/menus")
    assert r.status_code == 200
    data = r.json()
    assert "menus" in data and isinstance(data["menus"], list)
    assert any(m["id"] == "m-001" for m in data["menus"])

def test_get_menu_found():
    r = client.get("/menus/m-001")
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == "m-001"
    assert "items" in data

def test_get_menu_not_found():
    r = client.get("/menus/not-exist")
    assert r.status_code == 200
    assert r.json()["error"] == "menu_not_found"
