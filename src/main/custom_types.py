from http import HTTPStatus
from typing import Callable
from typing import Dict
from typing import Optional
from typing import Union

from pydantic import Field
from pydantic.main import BaseModel


class ResponseT(BaseModel):
    status: Union[int, HTTPStatus] = HTTPStatus.OK
    content_type: str = "text/html"
    payload: Optional[str] = None

    class Config:
        validate_assignment = True


class RequestT(BaseModel):
    method: str
    path: str
    query: Dict = Field(default_factory=dict)

    class Config:
        allow_mutation = False
        validate_assignment = True


HandlerT = Callable[[RequestT], ResponseT]
