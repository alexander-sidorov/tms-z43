from selenium.webdriver.common.by import By

from ..abstract import PageElement
from .base import TaskPage


class Task303Page(TaskPage):
    result = PageElement(By.ID, "id_result")
    sentence = PageElement(By.ID, "id_sentence")
    submit = PageElement(By.ID, "id_submit")
