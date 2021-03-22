from django.http import HttpRequest
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from main.util import render_template

TEMPLATE = "tasks/lesson03/task301.html"


@require_http_methods(["GET", "HEAD", "POST"])
def handle_index(request: HttpRequest) -> HttpResponse:
    """
    This view renders the main page for this app.
    """

    name = request.POST.get("name", "")

    context = {
        "input_name": name,
        "greeting_name": name or "anonymous",
    }

    document = render_template(TEMPLATE, context, engine_type="$")

    response = HttpResponse(document)

    return response
