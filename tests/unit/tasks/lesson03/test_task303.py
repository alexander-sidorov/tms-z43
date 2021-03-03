import pytest

from applications.task303.logic import solution


@pytest.mark.unit
def test_happy_path():
    word1 = "aaa"
    word2 = "bbb"

    input_data = f"{word1} {word2}"
    expected = f"!{word2} {word1}!"

    got = solution(input_data)
    assert expected == got


@pytest.mark.unit
def test_empty_sentence():
    result = solution("")
    assert result == "!!"


@pytest.mark.unit
def test_single_word_sentence():
    result = solution("aaa")
    assert result == "!aaa!"


@pytest.mark.unit
def test_more_words_sentence():
    ok = False

    try:
        solution("aaa bbb ccc")
    except ValueError:
        ok = True
    except Exception:
        pass

    assert ok, "ne ok"
