from http import HTTPStatus

from main.custom_types import RequestT
from main.custom_types import ResponseT


def handler(_request: RequestT) -> ResponseT:
    payload = str(1 / 0)

    response = ResponseT(
        payload=payload,
        status=HTTPStatus.INTERNAL_SERVER_ERROR,
    )

    return response
