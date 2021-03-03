from selenium.webdriver.common.by import By

from ..abstract import PageElement
from ..abstract import PageObject


class Task402Page(PageObject):
    number = PageElement(By.ID, "id_number")
    result = PageElement(By.ID, "id_result")
    submit = PageElement(By.ID, "id_submit")
