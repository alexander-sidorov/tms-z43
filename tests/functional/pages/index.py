from selenium.webdriver.common.by import By

from .abstract import PageElement
from .abstract import PageObject


class IndexPage(PageObject):
    projects = PageElement(By.CSS_SELECTOR, "article section#id_projects ul")
    tasks = PageElement(By.CSS_SELECTOR, "article section#id_tasks ul")
