from http import HTTPStatus
from typing import Any
from typing import Callable
from typing import Dict
from typing import Optional
from typing import Union
from urllib.parse import parse_qs

from pydantic import Field
from pydantic.main import BaseModel


class ResponseT(BaseModel):
    status: Union[int, HTTPStatus] = HTTPStatus.OK
    content_type: str = "text/html"
    payload: Optional[str] = None
    headers: Dict = Field(default_factory=dict)

    class Config:
        validate_assignment = True


class RequestT(BaseModel):
    method: str
    path: str
    query: Dict = Field(default_factory=dict)
    headers: Dict = Field(default_factory=dict)

    class Config:
        allow_mutation = False

    def __init__(self, environ: Dict):
        kwargs = self.prepare_kwargs(environ)

        super().__init__(**kwargs)

    @classmethod
    def prepare_kwargs(cls, environ: Dict) -> Dict[str, Any]:
        qs = environ["QUERY_STRING"]
        query = parse_qs(qs)
        headers = cls.prepare_headers(environ)

        kwargs = dict(
            headers=headers,
            method=environ["REQUEST_METHOD"],
            path=environ["PATH_INFO"],
            query=query,
        )

        return kwargs

    @staticmethod
    def prepare_headers(environ: Dict) -> Dict[str, str]:
        def reform_header(header: str) -> str:
            without_http = header[5:]
            words = without_http.split("_")
            capitalized_words = (word.capitalize() for word in words)
            reformed = "-".join(capitalized_words)

            return reformed

        headers = {
            reform_header(env_key): value
            for env_key, value in environ.items()
            if env_key.startswith("HTTP_")
        }

        return headers


HandlerT = Callable[[RequestT], ResponseT]
