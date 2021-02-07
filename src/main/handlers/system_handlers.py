import traceback
from http import HTTPStatus

from main.custom_types import RequestT
from main.custom_types import ResponseT


def handle_404(request: RequestT) -> ResponseT:
    response = ResponseT(
        content_type="text/plain",
        payload=f"OOPS! endpoint {request.path} not found!",
        status=HTTPStatus.NOT_FOUND,
    )

    return response


def handle_500(_request: RequestT) -> ResponseT:
    response = ResponseT(
        content_type="text/plain",
        payload=traceback.format_exc(),
        status=HTTPStatus.INTERNAL_SERVER_ERROR,
    )

    return response
