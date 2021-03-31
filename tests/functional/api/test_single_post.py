from starlette.testclient import TestClient

from api import schema
from project.asgi import application

client = TestClient(application)


def test():
    from applications.blog.models import Post

    response = client.get("/api/blog/post/1/")
    assert response.status_code == 404
    payload = response.json()
    assert payload["meta"]["ok"] is False
    errors = payload["errors"]
    assert isinstance(errors, list)
    assert len(errors) == 1

    obj = Post(title="t", content="c", image="i")

    try:
        obj.save()

        response = client.get(f"/api/blog/post/{obj.pk}/")
        assert response.status_code == 200
        payload = response.json()
        assert payload["meta"]["ok"] is True
        data = payload["data"]
        assert isinstance(data, dict)

        post = schema.Post.from_orm(obj)
        assert data == post

    finally:
        obj.delete()
