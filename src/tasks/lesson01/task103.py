from django.http import HttpRequest
from django.http import HttpResponse

from main.util import render_template

TEMPLATE = "tasks/lesson01/task103.html"


def handler(request: HttpRequest) -> HttpResponse:
    ages = (age1, age2, age3) = [
        int(request.GET.get(f"age{i}", 0)) for i in "123"
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

    response = HttpResponse(document)

    return response
