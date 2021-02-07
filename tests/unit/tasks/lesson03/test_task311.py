import pytest

from tasks.lesson03.task311 import solution


@pytest.mark.unit
def test():
    test_data = {
        "": (None, "malformed email '': cannot distinguish parts without '@' sign"),
        "@": (None, "malformed email '@': no local-part provided"),
        "@gmail.com": (None, "malformed email '@gmail.com': no local-part provided"),
        "test@": (None, "malformed email 'test@': no domain provided"),
        "test@example.com": (
            None,
            "malformed email 'test@example.com': 'gmail.com' only is supported",
        ),
        "test@gmail.com": ("test@gmail.com", None),
    }

    for test_value, expected in test_data.items():
        expected_value, expected_exception = expected
        if expected_exception:
            with pytest.raises(ValueError, match=expected_exception):
                solution(test_value)
        else:
            assert solution(test_value) is None
