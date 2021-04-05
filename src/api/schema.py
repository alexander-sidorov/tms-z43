from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class Post(BaseModel):
    author_id: Optional[int] = Field(None)
    content: Optional[str] = Field(None)
    id: Optional[int] = Field(None)
    image: Optional[str] = Field(None)
    title: Optional[str] = Field(None)

    class Config:
        orm_mode = True


class User(BaseModel):
    id: Optional[int] = Field(None)
    username: str = Field(...)
    password: str = Field(...)

    class Config:
        orm_mode = True


class _Meta(BaseModel):
    details: Optional[str] = Field(None)
    ok: bool = Field(True)


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
