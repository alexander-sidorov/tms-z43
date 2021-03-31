from typing import Dict
from typing import List
from typing import Union

from pydantic import BaseModel
from pydantic import Field


class Post(BaseModel):
    id: int = Field(None)
    title: str = Field(...)
    content: str = Field(...)
    image: str = Field(None)

    class Config:
        orm_mode = True


class JsonApiResponse(BaseModel):
    data: Union[Dict, List[Dict]]
    ok: bool = True


class PostsJsonApi(JsonApiResponse):
    data: List[Post]


class PostJsonApi(JsonApiResponse):
    data: Post
