import json
import os
from http import HTTPStatus
from pathlib import Path
from typing import Optional

from framework.dirs import DIR_STORAGE
from main.custom_types import RequestT
from main.custom_types import ResponseT
from main.util import render_template


def handler(request: RequestT) -> ResponseT:
    response = ResponseT()

    client_name = get_client(request)
    if not client_name:
        client_name = create_new_client()
        response.cookies["z43sessionid"] = client_name
        response.cookies["z43sessionid"]["path"] = "/"

    result = "invalid input"
    response.status = HTTPStatus.BAD_REQUEST

    client_data = request.query.get("number", [""])[0]
    if client_data.isnumeric():
        number = int(client_data)
        result = add_number(client_name, number)
        response.status = HTTPStatus.OK

    context = {"number": result}

    response.payload = render_template(
        "tasks/lesson04/task402.html", context, engine="$"
    )

    return response


def handler_api(request: RequestT) -> ResponseT:
    response = ResponseT(content_type="application/json")
    payload = {
        "ok": False,
        "result": "0",
    }

    client_name = get_client(request)
    if not client_name:
        client_name = create_new_client()
        response.cookies["z43sessionid"] = client_name

    result = calc_sum(client_name)
    payload["ok"] = True
    payload["result"] = result

    response.payload = json.dumps(payload)
    response.status = HTTPStatus.OK

    return response


def create_new_client() -> str:
    return os.urandom(8).hex()


def get_client_file(client_name: str) -> Path:
    file_path = DIR_STORAGE / f"{client_name}.402.txt"

    return file_path


def calc_sum(client_name: str) -> int:
    data_file = get_client_file(client_name)

    if not data_file.exists():
        return 0

    with data_file.open("r") as src:
        result = sum(int(line.strip()) for line in src.readlines())

    return result


def add_number(client_name: str, number: int) -> int:
    data_file = get_client_file(client_name)

    with data_file.open("a") as dst:
        dst.write(f"{number}\n")

    return number


def get_client(request: RequestT) -> Optional[str]:
    if not request.cookies:
        return None

    morsel = request.cookies.get("z43sessionid")
    if not morsel:
        return None

    return morsel.value or None
