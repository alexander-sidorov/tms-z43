import traceback

from main.custom_types import ResponseT


def handle_404(method: str, path: str, qs: str) -> ResponseT:
    status = "404 Not Found"
    content_type = "text/plain"
    payload = f"OOPS! endpoint {path} not found!"
    return status, content_type, payload


def handle_500(method: str, path: str, qs: str) -> ResponseT:
    status = "500 Internal Server Error"
    content_type = "text/plain"
    payload = traceback.format_exc()
    return status, content_type, payload
