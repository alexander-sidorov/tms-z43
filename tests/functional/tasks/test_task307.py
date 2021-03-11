import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.functional.pages import Task307Page
from tests.functional.utils import screenshot_on_failure


@pytest.fixture(scope="session")
def task_url(service_url) -> str:
    result = f"{service_url}/tasks/307/"
    yield result


@pytest.mark.functional
@screenshot_on_failure
def test(browser, request, task_url):
    page = Task307Page(browser, task_url)

    assert page.heading.tag_name == "h1"
    assert page.heading.text == "Задание 3.07"
    assert page.sentence.tag_name == "input"
    assert not page.sentence.text
    assert page.submit.tag_name == "button"
    with pytest.raises(NoSuchElementException):
        assert page.result.tag_name == "span"

    v_lt5 = "Need more!"
    v_eq5 = "It is five"

    verify_result(page, task_url, "", v_lt5)
    verify_result(page, task_url, "a", v_lt5)
    verify_result(page, task_url, "a" * 4, v_lt5)
    verify_result(page, task_url, "a" * 5, v_eq5)
    verify_result(page, task_url, "a" * 6, "a" * 6)


def verify_result(
    page: Task307Page, task_url: str, sentence: str, result: str
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
