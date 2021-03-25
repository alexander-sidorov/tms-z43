import pytest
import requests

from tests.functional.utils import build_chrome
from tests.functional.utils import build_firefox


@pytest.yield_fixture(scope="session")
def service_url():
    url = "http://localhost:8000"
    yield url


@pytest.yield_fixture(scope="session")
def browser():
    # _browser = build_chrome()
    _browser = build_firefox()

    yield _browser
    _browser.close()
    _browser.quit()


@pytest.yield_fixture(scope="function")
def http_client():
    with requests.Session() as session:
        yield session
