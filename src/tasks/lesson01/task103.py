from main.custom_types import RequestT
from main.custom_types import ResponseT
from main.util import render_template

TEMPLATE = "tasks/lesson01/task103.html"


def handler(request: RequestT) -> ResponseT:
    ages = (age1, age2, age3) = [
        int(request.query.get(f"age{i}", [0])[0]) for i in "123"
    ]
    age_sum = sum(ages)
    age_avg = age_sum / len(ages)

    context = {
        "age1": age1,
        "age2": age2,
        "age3": age3,
        "age_avg": age_avg,
        "age_sum": age_sum,
        "ages": ages,
    }

    document = render_template(TEMPLATE, context)

    response = ResponseT(payload=document)

    return response
