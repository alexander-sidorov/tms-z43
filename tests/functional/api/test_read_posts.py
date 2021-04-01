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
def test_single_post_get_all(post_factory, user_factory):
    author = user_factory(username="test_single_post_get_all")
    post = post_factory(
        author=author,
        content="c",
        image="i",
        title="test_single_post_get_all",
    )
    expected = [Post.from_orm(post)]

    response = client.get("/api/blog/post/")
    assert response.status_code == 200

    payload = response.json()
    assert payload["meta"]["ok"] is True

    data = payload["data"]
    got = [Post.parse_obj(obj) for obj in data]

    assert got == expected


@pytest.mark.functional
def test_single_post_get_single(user_factory, post_factory):
    author = user_factory(username="test_single_post_get_single")
    post = post_factory(
        author=author,
        content="c",
        image="i",
        title="test_single_post_get_single",
    )
    expected = Post.from_orm(post)

    response = client.get(f"/api/blog/post/{post.id}/")
    assert response.status_code == 200

    payload = response.json()
    assert payload["meta"]["ok"] is True

    data = payload["data"]
    got = Post.parse_obj(data)

    assert got == expected


@pytest.mark.functional
def test_multiple_posts_get_all(user_factory, post_factory):
    author = user_factory(username="test_multiple_posts_get_all")
    p1 = post_factory(
        author=author,
        content="c",
        image="i",
        title="p1__test_multiple_posts_get_all",
    )
    p3 = post_factory(
        author=author,
        content="c",
        image="i",
        title="p3__test_multiple_posts_get_all",
    )
    p2 = post_factory(
        author=author,
        content="c",
        image="i",
        title="p2__test_multiple_posts_get_all",
    )

    response = client.get("/api/blog/post/")
    assert response.status_code == 200

    payload = response.json()
    assert payload["meta"]["ok"] is True

    data = payload["data"]
    posts = [Post.from_orm(p) for p in (p1, p2, p3)]

    assert posts == data


@pytest.mark.functional
def test_multiple_posts_get_single(user_factory, post_factory):
    author = user_factory(username="test_multiple_posts_get_single")
    posts = [
        post_factory(
            title=f"p{i}__test_multiple_posts_get_single",
            author=author,
        )
        for i in "123"
    ]
    post = choice(posts)
    expected = Post.from_orm(post)

    response = client.get(f"/api/blog/post/{post.id}/")
    assert response.status_code == 200

    payload = response.json()
    assert payload["meta"]["ok"] is True

    data = payload["data"]
    got = Post.parse_obj(data)

    assert got == expected
