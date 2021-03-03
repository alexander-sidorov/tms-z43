from random import randint

import pytest

from tasks.lesson04 import task402


@pytest.mark.unit
def test(http_session):
    def verify_get_accumulated(expected=0, *, session_must_be_empty=False):
        if not session_must_be_empty:
            assert (
                "task402" in http_session
            ), f"{task402.add_number} does not save a number in session"
        got = task402.get_accumulated(http_session)
        assert (
            got == expected
        ), f"session contains invalid number: {http_session}"

    verify_get_accumulated(session_must_be_empty=True)
    # double check to be sure get_accumulated adds no keys to session
    verify_get_accumulated(session_must_be_empty=True)

    test_number = randint(1000, 9999)

    task402.add_number(http_session, test_number)
    verify_get_accumulated(test_number)

    task402.add_number(http_session, test_number)
    verify_get_accumulated(test_number * 2)
