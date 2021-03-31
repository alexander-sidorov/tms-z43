from typing import List

from pydantic import BaseModel
from pydantic import Field


class Post(BaseModel):
    id: int = Field(None)
    title: str = Field(...)
    content: str = Field(...)
    image: str = Field(None)

    class Config:
        orm_mode = True


class _Meta(BaseModel):
    ok: bool = Field(default=True)


class _JsonApi(BaseModel):
    meta: _Meta = Field(default_factory=_Meta)


class PostsJsonApi(_JsonApi):
    data: List[Post]


class PostJsonApi(_JsonApi):
    data: Post


class ErrorsJsonApi(_JsonApi):
    errors: List[str]
