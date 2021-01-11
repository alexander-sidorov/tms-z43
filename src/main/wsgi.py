import random

import sentry_sdk

from framework.util.settings import get_setting

sentry_sdk.init(get_setting("SENTRY_DSN"), traces_sample_rate=1.0)


def application(environ, start_response):
    if environ["PATH_INFO"] == "/e/":
        division = 1 / 0

    status = "200 OK"

    headers = {
        "Content-type": "text/html",
    }

    random_number = random.randint(-100, 100)

    environ2 = ""

    for key, value in environ.items():
        text = f"<tr><td>{key}</td><td>{value}</td></tr>"
        environ2 = environ2 + text

    payload = (
        "<!DOCTYPE html>"
        "<html>"
        "<head>"
        "<title>Alpha</title>"
        '<meta charset="utf-8">'
        "</head>"
        "<body>"
        f"<h1>Project Alpha: {random_number}</h1>"
        "<hr>"
        "<p>Environ</p>"
        "<table>"
        f"{environ2}"
        "</table>"
        "</body>"
        "</html>"
    )

    start_response(status, list(headers.items()))

    yield from [payload.encode()]
