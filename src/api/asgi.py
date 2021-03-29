from typing import Dict
from typing import List
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

from applications.blog.models import Post

app = FastAPI()


class ApiPost(BaseModel):
    id: int
    title: str
    content: str
    image: str


class JsonApiResponse(BaseModel):
    data: Union[Dict, List[Dict]]
    ok: bool = True


@app.get("/api/blog/post/")
async def all_posts() -> JsonApiResponse:
    posts = Post.objects.all()

    payload = JsonApiResponse(
        data=posts,
    )

    return payload


@app.get("/api/blog/post/{post_id}/")
async def single_post(post_id: int) -> JsonApiResponse:
    post = Post.objects.get(id=post_id)

    payload = JsonApiResponse(
        data=ApiPost.parse_obj(post)
    )

    return payload
