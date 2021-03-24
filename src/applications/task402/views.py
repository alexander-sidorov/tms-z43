import json
import traceback
from json import JSONDecodeError

from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.http import require_safe

from applications.task402.logic import add_number
from applications.task402.logic import get_accumulated


@require_safe
def handle_index(request: HttpRequest) -> HttpResponse:
    """
    This view renders the main page for this app.
    """

    number = get_accumulated(request.session)
    context = {"number": number}

    document = render(
        request,
        "task402/index.html",
        context,
    )

    response = HttpResponse(document)

    return response


class ApiView(View):
    def get(self, *a, **kw):
        number = get_accumulated(self.request.session)

        return self._make_api_response(number)

    def post(self, *a, **kw):
        class InvalidNumberError(RuntimeError):
            pass

        try:
            payload = json.loads(self.request.body)
            number = payload.get("number")
            if number is None:
                raise InvalidNumberError

            add_number(self.request.session, number)

        except (InvalidNumberError, JSONDecodeError) as err:
            payload = {
                "err": f"cannot process your json: {err}",
                "ok": False,
                "traceback": traceback.format_exc(),
            }

            return JsonResponse(payload, status=422)

        return self._make_api_response(number)

    @staticmethod
    def _make_api_response(number: int) -> JsonResponse:
        """
        A helper function to make a well-formed JSON response
        """

        payload = {"ok": True, "number": number}

        response = JsonResponse(payload)

        return response
