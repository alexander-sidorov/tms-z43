from decimal import Decimal

import pytest

from tasks.lesson03.task310 import solution2


@pytest.mark.unit
def test():
    assert solution2(Decimal("1")) == "1 рубль \N{FIRST PLACE MEDAL} &times; 1"
    assert solution2(Decimal("83.88")) == "\n".join(
        (
            "50 рублей \N{BANKNOTE WITH DOLLAR SIGN} &times; 1",
            "20 рублей \N{BANKNOTE WITH DOLLAR SIGN} &times; 1",
            "10 рублей \N{BANKNOTE WITH DOLLAR SIGN} &times; 1",
            "2 рубля \N{FIRST PLACE MEDAL} &times; 1",
            "1 рубль \N{FIRST PLACE MEDAL} &times; 1",
            "50 копеек \N{FIRST PLACE MEDAL} &times; 1",
            "20 копеек \N{FIRST PLACE MEDAL} &times; 1",
            "10 копеек \N{FIRST PLACE MEDAL} &times; 1",
            "5 копеек \N{FIRST PLACE MEDAL} &times; 1",
            "2 копейки \N{FIRST PLACE MEDAL} &times; 1",
            "1 копейка \N{FIRST PLACE MEDAL} &times; 1",
        )
    )
