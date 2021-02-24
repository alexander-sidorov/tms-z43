from django.http import HttpRequest
from django.http import HttpResponse

from main.util import render_template

TEMPLATE = "tasks/lesson03/task304.html"


def handler(request: HttpRequest) -> HttpResponse:
    sentence = request.GET.get("sentence", "")
    result = solution(sentence) if sentence else ""

    context = {
        "sentence": sentence,
        "result": result,
    }

    document = render_template(TEMPLATE, context)

    response = HttpResponse(document)

    return response


def solution(sentence: str) -> str:
    result = sentence if len(sentence) % 3 else f"{sentence}!"
    return result
