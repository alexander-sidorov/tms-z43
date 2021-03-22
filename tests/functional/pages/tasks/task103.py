from selenium.webdriver.common.by import By

from ..abstract import PageElement
from ..abstract import PageObject


class Task103Page(PageObject):
    heading = PageElement(By.XPATH, "/html/body/article/h1")

    age1 = PageElement(By.ID, "id_age1")
    age2 = PageElement(By.ID, "id_age2")
    age3 = PageElement(By.ID, "id_age3")
    submit = PageElement(By.ID, "id_submit")

    result_ages = PageElement(By.ID, "id_result_ages")
    result_sum = PageElement(By.ID, "id_result_sum")
    result_avg = PageElement(By.ID, "id_result_avg")
