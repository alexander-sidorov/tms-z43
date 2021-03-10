from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from applications.task305.logic import solution


@require_http_methods(["GET", "HEAD", "POST"])
def handle_index(request: HttpRequest) -> HttpResponse:
    """
    This view renders the main page for this app.
    """

    sentence = request.POST.get("sentence", "")
    result = solution(sentence) if sentence else ""

    context = {
        "sentence": sentence,
        "result": result,
    }

    response = render(request, "task305/index.html", context)

    return response
