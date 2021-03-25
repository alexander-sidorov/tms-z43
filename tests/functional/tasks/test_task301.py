import os

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.functional.pages import Task301Page
from tests.functional.utils import screenshot_on_failure


@pytest.fixture(scope="session")
def task_url(service_url) -> str:
    result = f"{service_url}/tasks/301/"
    yield result


@pytest.mark.functional
@screenshot_on_failure
def test(browser, request, task_url):
    page = Task301Page(browser, task_url)

    assert page.heading.tag_name == "h1"
    assert page.heading.text == "Задание 3.01"

    assert page.name.tag_name == "input"
    assert page.submit.tag_name == "button"

    with pytest.raises(NoSuchElementException):
        assert page.greeting

    name = os.urandom(4).hex()

    page.name.clear()
    page.name.send_keys(name)
    page.submit.click()

    WebDriverWait(page.browser, timeout=4).until(
        EC.url_to_be(task_url),
        f"no page reload",
    )

    assert page.greeting.tag_name == "span"
    assert page.greeting.text == name
