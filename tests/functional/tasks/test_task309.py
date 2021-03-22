from typing import Optional

import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from applications.task309.logic import AlgebraicNumberT
from tests.functional.pages import Task309Page
from tests.functional.utils import screenshot_on_failure


@pytest.fixture(scope="session")
def task_url(service_url) -> str:
    result = f"{service_url}/tasks/309/"
    yield result


@pytest.mark.functional
@screenshot_on_failure
def test(browser, request, task_url):
    page = Task309Page(browser, task_url)

    assert page.heading.tag_name == "h1"
    assert page.heading.text == "Задание 3.09"

    assert page.a.tag_name == "input"
    assert not page.a.text

    assert page.b.tag_name == "input"
    assert not page.b.text

    assert page.c.tag_name == "input"
    assert not page.c.text

    assert page.can_into_complex.tag_name == "input"
    assert page.can_into_complex.get_attribute("type") == "checkbox"
    assert not page.can_into_complex.is_selected()

    assert page.submit.tag_name == "button"
    with pytest.raises(NoSuchElementException):
        assert page.result.tag_name == "span"
    with pytest.raises(NoSuchElementException):
        assert page.reason.tag_name == "span"


def verify_result(
    page: Task309Page,
    task_url: str,
    a: AlgebraicNumberT,
    b: AlgebraicNumberT,
    c: AlgebraicNumberT,
    can_into_complex: bool = False,
    result: Optional[str] = None,
    reason: Optional[str] = None,
) -> None:
    coefficients_inputs = {
        "a": (a, page.a),
        "b": (b, page.b),
        "c": (c, page.c),
    }
    for _cf, (var, input) in coefficients_inputs.items():
        input.clear()
        input.send_keys(str(var))

    if page.can_into_complex.is_selected() ^ can_into_complex:
        page.can_into_complex.click()

    page.submit.click()

    WebDriverWait(page.browser, timeout=4).until(
        EC.url_to_be(task_url),
        f"no page reload",
    )

    if result:
        assert page.result.tag_name == "span"
        assert (
            page.result.text == result
        ), f"mismatch for: {(a, b, c, can_into_complex)!r}"

    if reason:
        assert page.reason.tag_name == "span"
        assert (
            page.reason.text == reason
        ), f"mismatch for: {(a, b, c, can_into_complex)!r}"
