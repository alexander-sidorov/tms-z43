import pytest

from tasks.lesson03.task305 import solution


@pytest.mark.unit
def test():
    test_data = {
        " ": False,
        " code ": True,
        " code code ": True,
        " code": True,
        "": False,
        "1code": False,
        "1code1": False,
        "code ": True,
        "code": True,
        "code1": False,
        "y code x": True,
    }

    for test_value, expected_value in test_data.items():
        got_value = solution(test_value)
        assert expected_value == got_value
