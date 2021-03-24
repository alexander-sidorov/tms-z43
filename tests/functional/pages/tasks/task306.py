from selenium.webdriver.common.by import By

from ..abstract import PageElement
from .base import TaskPage


class Task306Page(TaskPage):
    age = PageElement(By.ID, "id_age")
    result = PageElement(By.ID, "id_result")
    submit = PageElement(By.ID, "id_submit")
