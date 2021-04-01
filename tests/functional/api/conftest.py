import pytest


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

    def factory(**kwargs):
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

    def factory(**kwargs):
        user = user_model(**kwargs)
        users.append(user)

        user.save()
        return user

    yield factory

    for _user in users:
        _user.delete()
