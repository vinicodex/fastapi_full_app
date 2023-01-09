from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_should_return_hello_world_and_status_code_200():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
