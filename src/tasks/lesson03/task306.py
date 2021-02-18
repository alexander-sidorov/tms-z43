from django.http import HttpRequest
from django.http import HttpResponse

from main.util import render_template

TEMPLATE = "tasks/lesson03/task306.html"


def handler(request: HttpRequest) -> HttpResponse:
    age_raw = request.GET.get("age", "")
    age = (
        None
        if (not age_raw or (isinstance(age_raw, str) and not age_raw.isnumeric()))
        else int(age_raw)
    )

    if age is not None:
        legal = solution(age)
        emoji = ["\N{LOLLIPOP}", "\N{BEER MUG}"][legal]
    else:
        emoji = "\N{FACE PALM}\N{ZERO WIDTH JOINER}\N{MALE SIGN}"

    context = {
        "age": age_raw,
        "result": emoji,
    }

    document = render_template(TEMPLATE, context)

    response = HttpResponse(payload=document)

    return response


def solution(age: int) -> bool:
    return age >= 18
