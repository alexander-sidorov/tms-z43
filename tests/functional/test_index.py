from urllib.parse import urlsplit

import pytest

from tests.functional.pages import IndexPage
from tests.functional.utils import screenshot_on_failure


@pytest.mark.functional
@screenshot_on_failure
def test(browser, request, service_url):
    page = IndexPage(browser, service_url)

    validate_title(page)
    validate_content(page)


def validate_title(page: IndexPage):
    assert page.title == "Home::Z43"


def validate_content(page: IndexPage):
    validate_nav(page)


def validate_nav(page: IndexPage):
    assert page.nav.tag_name == "nav"
    assert page.nav_content.tag_name == "div"
    assert page.nav_items.tag_name == "ul"
    assert page.nav_tasks.tag_name == "ul"

    nav_items = page.nav_items.find_elements_by_xpath("./li/a")
    links = {
        urlsplit(item.get_attribute("href")).path: item.text
        for item in nav_items
    }
    assert "/b/" in links
    assert links["/b/"] == "Blog"

    page.nav_dropdown.click()

    tasks_links = {
        urlsplit(item.get_attribute("href")).path: item.text
        for item in page.nav_tasks.find_elements_by_xpath("./li/a")
    }

    expected_links = {
        "/tasks/103/": "Задача 1.03",
        "/tasks/301/": "Задача 3.01",
        "/tasks/302/": "Задача 3.02",
        "/tasks/303/": "Задача 3.03",
        "/tasks/304/": "Задача 3.04",
        "/tasks/305/": "Задача 3.05",
        "/tasks/306/": "Задача 3.06",
        "/tasks/307/": "Задача 3.07",
        "/tasks/309/": "Задача 3.09",
        "/tasks/310/": "Задача 3.10",
        "/tasks/311/": "Задача 3.11",
        "/tasks/402/": "Задача 4.02",
    }

    assert tasks_links == expected_links
