from typing import List

from pydantic import BaseModel
from pydantic import Field


class Post(BaseModel):
    author_id: int = Field(...)
    content: str = Field(...)
    id: int = Field(None)
    image: str = Field(None)
    title: str = Field(...)

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int = Field(None)
    username: str = Field(...)
    password: str = Field(...)

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


class UserJsonApi(_JsonApi):
    data: User


class ErrorsJsonApi(_JsonApi):
    errors: List[str]
