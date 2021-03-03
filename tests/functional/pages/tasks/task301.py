from selenium.webdriver.common.by import By

from ..abstract import PageElement
from ..abstract import PageObject


class Task301Page(PageObject):
    heading = PageElement(By.XPATH, "/html/body/article/h1")

    name = PageElement(By.ID, "id_name")
    submit = PageElement(By.ID, "id_submit")
    greeting = PageElement(By.ID, "id_greeting")
