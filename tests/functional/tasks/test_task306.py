from typing import Union

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.functional.pages import Task306Page
from tests.functional.utils import screenshot_on_failure


@pytest.fixture(scope="session")
def task_url(service_url) -> str:
    result = f"{service_url}/tasks/306/"
    yield result


@pytest.mark.functional
@screenshot_on_failure
def test(browser, request, task_url):
    page = Task306Page(browser, task_url)

    assert page.heading.tag_name == "h1"
    assert page.heading.text == "Задание 3.06"
    assert page.age.tag_name == "input"
    assert not page.age.text
    assert page.submit.tag_name == "button"
    assert page.result.tag_name == "span"

    emoji_facepalm = "\N{FACE PALM}\N{ZERO WIDTH JOINER}\N{MALE SIGN}\N{VARIATION SELECTOR-16}"
    emoji_candy = "\N{LOLLIPOP}"
    emoji_beer = "\N{CLINKING BEER MUGS}"

    verify_result(page, task_url, "", emoji_facepalm)
    verify_result(page, task_url, -1, emoji_facepalm)
    verify_result(page, task_url, 0, emoji_candy)
    verify_result(page, task_url, 17, emoji_candy)
    verify_result(page, task_url, 18, emoji_beer)
    verify_result(page, task_url, 19, emoji_beer)


def verify_result(
    page: Task306Page, task_url: str, age: Union[int, str], result: str
) -> None:
    page.age.clear()
    page.age.send_keys(str(age))
    page.submit.click()
    WebDriverWait(page.browser, timeout=4).until(
        EC.url_to_be(task_url),
        f"no page reload",
    )
    assert page.result.tag_name == "span"
    assert page.result.text == result, f"mismatch for: {age!r}"
