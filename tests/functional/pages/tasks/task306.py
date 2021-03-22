from selenium.webdriver.common.by import By

from ..abstract import PageElement
from ..abstract import PageObject


class Task306Page(PageObject):
    heading = PageElement(By.XPATH, "/html/body/article/h1")

    age = PageElement(By.ID, "id_age")
    result = PageElement(By.ID, "id_result")
    submit = PageElement(By.ID, "id_submit")
