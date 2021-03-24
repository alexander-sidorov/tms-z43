from selenium.webdriver.common.by import By

from ..abstract import PageElement
from .base import TaskPage


class Task310Page(TaskPage):
    money = PageElement(By.ID, "id_money")
    submit = PageElement(By.ID, "id_submit")

    result1 = PageElement(By.ID, "id_result1")
    result2 = PageElement(By.ID, "id_result2")
