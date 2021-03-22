from django.http import HttpRequest
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from main.util import render_template

TEMPLATE = "tasks/lesson03/task302.html"


@require_http_methods(["GET", "HEAD", "POST"])
def handle_index(request: HttpRequest) -> HttpResponse:
    """
    This view renders the main page for this app.
    """

    a_raw = request.POST.get("a", "")
    b_raw = request.POST.get("b", "")

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
