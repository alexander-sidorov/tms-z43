from django.http import HttpRequest
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from main.util import render_template

TEMPLATE = "tasks/lesson01/task103.html"


@require_http_methods(["GET", "HEAD", "POST"])
def handle_index(request: HttpRequest) -> HttpResponse:
    """
    This view renders the main page for this app.
    """

    ages = (age1, age2, age3) = [
        int(request.POST.get(f"age{i}", 0)) for i in "123"
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
