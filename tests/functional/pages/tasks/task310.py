from selenium.webdriver.common.by import By

from ..abstract import PageElement
from ..abstract import PageObject


class Task310Page(PageObject):
    heading = PageElement(By.XPATH, "/html/body/article/h1")

    money = PageElement(By.ID, "id_money")
    submit = PageElement(By.ID, "id_submit")

    result1 = PageElement(By.ID, "id_result1")
    result2 = PageElement(By.ID, "id_result2")
