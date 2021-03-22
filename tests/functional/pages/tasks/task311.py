from selenium.webdriver.common.by import By

from ..abstract import PageElement
from ..abstract import PageObject


class Task311Page(PageObject):
    heading = PageElement(By.XPATH, "/html/body/article/h1")

    email = PageElement(By.ID, "id_email")
    submit = PageElement(By.ID, "id_submit")

    result = PageElement(By.ID, "id_result")
