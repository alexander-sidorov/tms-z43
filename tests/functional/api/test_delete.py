import os

import pytest
from starlette import status
from starlette.testclient import TestClient

from project.asgi import application

client = TestClient(application)


@pytest.mark.functional
def test_delete(post_model, post_factory, delete_on_exit):
    h = os.urandom(4).hex()
    post = post_factory(title=f"post_{h}_title")
    delete_on_exit(post)

    response = client.delete(
        f"/api/blog/post/{post.id}/",
        headers={"Content-Type": "application/vnd.api+json"},
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not response.content

    post = post_model.objects.filter(id=post.id).first()
    assert post is None
