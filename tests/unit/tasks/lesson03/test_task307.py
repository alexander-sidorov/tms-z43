import pytest

from applications.task307.logic import solution


@pytest.mark.unit
def test():
    lt5 = "Need more!"
    eq5 = "It is five"
    char = "x"

    test_data = {
        char * 0: lt5,
        char * 1: lt5,
        char * 4: lt5,
        char * 5: eq5,
        char * 6: char * 6,
        char * 10: char * 10,
    }

    for test_value, expected_value in test_data.items():
        got_value = solution(test_value)
        assert expected_value == got_value
