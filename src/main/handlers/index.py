from random import randint

from main.custom_types import RequestT
from main.custom_types import ResponseT
from main.util import render_template

TEMPLATE = "index.html"


def handler(_request: RequestT) -> ResponseT:
    context = {"random_number": randint(100000, 999999)}

    document = render_template(TEMPLATE, context)

    response = ResponseT(payload=document)

    return response
