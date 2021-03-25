from selenium.webdriver.common.by import By

from ..abstract import PageElement
from .base import TaskPage


class Task301Page(TaskPage):
    name = PageElement(By.ID, "id_name")
    submit = PageElement(By.ID, "id_submit")
    greeting = PageElement(By.ID, "id_greeting")
