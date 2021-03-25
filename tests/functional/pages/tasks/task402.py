from selenium.webdriver.common.by import By

from ..abstract import PageElement
from .base import TaskPage


class Task402Page(TaskPage):
    number = PageElement(By.ID, "id_number")
    result = PageElement(By.ID, "id_result")
    submit = PageElement(By.ID, "id_submit")
