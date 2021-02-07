from main.custom_types import RequestT
from main.custom_types import ResponseT
from main.util import render_template

TEMPLATE = "tasks/lesson03/task304.html"


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
    result = sentence if len(sentence) % 3 else f"{sentence}!"
    return result
