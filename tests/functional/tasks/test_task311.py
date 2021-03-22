import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.functional.pages import Task311Page
from tests.functional.utils import screenshot_on_failure


@pytest.fixture(scope="session")
def task_url(service_url) -> str:
    result = f"{service_url}/tasks/311/"
    yield result


@pytest.mark.functional
@screenshot_on_failure
def test(browser, request, task_url):
    page = Task311Page(browser, task_url)

    assert page.heading.tag_name == "h1"
    assert page.heading.text == "Задание 3.11"
    assert page.email.tag_name == "input"
    assert not page.email.text
    assert page.submit.tag_name == "button"
    with pytest.raises(NoSuchElementException):
        assert page.result.tag_name

    verify_result(page, task_url, "")
    verify_result(
        page,
        task_url,
        "xxx",
        "malformed email 'xxx': cannot distinguish parts without '@' sign",
    )
    verify_result(
        page,
        task_url,
        "xxx@gmail.com",
        "xxx@gmail.com",
    )


def verify_result(
    page: Task311Page,
    task_url: str,
    email: str,
    result: str = "",
) -> None:
    page.email.clear()
    page.email.send_keys(email)
    page.submit.click()
    WebDriverWait(page.browser, timeout=4).until(
        EC.url_to_be(task_url),
        f"no page reload",
    )

    if not email:
        with pytest.raises(NoSuchElementException):
            assert page.result.tag_name
        return

    assert page.result.tag_name == "span"
    assert page.result.text == result, f"mismatch for: {email!r}"
