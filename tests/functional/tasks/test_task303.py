import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.functional.pages import Task303Page
from tests.functional.utils import screenshot_on_failure


@pytest.fixture(scope="session")
def task_url(service_url) -> str:
    result = f"{service_url}/tasks/303/"
    yield result


@pytest.mark.functional
@screenshot_on_failure
def test(browser, request, task_url):
    page = Task303Page(browser, task_url)

    assert page.heading.tag_name == "h1"
    assert page.heading.text == "Задание 3.03"

    assert page.result.tag_name == "span"
    assert page.sentence.tag_name == "input"
    assert page.submit.tag_name == "button"

    word1 = "aaa"
    word2 = "bbb"

    sentence = f"{word1} {word2}"
    sentence_expected = f"!{word2} {word1}!"

    page.sentence.clear()
    page.sentence.send_keys(sentence)

    page.submit.click()

    WebDriverWait(page.browser, timeout=4).until(
        EC.url_to_be(task_url),
        f"no page reload",
    )

    assert page.result.text == sentence_expected
