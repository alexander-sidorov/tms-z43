from django.http import HttpRequest
from django.http import HttpResponse

from main.util import render_template

TEMPLATE = "tasks/lesson03/task301.html"


def handler(request: HttpRequest) -> HttpResponse:
    name = request.GET.get("name", "")

    context = {
        "input_name": name,
        "greeting_name": name or "anonymous",
    }

    document = render_template(TEMPLATE, context)

    response = HttpResponse(document)

    return response
