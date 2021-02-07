import pytest

from tasks.lesson03.task304 import solution


@pytest.mark.unit
def test():
    test_data = {
        "": "!",
        "1": "1",
        "12": "12",
        "123": "123!",
        "1234": "1234",
        "12345": "12345",
        "123456": "123456!",
    }

    for test_value, expected_value in test_data.items():
        got_value = solution(test_value)
        assert expected_value == got_value
