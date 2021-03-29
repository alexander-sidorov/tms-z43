from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Path

from api import schema
from applications.blog.models import Post

app = FastAPI()


@app.get("/api/blog/post/")
def all_posts() -> schema.PostsJsonApi:
    posts = Post.objects.all()

    payload = schema.PostsJsonApi(data=list(posts))

    return payload


@app.get("/api/blog/post/{post_id}/")
def single_post(post_id: int = Path(...)):
    post = Post.objects.filter(id=post_id).first()
    if not post:
        raise HTTPException(
            detail=f"post with id={post_id} not found",
            status_code=404,
        )

    payload = schema.PostJsonApi(data=post)

    return payload
