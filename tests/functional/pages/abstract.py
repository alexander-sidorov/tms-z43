from typing import Union

from selenium.webdriver.android.webdriver import WebDriver as AndroidWD
from selenium.webdriver.blackberry.webdriver import WebDriver as BlackberryWD
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWD
from selenium.webdriver.edge.webdriver import WebDriver as EdgeWD
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWD
from selenium.webdriver.ie.webdriver import WebDriver as IeWD
from selenium.webdriver.opera.webdriver import WebDriver as OperaWD
from selenium.webdriver.phantomjs.webdriver import WebDriver as PhantomJsWD
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWD
from selenium.webdriver.safari.webdriver import WebDriver as SafariWD
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

WebDriverT = Union[
    AndroidWD,
    BlackberryWD,
    ChromeWD,
    EdgeWD,
    FirefoxWD,
    IeWD,
    OperaWD,
    PhantomJsWD,
    RemoteWD,
    SafariWD,
]


class PageObject:
    def __init__(self, browser: WebDriverT, url: str):
        self._browser = browser
        self._url = url
        self._browser.get(f"{self._url}")

    @property
    def browser(self):
        return self._browser

    @property
    def html(self) -> str:
        return self.browser.page_source

    @property
    def title(self) -> str:
        return self.browser.title


class PageElement:
    def __init__(self, by, value):
        self._by = by
        self._value = value

    def __get__(self, page_object: PageObject, page_object_cls: type):
        if not page_object:
            return self

        return page_object.browser.find_element(self._by, self._value)


class PageResource:
    def __init__(self, ref: str):
        self._ref = ref

    def __get__(
        self, page_object: PageObject, page_object_cls: type
    ) -> Union["PageResource", str]:
        if not page_object:
            return self

        browser = page_object.browser

        current_url = browser.current_url
        if current_url[-1] == "/":
            current_url = current_url[:-1]

        assert (
            self._ref in browser.page_source
        ), f"no '{self._ref}' found on page at {current_url}"

        resource_url = f"{current_url}{self._ref}"
        try:
            browser.get(resource_url)
            found = WebDriverWait(browser, 4).until(
                expected_conditions.url_matches(resource_url)
            )
            assert found, f"browser does not open url {resource_url}"
            content = browser.page_source
            return content
        finally:
            browser.get(current_url)
