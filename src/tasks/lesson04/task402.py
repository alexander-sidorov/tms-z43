import json
from http import HTTPStatus
from typing import Dict

from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse

from main.util import render_template


def handler(request: HttpRequest) -> HttpResponse:
    number = get_accumulated(request.session)
    context = {"number": number}

    document = render_template("tasks/lesson04/task402.html", context, engine="$")

    response = HttpResponse(document)

    return response


def handler_api(request: HttpRequest) -> JsonResponse:
    if request.method.lower() == "post":
        payload = json.loads(request.body)
        result = payload.get("number")
        if result:
            add_number(request.session, result)
    else:
        result = get_accumulated(request.session)

    payload = {"ok": True, "result": result}

    response = JsonResponse(payload)

    return response


def get_accumulated(session: Dict) -> int:
    result = session.get("task402", 0)

    return result


def add_number(session: Dict, number: int) -> int:
    acc = get_accumulated(session)
    acc += number
    session["task402"] = acc

    return number
