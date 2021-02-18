from random import randint

from django.http import HttpRequest
from django.http import HttpResponse

from main.util import render_template

TEMPLATE = "index.html"


def index(_request: HttpRequest) -> HttpResponse:
    context = {"random_number": randint(100000, 999999)}

    document = render_template(TEMPLATE, context)

    response = HttpResponse(document)

    return response
