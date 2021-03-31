from starlette.testclient import TestClient

from project.asgi import application

client = TestClient(application)


def test():
    response = client.get("/api/blog/post/")
    assert response.status_code == 200
    payload = response.json()
    assert payload["meta"]["ok"] is True
    assert payload["data"] == []
