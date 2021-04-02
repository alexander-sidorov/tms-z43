import os

import pytest
from starlette import status
from starlette.testclient import TestClient

from api.schema import Post
from project.asgi import application

client = TestClient(application)


@pytest.mark.functional
def test_invalid_content_type():
    response = client.post("/api/blog/post/")
    assert response.status_code == status.HTTP_415_UNSUPPORTED_MEDIA_TYPE


@pytest.mark.functional
def test_missing_request_body():
    response = client.post(
        "/api/blog/post/", headers={"Content-Type": "application/vnd.api+json"}
    )
    assert response.status_code == 422


@pytest.mark.functional
def test_success(user_factory, post_model, delete_on_exit):
    h = os.urandom(4).hex()
    user = user_factory(username=f"user_{h}")

    expected = Post(
        author_id=user.id,
        content=f"post_content_{h}",
        image=f"post_image_{h}",
        title=f"post_title_{h}",
    )

    response = client.post(
        "/api/blog/post/",
        json=expected.dict(),
        headers={"Content-Type": "application/vnd.api+json"},
    )
    assert response.status_code == 201

    obj = post_model.objects.get(title=expected.title)
    delete_on_exit(obj)
    expected.id = obj.id

    got = Post.parse_obj(response.json()["data"])

    assert got == expected
