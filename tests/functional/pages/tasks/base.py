from selenium.webdriver.common.by import By

from ..abstract import PageElement
from ..abstract import PageObject


class TaskPage(PageObject):
    heading = PageElement(By.XPATH, "/html/body/main//h1")
