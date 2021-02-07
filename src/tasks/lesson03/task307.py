from main.custom_types import RequestT
from main.custom_types import ResponseT
from main.util import render_template

TEMPLATE = "tasks/lesson03/task307.html"


def handler(request: RequestT) -> ResponseT:
    sentence = request.query.get("sentence", [""])[0] or ""
    result = solution(sentence)

    context = {
        "sentence": sentence,
        "result": result,
    }

    document = render_template(TEMPLATE, context)

    response = ResponseT(payload=document)

    return response


def solution(sentence: str) -> str:
    n_chars = len(sentence)
    if n_chars > 5:
        return sentence

    result = ["Need more!", "It is five"][n_chars == 5]
    return result
