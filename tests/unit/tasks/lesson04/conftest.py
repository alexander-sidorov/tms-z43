import pytest


@pytest.yield_fixture
def http_session():
    session = {}

    yield session
