from typing import Dict
from typing import List
from typing import Union

from pydantic import BaseModel


class Post(BaseModel):
    id: int
    title: str
    content: str
    image: str

    class Config:
        orm_mode = True


class JsonApiResponse(BaseModel):
    data: Union[Dict, List[Dict]]
    ok: bool = True


class PostsJsonApi(JsonApiResponse):
    data: List[Post]


class PostJsonApi(JsonApiResponse):
    data: Post
