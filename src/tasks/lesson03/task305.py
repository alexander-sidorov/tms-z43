from main.custom_types import RequestT
from main.custom_types import ResponseT
from main.util import render_template

TEMPLATE = "tasks/lesson03/task305.html"


def handler(request: RequestT) -> ResponseT:
    sentence = request.query.get("sentence", [""])[0] or ""
    result = solution(sentence)

    context = {
        "sentence": sentence,
        "result": ["отсутствует", "присутствует"][result],
    }

    document = render_template(TEMPLATE, context)

    response = ResponseT(payload=document)

    return response


def solution(sentence: str) -> bool:
    words = (sentence or "").split(" ")
    result = "code" in words
    return result
