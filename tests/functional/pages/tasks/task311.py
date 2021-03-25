from selenium.webdriver.common.by import By

from ..abstract import PageElement
from .base import TaskPage


class Task311Page(TaskPage):
    email = PageElement(By.ID, "id_email")
    submit = PageElement(By.ID, "id_submit")

    result = PageElement(By.ID, "id_result")
