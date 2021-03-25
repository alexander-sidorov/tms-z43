from selenium.webdriver.common.by import By

from ..abstract import PageElement
from .base import TaskPage


class Task302Page(TaskPage):
    a = PageElement(By.ID, "id_a")
    b = PageElement(By.ID, "id_b")
    submit = PageElement(By.ID, "id_submit")
    result = PageElement(By.ID, "id_result")
