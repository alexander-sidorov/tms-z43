import sentry_sdk

from framework.util.settings import get_setting
from main.handlers import get_handler
from main.handlers import handle_500
from main.util import build_request

sentry_sdk.init(get_setting("SENTRY_DSN"), traces_sample_rate=1.0)


def application(environ, start_response):
    request = build_request(environ)
    handler = get_handler(request)

    try:
        response = handler(request)
    except Exception:
        response = handle_500(request)

    headers = {
        "Content-Type": response.content_type,
    }

    start_response(
        f"{response.status.value} {response.status.phrase}",
        list(headers.items()),
    )

    yield response.payload.encode()
