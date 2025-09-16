import pytest
from fastapi.testclient import TestClient
from project_name.main import app
from project_name.database import SessionLocal, engine
from project_name.models.base import Base

client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Создать все таблицы
    Base.metadata.create_all(bind=engine)
    yield
    # Удалить все таблицы
    Base.metadata.drop_all(bind=engine)


def test_create_user():
    response = client.post(
        "/api/v1/users/", json={"email": "user1@example.com", "name": "User One"})
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "user1@example.com"
    assert data["name"] == "User One"


def test_read_user():
    # Сначала создаём пользователя
    response = client.post(
        "/api/v1/users/", json={"email": "user2@example.com", "name": "User Two"})
    user_id = response.json()["id"]
    # Получаем пользователя
    response = client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "user2@example.com"
    assert data["name"] == "User Two"


def test_update_user():
    response = client.post(
        "/api/v1/users/", json={"email": "user3@example.com", "name": "User Three"})
    user_id = response.json()["id"]
    response = client.put(
        f"/api/v1/users/{user_id}", json={"name": "User 3 Updated"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "User 3 Updated"


def test_delete_user():
    response = client.post(
        "/api/v1/users/", json={"email": "user4@example.com", "name": "User Four"})
    user_id = response.json()["id"]
    response = client.delete(f"/api/v1/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["ok"] == True
    # Проверяем, что пользователь удалён
    response = client.get(f"/api/v1/users/{user_id}")
    assert response.status_code == 404
