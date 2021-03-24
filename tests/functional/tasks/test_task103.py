import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.functional.pages import Task103Page
from tests.functional.utils import screenshot_on_failure


@pytest.fixture(scope="session")
def task_url(service_url) -> str:
    result = f"{service_url}/tasks/103/"
    yield result


@pytest.mark.functional
@screenshot_on_failure
def test(browser, request, task_url):
    page = Task103Page(browser, task_url)

    assert page.heading.tag_name == "h1"
    assert page.heading.text == "Задание 1.03"

    assert page.age1.tag_name == "input"
    assert page.age2.tag_name == "input"
    assert page.age3.tag_name == "input"

    assert page.submit.tag_name == "button"

    with pytest.raises(NoSuchElementException):
        assert page.result_ages

    with pytest.raises(NoSuchElementException):
        assert page.result_sum

    with pytest.raises(NoSuchElementException):
        assert page.result_avg

    for input in (
        page.age1,
        page.age2,
        page.age3,
    ):
        input.clear()

    page.age1.send_keys("1")
    page.age2.send_keys("10")
    page.age3.send_keys("100")

    page.submit.click()

    WebDriverWait(page.browser, timeout=4).until(
        EC.url_to_be(task_url),
        f"no page reload",
    )

    assert page.result_ages.tag_name == "span"
    assert page.result_ages.text == "[1, 10, 100]"

    assert page.result_sum.tag_name == "span"
    assert page.result_sum.text == "111"

    assert page.result_avg.tag_name == "span"
    assert page.result_avg.text == "37.0"
