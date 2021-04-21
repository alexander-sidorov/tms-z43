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
def test_yes_posts_get_all_filtered(dataset32):
    posts1 = [Post.from_orm(dataset32.post1)]
    posts2 = [Post.from_orm(dataset32.post2)]

    url0 = f"/api/blog/post/"
    url1 = f"/api/blog/post/?author_id={dataset32.author1.id}"
    url2 = f"/api/blog/post/?author_id={dataset32.author2.id}"

    def validate_posts(url, posts):
        response = client.get(url)
        assert response.status_code == 200

        payload = response.json()
        assert payload["meta"]["ok"] is True

        data = payload["data"]
        got = [Post.parse_obj(obj) for obj in data]

        assert got == posts

    validate_posts(url1, posts1)
    validate_posts(url2, posts2)

    all_posts = sorted(
        posts1 + posts2,
        key=lambda post: post.created_at,
        reverse=True,
    )
    validate_posts(url0, all_posts)


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
