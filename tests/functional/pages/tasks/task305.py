from selenium.webdriver.common.by import By

from ..abstract import PageElement
from ..abstract import PageObject


class Task305Page(PageObject):
    heading = PageElement(By.XPATH, "/html/body/article/h1")

    result = PageElement(By.ID, "id_result")
    sentence = PageElement(By.ID, "id_sentence")
    submit = PageElement(By.ID, "id_submit")
