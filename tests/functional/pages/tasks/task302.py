from selenium.webdriver.common.by import By

from ..abstract import PageElement
from ..abstract import PageObject


class Task302Page(PageObject):
    heading = PageElement(By.XPATH, "/html/body/article/h1")

    a = PageElement(By.ID, "id_a")
    b = PageElement(By.ID, "id_b")
    submit = PageElement(By.ID, "id_submit")
    result = PageElement(By.ID, "id_result")
