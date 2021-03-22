import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.functional.pages import Task305Page
from tests.functional.utils import screenshot_on_failure


@pytest.fixture(scope="session")
def task_url(service_url) -> str:
    result = f"{service_url}/tasks/305/"
    yield result


@pytest.mark.functional
@screenshot_on_failure
def test(browser, request, task_url):
    page = Task305Page(browser, task_url)

    assert page.heading.tag_name == "h1"
    assert page.heading.text == "Задание 3.05"
    assert page.sentence.tag_name == "input"
    assert not page.sentence.text
    assert page.submit.tag_name == "button"
    with pytest.raises(NoSuchElementException):
        assert page.result.tag_name == "span"

    verify_result(page, task_url, " code ", "есть")
    verify_result(page, task_url, " code", "есть")
    verify_result(page, task_url, "", "нету")
    verify_result(page, task_url, "a code a", "есть")
    verify_result(page, task_url, "a code", "есть")
    verify_result(page, task_url, "a codea", "нету")
    verify_result(page, task_url, "a", "нету")
    verify_result(page, task_url, "acode a", "нету")
    verify_result(page, task_url, "acodea", "нету")
    verify_result(page, task_url, "code ", "есть")
    verify_result(page, task_url, "code a", "есть")
    verify_result(page, task_url, "code", "есть")


def verify_result(
    page: Task305Page, task_url: str, sentence: str, result: str
) -> None:
    page.sentence.clear()
    page.sentence.send_keys(sentence)
    page.submit.click()
    WebDriverWait(page.browser, timeout=4).until(
        EC.url_to_be(task_url),
        f"no page reload",
    )
    assert page.result.tag_name == "span"
    assert page.result.text == result, f"mismatch for: {sentence!r}"
