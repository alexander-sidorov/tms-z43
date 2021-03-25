from random import randint

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.functional.pages import Task302Page
from tests.functional.utils import screenshot_on_failure


@pytest.fixture(scope="session")
def task_url(service_url) -> str:
    result = f"{service_url}/tasks/302/"
    yield result


@pytest.mark.functional
@screenshot_on_failure
def test(browser, request, task_url):
    page = Task302Page(browser, task_url)

    assert page.heading.tag_name == "h1"
    assert page.heading.text == "Задание 3.02"

    assert page.a.tag_name == "input"
    assert page.b.tag_name == "input"
    assert page.submit.tag_name == "button"

    with pytest.raises(NoSuchElementException):
        assert page.result

    a = randint(10, 99)
    b = randint(10, 99)

    page.a.clear()
    page.a.send_keys(str(a))

    page.b.clear()
    page.b.send_keys(str(b))

    page.submit.click()

    WebDriverWait(page.browser, timeout=4).until(
        EC.url_to_be(task_url),
        f"no page reload",
    )

    assert page.result.tag_name == "span"
    assert page.result.text == f"{a} плюс {b} равно {a + b}"
