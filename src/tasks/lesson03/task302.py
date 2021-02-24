from django.http import HttpRequest
from django.http import HttpResponse

from main.util import render_template

TEMPLATE = "tasks/lesson03/task302.html"


def handler(request: HttpRequest) -> HttpResponse:
    a_raw = request.GET.get("a", "")
    b_raw = request.GET.get("b", "")

    a = int(a_raw) if a_raw else 0
    b = int(b_raw) if b_raw else 0

    result = f"{a} плюс {b} равно {a + b}"

    context = {
        "a": a_raw,
        "b": b_raw,
        "result": result,
    }

    document = render_template(TEMPLATE, context)

    response = HttpResponse(document)

    return response
