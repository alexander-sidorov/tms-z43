from typing import NoReturn
from typing import Optional

from main.custom_types import RequestT
from main.custom_types import ResponseT
from main.util import render_template

TEMPLATE = "tasks/lesson03/task311.html"


def handler(request: RequestT) -> ResponseT:
    email = request.query.get("email", [""])[0]

    try:
        solution(email)
        result = email
    except ValueError as err:
        result = str(err)

    context = {
        "email": email,
        "result": result,
    }

    document = render_template(TEMPLATE, context)

    response = ResponseT(payload=document)

    return response


def solution(email: str) -> Optional[NoReturn]:
    if "@" not in email:
        errmsg = f"malformed email {email!r}: cannot distinguish parts without '@' sign"
        raise ValueError(errmsg)

    local_part, domain = email.split("@")
    if not local_part:
        errmsg = f"malformed email {email!r}: no local-part provided"
        raise ValueError(errmsg)

    if not domain:
        errmsg = f"malformed email {email!r}: no domain provided"
        raise ValueError(errmsg)

    if domain != "gmail.com":
        errmsg = f"malformed email {email!r}: 'gmail.com' only is supported"
        raise ValueError(errmsg)
