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
    assert page.title == "Z43"


def validate_content(page: IndexPage):
    validate_tasks_content(page)
    validate_projects_content(page)


def validate_tasks_content(page: IndexPage):
    lesson_links_groups = page.tasks.find_elements_by_xpath("./li")
    assert len(lesson_links_groups) == 3

    expected_links = {
        "Урок 1": [
            ("/tasks/103/", "Задача 1.03"),
        ],
        "Урок 3": [
            ("/tasks/301/", "Задача 3.01"),
            ("/tasks/302/", "Задача 3.02"),
            ("/tasks/303/", "Задача 3.03"),
            ("/tasks/304/", "Задача 3.04"),
            ("/tasks/305/", "Задача 3.05"),
            ("/tasks/306/", "Задача 3.06"),
            ("/tasks/307/", "Задача 3.07"),
            ("/tasks/309/", "Задача 3.09"),
            ("/tasks/310/", "Задача 3.10"),
            ("/tasks/311/", "Задача 3.11"),
        ],
        "Урок 4": [
            ("/tasks/402/", "Задача 4.02"),
        ],
    }

    for lesson_links_group in lesson_links_groups:
        heading = lesson_links_group.find_element_by_xpath("./p")
        lesson_links = lesson_links_group.find_elements_by_xpath("./ul/li")

        expected = expected_links.get(heading.text)
        assert expected, heading.text

        assert len(expected) == len(lesson_links)

        got = sorted(
            (
                urlsplit(
                    li.find_element_by_xpath("./a").get_attribute("href")
                ).path,
                li.find_element_by_xpath("./a").text,
            )
            for li in lesson_links
        )

        assert expected == got


def validate_projects_content(page: IndexPage):
    project_links_lis = page.projects.find_elements_by_xpath("./li")
    assert len(project_links_lis) == 1

    expected_links = {
        "/b/": "Блог",
    }

    for li in project_links_lis:
        a = li.find_element_by_xpath("./a")
        href = a.get_attribute("href")
        url = urlsplit(href)

        expected_name = expected_links.get(url.path)
        assert a.text == expected_name, f"mismatch for {url.path}"
