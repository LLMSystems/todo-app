from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200


def test_get_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_todo():
    response = client.post("/todos", json={"title": "測試新增"})
    assert response.status_code == 200
    assert response.json()["title"] == "測試新增"


def test_delete_todo():
    response = client.delete("/todos/1")
    assert response.status_code == 200
