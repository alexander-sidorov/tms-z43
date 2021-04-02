import os

import pytest
from pydantic import BaseModel


@pytest.yield_fixture(scope="session")
def post_model():
    from applications.blog.models import Post

    yield Post


@pytest.yield_fixture(scope="session")
def user_model():
    from django.contrib.auth import get_user_model

    user = get_user_model()

    yield user


@pytest.yield_fixture(scope="function")
def post_factory(post_model):
    posts = []

    def factory(**kwargs) -> post_model:
        post = post_model(**kwargs)
        posts.append(post)

        post.save()
        return post

    yield factory

    for _post in posts:
        _post.delete()


@pytest.yield_fixture(scope="function")
def user_factory(user_model):
    users = []

    def factory(**kwargs) -> user_model:
        user = user_model(**kwargs)
        users.append(user)

        user.save()
        return user

    yield factory

    for _user in users:
        _user.delete()


@pytest.yield_fixture(scope="session")
def dataset31_model(user_model, post_model):
    class Dataset31(BaseModel):
        author: user_model
        post1: post_model
        post2: post_model
        post3: post_model

        class Config:
            arbitrary_types_allowed = True

    return Dataset31


@pytest.yield_fixture(scope="function")
def dataset31(user_factory, post_factory, dataset31_model):
    """
    Provides the dataset:
    - 1 user as author
    - 3 posts

    Each object has random shared hash assigned to dataset:
    - author:
        - username: user_{hash}
        - password: user_{hash}
    - post N:  N in "acb"
        - author: author
        - content: post_{N}_{hash}_content
        - image: post_{N}_{hash}_image
        - title: post_{N}_{hash}_title
    """

    hash_ = os.urandom(4).hex()

    author = user_factory(username=f"user_{hash_}")
    author.set_password(f"user_{hash_}")
    author.save()

    posts = [
        post_factory(
            author=author,
            content=f"post_{i}_{hash_}_content",
            image=f"post_{i}_{hash_}_image",
            title=f"post_{i}_{hash_}_title",
        )
        for i in "acb"  # XXX: creation order != title order
    ]

    dataset = dataset31_model(
        author=author,
        post1=posts[0],
        post2=posts[1],
        post3=posts[2],
    )

    return dataset
