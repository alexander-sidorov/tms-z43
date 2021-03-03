import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.functional.pages import Task304Page
from tests.functional.utils import screenshot_on_failure


@pytest.fixture(scope="session")
def task_url(service_url) -> str:
    result = f"{service_url}/tasks/304/"
    yield result


@pytest.mark.functional
@screenshot_on_failure
def test(browser, request, task_url):
    page = Task304Page(browser, task_url)

    assert page.heading.tag_name == "h1"
    assert page.heading.text == "Задание 3.04"

    assert page.result.tag_name == "span"
    assert page.sentence.tag_name == "input"
    assert page.submit.tag_name == "button"

    verify_result(page, task_url, "a", "a")
    verify_result(page, task_url, "aa", "aa")
    verify_result(page, task_url, "aaa", "aaa!")


def verify_result(
    page: Task304Page, task_url: str, sentence: str, result: str
) -> None:
    page.sentence.clear()
    page.sentence.send_keys(sentence)
    page.submit.click()
    WebDriverWait(page.browser, timeout=4).until(
        EC.url_to_be(task_url),
        f"no page reload",
    )
    assert page.result.text == result
