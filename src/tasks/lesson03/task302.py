from main.custom_types import RequestT
from main.custom_types import ResponseT
from main.util import render_template

TEMPLATE = "tasks/lesson03/task302.html"


def handler(request: RequestT) -> ResponseT:
    a_raw = request.query.get("a", [""])[0]
    b_raw = request.query.get("b", [""])[0]

    a = int(a_raw) if a_raw else 0
    b = int(b_raw) if b_raw else 0

    result = f"{a} плюс {b} равно {a + b}"

    context = {
        "a": a_raw,
        "b": b_raw,
        "result": result,
    }

    document = render_template(TEMPLATE, context)

    response = ResponseT(payload=document)

    return response
