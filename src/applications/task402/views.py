import json
import traceback
from json import JSONDecodeError

from django.http import HttpRequest
from django.http import HttpResponse
from django.http import HttpResponseNotAllowed
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_POST
from django.views.decorators.http import require_safe

from main.util import render_template
from tasks.lesson04.task402 import add_number
from tasks.lesson04.task402 import get_accumulated


@require_safe
def handle_index(request: HttpRequest) -> HttpResponse:
    """
    This view renders the main page for this app.
    """

    number = get_accumulated(request.session)
    context = {"number": number}

    document = render_template(
        "tasks/lesson04/task402.html",
        context,
        engine_type="$",
    )

    response = HttpResponse(document)

    return response


@require_http_methods(("GET", "HEAD", "POST"))
def handle_api(request: HttpRequest) -> HttpResponse:
    """
    This view renders the main page for this app.
    """

    handlers = {
        "GET": handle_api_get,
        "POST": handle_api_post,
    }

    handler = handlers.get(request.method.upper())
    if not handler:
        return HttpResponseNotAllowed(["GET", "POST", "HEAD"])

    return handler(request)


@require_safe
def handle_api_get(request: HttpRequest) -> JsonResponse:
    """
    This view returns the accumulated number
    """

    number = get_accumulated(request.session)

    return _make_api_response(number)


@require_POST
def handle_api_post(request: HttpRequest) -> JsonResponse:
    """
    This view accepts JSON with number
    and add a given number to the accumulator.
    """

    class InvalidNumberError(RuntimeError):
        pass

    try:
        payload = json.loads(request.body)
        number = payload.get("number")
        if number is None:
            raise InvalidNumberError

        add_number(request.session, number)

    except (InvalidNumberError, JSONDecodeError) as err:
        payload = {
            "err": f"cannot process your json: {err}",
            "ok": False,
            "traceback": traceback.format_exc(),
        }

        return JsonResponse(payload, status=422)

    return _make_api_response(number)


def _make_api_response(number: int) -> JsonResponse:
    """
    A helper function to make a well-formed JSON response
    """
    payload = {"ok": True, "number": number}

    response = JsonResponse(payload)

    return response
