from random import randint

import pytest
from requests import Response
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.functional.pages import Task402Page
from tests.functional.utils import screenshot_on_failure


@pytest.fixture(scope="session")
def api(service_url) -> str:
    api_endpoint = f"{service_url}/tasks/402/api/"
    yield api_endpoint


@pytest.fixture(scope="session")
def index(service_url) -> str:
    path = f"{service_url}/tasks/402/"
    yield path


@pytest.mark.functional
@screenshot_on_failure
def test_index(browser, request, index):
    page = Task402Page(browser, index)

    assert page.number.tag_name == "input"
    assert page.result.tag_name == "span"
    assert page.submit.tag_name == "button"

    assert page.result.text == "?"
    verify_number_on_page(page, 0)

    test_number = randint(10, 99)

    page.number.clear()
    page.number.send_keys(str(test_number))
    page.submit.click()
    verify_number_on_page(page, test_number)

    page.number.clear()
    page.number.send_keys(str(test_number))
    page.submit.click()
    verify_number_on_page(page, test_number * 2)


def verify_number_on_page(page: Task402Page, expected: int) -> None:
    WebDriverWait(page.browser, 5).until(
        EC.text_to_be_present_in_element(
            (
                By.ID,
                page.result.get_attribute("id"),
            ),
            str(expected),
        ),
    )


@pytest.mark.functional
def test_api(api, http_client):
    verify_number(http_client, api, 0)

    test_number = randint(1000, 9999)

    payload = add_number(http_client, api, test_number)
    number = payload.get("number")
    assert number == test_number
    verify_number(http_client, api, test_number)

    payload = add_number(http_client, api, test_number)
    number = payload.get("number")
    assert number == test_number
    verify_number(http_client, api, test_number * 2)


def verify_number(http_client, api, expected: int) -> None:
    resp: Response = http_client.get(api)
    assert resp.status_code == 200

    payload = resp.json()
    assert isinstance(payload, dict)

    assert payload.get("ok")

    number = payload.get("number")
    assert number == expected


def add_number(http_client, api, number: int) -> dict:
    payload = {"ok": True, "number": number}
    resp: Response = http_client.post(api, json=payload)
    assert resp.status_code == 200

    payload = resp.json()
    assert isinstance(payload, dict)

    assert payload.get("ok")

    return payload
