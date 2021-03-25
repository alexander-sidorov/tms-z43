import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.functional.pages import Task310Page
from tests.functional.utils import screenshot_on_failure


@pytest.fixture(scope="session")
def task_url(service_url) -> str:
    result = f"{service_url}/tasks/310/"
    yield result


@pytest.mark.functional
@screenshot_on_failure
def test(browser, request, task_url):
    page = Task310Page(browser, task_url)

    assert page.heading.tag_name == "h1"
    assert page.heading.text == "Задание 3.10"
    assert page.money.tag_name == "input"
    assert not page.money.text
    assert page.submit.tag_name == "button"
    with pytest.raises(NoSuchElementException):
        assert page.result1.tag_name
    with pytest.raises(NoSuchElementException):
        assert page.result2.tag_name

    verify_result(page, task_url, "")
    verify_result(
        page,
        task_url,
        "1",
        "1 рубль",
        "1 рубль \N{FIRST PLACE MEDAL} × 1",
    )
    verify_result(
        page,
        task_url,
        "11",
        "11 рублей",
        (
            "10 рублей \N{BANKNOTE WITH DOLLAR SIGN} × 1\n"
            "1 рубль \N{FIRST PLACE MEDAL} × 1"
        ),
    )


def verify_result(
    page: Task310Page,
    task_url: str,
    money: str,
    result1: str = "",
    result2: str = "",
) -> None:
    page.money.clear()
    if money:
        page.money.send_keys(money)
    page.submit.click()
    WebDriverWait(page.browser, timeout=4).until(
        EC.url_to_be(task_url),
        f"no page reload",
    )

    if not money:
        with pytest.raises(NoSuchElementException):
            assert page.result1.tag_name
        with pytest.raises(NoSuchElementException):
            assert page.result2.tag_name
        return

    assert page.result1.tag_name == "span"
    assert page.result1.text == result1, f"result1 mismatch for: {money!r}"

    assert page.result2.tag_name == "pre"
    assert page.result2.text == result2, f"result2 mismatch for: {money!r}"
