import os
from random import randint

import pytest
from delorean import utcnow
from starlette import status
from starlette.responses import Response
from starlette.testclient import TestClient

from api.schema import Post
from project.asgi import application

client = TestClient(application)


@pytest.mark.functional
def test_put(user_factory, post_model, delete_on_exit):
    h = os.urandom(4).hex()
    atm = utcnow().datetime

    user = user_factory(username=f"user_{h}")
    delete_on_exit(user)

    post_id = randint(1000, 2000)
    obj_url = f"/api/blog/post/{post_id}/"

    expected = Post(
        author_id=user.id,
        content=f"post_content_{h}",
        created_at=atm,
        image=f"post_image_{h}",
        title=f"post_title_{h}",
    )

    response = client.put(
        obj_url,
        data=expected.json(),
        headers={"Content-Type": "application/vnd.api+json"},
    )
    obj = post_model.objects.get(id=post_id)
    delete_on_exit(obj)
    expected.id = obj.id

    assert response.status_code == status.HTTP_201_CREATED
    validate_content_location(response, obj_url)

    got = Post.parse_obj(response.json()["data"])
    assert got == expected

    expected.title = f"{expected.title}_put2"

    response = client.put(
        obj_url,
        data=expected.json(),
        headers={"Content-Type": "application/vnd.api+json"},
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not response.content
    validate_content_location(response, obj_url)

    obj = post_model.objects.get(id=post_id)
    delete_on_exit(obj)


@pytest.mark.functional
def test_patch(user_factory, post_factory, delete_on_exit):
    h = os.urandom(4).hex()
    user1 = user_factory(username=f"user_{h}_1")
    delete_on_exit(user1)

    user2 = user_factory(username=f"user_{h}_2")
    delete_on_exit(user2)

    post = post_factory(
        title=f"post_{h}_title",
        content=f"post_{h}_content",
        image=f"post_{h}_image",
        author=user1,
    )
    expected = Post.from_orm(post)

    obj_url = f"/api/blog/post/{post.id}/"

    patch = Post(
        author_id=user2.id,
        content=f"post_{h}_content_patched",
    ).dict(exclude_unset=True)

    expected = expected.copy(update=patch)

    response = client.patch(
        obj_url,
        json=patch,
        headers={"Content-Type": "application/vnd.api+json"},
    )
    assert response.status_code == status.HTTP_200_OK

    post.refresh_from_db()

    got = Post.parse_obj(response.json()["data"])
    assert got == expected


def validate_content_location(response: Response, obj_url: str):
    cl = response.headers.get("Content-Location")
    assert cl == obj_url
