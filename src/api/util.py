from typing import Optional

from api.consts import JSONAPI_CONTENT_TYPE
from api.errors import BadRequest


def validate_content_type(content_type: Optional[str]):
    if content_type != JSONAPI_CONTENT_TYPE:
        supported_cts = sorted([JSONAPI_CONTENT_TYPE])
        errmsg = (
            f"Unsupported content type {content_type}."
            f" Supported content types: {supported_cts}."
        )

        raise BadRequest(errmsg)
