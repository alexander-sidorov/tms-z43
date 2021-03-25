from selenium.webdriver.common.by import By

from .abstract import PageElement
from .abstract import PageObject


class IndexPage(PageObject):
    nav = PageElement(By.CSS_SELECTOR, "nav")
    nav_content = PageElement(By.ID, "navbarSupportedContent")
    nav_items = PageElement(By.CSS_SELECTOR, "#navbarSupportedContent ul")
    nav_dropdown = PageElement(By.CSS_SELECTOR, "li.dropdown")
    nav_tasks = PageElement(By.CSS_SELECTOR, "li.dropdown ul")
