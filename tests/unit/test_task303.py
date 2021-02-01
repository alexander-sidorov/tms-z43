import pytest

from tasks.lesson03.task303 import solution


@pytest.mark.unit
def test():
    result = solution("aaa bbb")
    assert result == "!bbb aaa!"
