import string
from http import HTTPStatus
from http.cookies import SimpleCookie
from typing import Any
from typing import Callable
from typing import Dict
from typing import Generator
from typing import Optional
from typing import Tuple
from typing import Union
from urllib.parse import parse_qs

from pydantic import Field
from pydantic.main import BaseModel


class ResponseT(BaseModel):
    status: Union[int, HTTPStatus] = HTTPStatus.OK
    content_type: str = "text/html"
    payload: Optional[str] = None
    headers: Dict = Field(default_factory=dict)
    cookies: SimpleCookie = Field(default_factory=SimpleCookie)

    class Config:
        validate_assignment = True

    def headers_items(self) -> Generator[Tuple[str, str], None, None]:
        yield "Content-Type", self.content_type
        yield from self.headers.items()
        for morsel in self.cookies.values():
            yield "Set-Cookie", morsel.OutputString()


class RequestT(BaseModel):
    method: str
    path: str
    query: Dict = Field(default_factory=dict)
    headers: Dict = Field(default_factory=dict)
    cookies: SimpleCookie = Field(default_factory=SimpleCookie)

    class Config:
        allow_mutation = False

    def __init__(self, environ: Dict):
        kwargs = prepare_kwargs(environ)
        super().__init__(**kwargs)


def prepare_kwargs(environ: Dict) -> Dict[str, Any]:
    qs = environ["QUERY_STRING"]
    query = parse_qs(qs)
    headers = prepare_headers(environ)
    cookies = prepare_cookies(headers)

    kwargs = dict(
        cookies=cookies,
        headers=headers,
        method=environ["REQUEST_METHOD"],
        path=environ["PATH_INFO"],
        query=query,
    )

    return kwargs


def prepare_headers(environ: Dict) -> Dict[str, str]:
    headers = {
        reform_header(env_key): value
        for env_key, value in environ.items()
        if env_key.startswith("HTTP_")
    }

    return headers


def prepare_cookies(headers: Dict[str, str]) -> SimpleCookie:
    cookies = SimpleCookie()
    if "Cookie" in headers:
        cookies.load(headers["Cookie"])

    return cookies


def reform_header(header: str) -> str:
    """
    Converts "HTTP_SET_COOKIE" -> "Set-Cookie"
    """

    without_http = header[5:]
    dash_sep = without_http.replace("_", "-")
    capitalized = string.capwords(dash_sep, "-")

    return capitalized


HandlerT = Callable[[RequestT], ResponseT]
