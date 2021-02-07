from main.custom_types import RequestT
from main.custom_types import ResponseT
from main.util import render_template

TEMPLATE = "tasks/lesson03/task306.html"


def handler(request: RequestT) -> ResponseT:
    age_raw = request.query.get("age", [""])[0]
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

    response = ResponseT(payload=document)

    return response


def solution(age: int) -> bool:
    return age >= 18
