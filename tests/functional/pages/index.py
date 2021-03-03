from selenium.webdriver.common.by import By

from .abstract import PageElement
from .abstract import PageObject


class IndexPage(PageObject):
    links = PageElement(By.CSS_SELECTOR, "article section ul")
