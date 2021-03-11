from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from applications.task306.logic import solution


@require_http_methods(["GET", "HEAD", "POST"])
def handle_index(request: HttpRequest) -> HttpResponse:
    """
    This view renders the main page for this app.
    """

    age_raw = request.POST.get("age", "")
    age = (
        None
        if (
            not age_raw
            or (isinstance(age_raw, str) and not age_raw.isnumeric())
        )
        else int(age_raw)
    )

    if age is not None:
        legal = solution(age)
    else:
        legal = None

    context = {
        "age": age_raw,
        "result": legal,
    }

    response = render(request, "task306/index.html", context)

    return response
