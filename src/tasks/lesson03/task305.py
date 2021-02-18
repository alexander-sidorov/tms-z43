from django.http import HttpRequest
from django.http import HttpResponse

from main.util import render_template

TEMPLATE = "tasks/lesson03/task305.html"


def handler(request: HttpRequest) -> HttpResponse:
    sentence = request.GET.get("sentence", "")
    result = solution(sentence)

    context = {
        "sentence": sentence,
        "result": ["отсутствует", "присутствует"][result],
    }

    document = render_template(TEMPLATE, context)

    response = HttpResponse(document)

    return response


def solution(sentence: str) -> bool:
    words = (sentence or "").split(" ")
    result = "code" in words
    return result
