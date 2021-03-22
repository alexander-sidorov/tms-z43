import pytest

from applications.task306.logic import solution


@pytest.mark.unit
def test():
    test_data = {
        -1: False,
        17: False,
        18: True,
        19: True,
        0: False,
    }

    for test_value, expected_value in test_data.items():
        got_value = solution(test_value)
        assert expected_value == got_value
