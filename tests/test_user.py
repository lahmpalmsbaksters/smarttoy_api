# tests/test_user.py

from fastapi.testclient import TestClient
from app.main import app
import json
import random
client = TestClient(app)


def test_create_user():
    response = client.post("/users/", content=json.dumps({"id": random.randint(
        3, 9), "username": "testuser", "email": "test@example.com"}))
    print(response.json())  # Print response content for debugging
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"
    assert response.json()["email"] == "test@example.com"


def test_another_user():
    response = client.post("/users/", content=json.dumps({"id": random.randint(
        3, 9), "username": "anotheruser", "email": "another@example.com"}))
    assert response.status_code == 200
    assert response.json()["username"] == "anotheruser"
    assert response.json()["email"] == "another@example.com"
