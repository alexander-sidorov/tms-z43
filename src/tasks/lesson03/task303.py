from main.custom_types import RequestT
from main.custom_types import ResponseT
from main.util import render_template

TEMPLATE = "tasks/lesson03/task303.html"


def handler(request: RequestT) -> ResponseT:
    sentence = request.query.get("sentence", [""])[0] or ""
    result = solution(sentence) if sentence else ""

    context = {
        "sentence": sentence,
        "result": result,
    }

    document = render_template(TEMPLATE, context)

    response = ResponseT(payload=document)

    return response


def solution(sentence: str) -> str:
    """
    Splits a sentence to two words, exchanges them
    and adds "!" to each side of new sentence.
    """

    words = extract_words_from_sentence(sentence)
    if len(words) < 2:
        word = words[0]
        return f"!{word}!"

    if len(words) > 2:
        raise ValueError("function does not support sentences with > 2 words")

    word1, word2 = words
    result = f"!{word2} {word1}!"

    return result


def extract_words_from_sentence(s: str) -> list:
    w = s.split(" ")
    return w


def ask_user_to_input_a_sentence() -> str:
    s = input("введи предложение из двух слов: ")
    return s


if __name__ == "__main__":
    _user_input = ask_user_to_input_a_sentence()
    _result = solution(_user_input)
    print(_result)
