from django.http import HttpRequest
from django.http import HttpResponse

from main.util import render_template

TEMPLATE = "tasks/lesson03/task307.html"


def handler(request: HttpRequest) -> HttpResponse:
    sentence = request.GET.get("sentence", "")
    result = solution(sentence)

    context = {
        "sentence": sentence,
        "result": result,
    }

    document = render_template(TEMPLATE, context)

    response = HttpResponse(payload=document)

    return response


def solution(sentence: str) -> str:
    n_chars = len(sentence)
    if n_chars > 5:
        return sentence

    result = ["Need more!", "It is five"][n_chars == 5]
    return result
