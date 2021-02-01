from typing import Callable
from typing import Tuple
from urllib.parse import parse_qs

import sentry_sdk

from framework.dirs import DIR_SRC
from framework.util.settings import get_setting
from tasks.lesson03 import task303

sentry_sdk.init(get_setting("SENTRY_DSN"), traces_sample_rate=1.0)

ResponseT = Tuple[str, str, str]


def handle_error(method: str, path: str, qs: str) -> ResponseT:
    payload = str(1 / 0)
    return "500 Internal Server Error", "text/plain", payload


def handle_404(method: str, path: str, qs: str) -> ResponseT:
    status = "404 Not Found"
    content_type = "text/plain"
    payload = f"OOPS! endpoint {path} not found!"
    return status, content_type, payload


def handle_task_303(method: str, path: str, qs: str) -> ResponseT:
    status = "200 OK"
    content_type = "text/html"

    qsi = parse_qs(qs)

    template = read_template("task_303.html")

    sentence = qsi.get("sentence")

    if not sentence:
        result = ""
    else:
        sentence = sentence[0]
        result = task303.solution(sentence)

    payload = template.format(text=result)

    return status, content_type, payload


def handle_index(method: str, path: str, qs: str) -> ResponseT:
    status = "200 OK"

    content_type = "text/html"

    template = read_template("index.html")

    payload = template.format(
        random_number=123,
        environ={},
    )

    return status, content_type, payload


HANDLERS = {
    "/": handle_index,
    "/e/": handle_error,
    "/tasks/lesson03/task303/": handle_task_303,
}


def get_handler(path: str) -> Callable:
    handler = HANDLERS.get(path, handle_404)

    return handler


def application(environ, start_response):
    method = environ["REQUEST_METHOD"]
    path = environ["PATH_INFO"]
    query_string = environ["QUERY_STRING"]

    handler = get_handler(path)

    status, content_type, payload = handler(method, path, query_string)

    headers = {
        "Content-type": content_type,
    }

    start_response(status, list(headers.items()))

    yield payload.encode()


def read_template(template_name: str) -> str:
    dir_templates = DIR_SRC / "main" / "templates"
    template = dir_templates / template_name

    assert template.is_file()

    with template.open("r") as fd:
        content = fd.read()

    return content
