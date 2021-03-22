from typing import NoReturn
from typing import Optional


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
