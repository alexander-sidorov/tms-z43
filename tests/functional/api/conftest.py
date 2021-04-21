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
def delete_on_exit():
    from django.db import models

    ds = {}

    def _cb(model, id=None):
        if isinstance(model, models.Model):
            ds.setdefault(model.__class__, []).append(model.pk)
        else:
            ds.setdefault(model, []).append(id)

    yield _cb

    for model_cls, pks in ds.items():
        model_cls.objects.filter(id__in=sorted(pks)).delete()


@pytest.yield_fixture(scope="function")
def post_factory(post_model, delete_on_exit):
    def factory(**kwargs) -> post_model:
        post = post_model(**kwargs)
        post.save()
        delete_on_exit(post)
        return post

    yield factory


@pytest.yield_fixture(scope="function")
def user_factory(user_model, delete_on_exit):
    def factory(**kwargs) -> user_model:
        user = user_model(**kwargs)
        user.save()
        delete_on_exit(user)
        return user

    yield factory


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


@pytest.yield_fixture(scope="session")
def dataset32_model(user_model, post_model):
    class Dataset32(BaseModel):
        author1: user_model
        author2: user_model
        post1: post_model
        post2: post_model

        class Config:
            arbitrary_types_allowed = True

    return Dataset32


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


@pytest.yield_fixture(scope="function")
def dataset32(user_factory, post_factory, dataset32_model):
    """
    Provides the dataset:
    - 2 users as authors
    - 2 posts, each post authored by each user

    Each object has random shared hash assigned to dataset:
    - author:
        - username: user_{hash}
        - password: user_{hash}
    - post:
        - author: author
        - content: post_{author_N}_{hash}_content
        - image: post_{author_N}_{hash}_image
        - title: post_{author_N}_{hash}_title
    """

    hash_ = os.urandom(4).hex()

    authors = []
    for i in "12":
        username = f"user_{i}_{hash_}"
        author = user_factory(username=username)
        author.set_password(username)
        author.save()
        authors.append(author)

    author1, author2 = authors

    posts = [
        post_factory(
            author=author,
            content=f"post_{i}_{hash_}_content",
            image=f"post_{i}_{hash_}_image",
            title=f"post_{i}_{hash_}_title",
        )
        for i, author in zip("12", authors)
    ]

    dataset = dataset32_model(
        author1=author1,
        author2=author2,
        post1=posts[0],
        post2=posts[1],
    )

    return dataset
