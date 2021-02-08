import os
from pathlib import Path
from typing import Optional

from framework.dirs import DIR_STORAGE
from main.custom_types import RequestT
from main.custom_types import ResponseT


def handler(request: RequestT) -> ResponseT:
    headers = {}
    client_name = get_client(request)
    if not client_name:
        client_name = create_new_client()
        headers["Set-Cookie"] = f"name={client_name}"

    client_data = request.query.get("number")[0]
    result = "invalid input"
    if client_data == "stop":
        result = calc_sum(client_name)
    elif client_data.isnumeric():
        number = int(client_data)
        result = add_number(client_name, number)

    response = ResponseT(
        headers=headers,
        payload=str(result),
    )

    return response


def create_new_client() -> str:
    return os.urandom(8).hex()


def get_client_file(client_name: str) -> Path:
    file_path = DIR_STORAGE / f"{client_name}.402.txt"

    return file_path


def calc_sum(client_name: str) -> int:
    data_file = get_client_file(client_name)

    with data_file.open("r") as src:
        result = sum(int(line.strip()) for line in src.readlines())

    return result


def add_number(client_name: str, number: int) -> int:
    data_file = get_client_file(client_name)

    with data_file.open("a") as dst:
        dst.write(f"{number}\n")

    return number


def get_client(request: RequestT) -> Optional[str]:
    cookies = request.headers.get("Cookie")
    if not cookies:
        return None

    cookie_name, cookie_value = cookies.split("=")
    assert cookie_name == "name"

    return cookie_value or None
