from random import choice

import pytest
from starlette.testclient import TestClient

from api.schema import Post
from project.asgi import application

client = TestClient(application)


@pytest.mark.functional
def test_no_posts_get_all():
    response = client.get("/api/blog/post/")
    assert response.status_code == 200

    payload = response.json()
    assert payload["meta"]["ok"] is True
    assert payload["data"] == []


@pytest.mark.functional
def test_no_posts_get_single():
    response = client.get("/api/blog/post/1/")
    assert response.status_code == 404

    payload = response.json()
    assert payload["meta"]["ok"] is False

    errors = payload["errors"]
    assert isinstance(errors, list)
    assert len(errors) == 1


@pytest.mark.functional
def test_yes_posts_get_all(dataset31):
    expected = [
        Post.from_orm(p)
        for p in (
            dataset31.post3,
            dataset31.post2,
            dataset31.post1,
        )
    ]

    response = client.get("/api/blog/post/")
    assert response.status_code == 200

    payload = response.json()
    assert payload["meta"]["ok"] is True

    data = payload["data"]
    got = [Post.parse_obj(obj) for obj in data]

    assert got == expected


@pytest.mark.functional
def test_yes_posts_get_single(dataset31):
    post = choice([dataset31.post1, dataset31.post2, dataset31.post3])
    expected = Post.from_orm(post)

    response = client.get(f"/api/blog/post/{post.id}/")
    assert response.status_code == 200

    payload = response.json()
    assert payload["meta"]["ok"] is True

    data = payload["data"]
    got = Post.parse_obj(data)

    assert got == expected
