from decimal import Decimal

import pytest

from tasks.lesson03.task310 import solution1


@pytest.mark.unit
def test():
    test_data = {
        "0": "\N{EMPTY SET}",
        "0.0": "\N{EMPTY SET}",
        "0.001": "\N{EMPTY SET}",
        "0.01": "1 копейка",
        "0.1": "10 копеек",
        "0.02": "2 копейки",
        "0.04": "4 копейки",
        "0.05": "5 копеек",
        "0.009": "\N{EMPTY SET}",
        "0.09": "9 копеек",
        "0.10": "10 копеек",
        "0.11": "11 копеек",
        "0.19": "19 копеек",
        "0.20": "20 копеек",
        "0.21": "21 копейка",
        "0.99": "99 копеек",
        "1": "1 рубль",
        "2": "2 рубля",
        "4": "4 рубля",
        "5": "5 рублей",
        "9": "9 рублей",
        "10": "10 рублей",
        "11": "11 рублей",
        "19": "19 рублей",
        "20": "20 рублей",
        "21": "21 рубль",
        "22": "22 рубля",
        "24": "24 рубля",
        "25": "25 рублей",
        "2.04": "2 рубля, 4 копейки",
    }

    for test_value, expected_value in test_data.items():
        number = Decimal(test_value)
        got_value = solution1(number)
        assert expected_value == got_value, f"failed on {number}"
