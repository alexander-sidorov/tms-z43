from selenium.webdriver.common.by import By

from ..abstract import PageElement
from ..abstract import PageObject


class Task309Page(PageObject):
    heading = PageElement(By.XPATH, "/html/body/article/h1")

    a = PageElement(By.ID, "id_a")
    b = PageElement(By.ID, "id_b")
    c = PageElement(By.ID, "id_c")
    can_into_complex = PageElement(By.ID, "id_can_into_complex")

    submit = PageElement(By.ID, "id_submit")

    result = PageElement(By.ID, "id_result")
    reason = PageElement(By.ID, "id_reason")
