from selenium.webdriver.common.by import By

from ..abstract import PageElement
from .base import TaskPage


class Task309Page(TaskPage):
    a = PageElement(By.ID, "id_a")
    b = PageElement(By.ID, "id_b")
    c = PageElement(By.ID, "id_c")
    can_into_complex = PageElement(By.ID, "id_can_into_complex")

    submit = PageElement(By.ID, "id_submit")

    result = PageElement(By.ID, "id_result")
    reason = PageElement(By.ID, "id_reason")
