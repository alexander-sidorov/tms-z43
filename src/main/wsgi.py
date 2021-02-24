import sentry_sdk

from framework.util.settings import get_setting
from main.custom_types import RequestT
from main.handlers import get_handler
from main.handlers import handle_500

sentry_sdk.init(get_setting("SENTRY_DSN"), traces_sample_rate=1.0)


def application(environ, start_response):
    request = RequestT(environ)
    handler = get_handler(request)

    try:
        response = handler(request)
    except Exception:
        response = handle_500(request)

    status = f"{response.status.value} {response.status.phrase}"
    headers_list = list(response.headers_items())
    start_response(status, headers_list)

    yield response.payload.encode()
