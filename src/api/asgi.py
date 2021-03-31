from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Path
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from api import schema
from api.consts import JSONAPI_CONTENT_TYPE
from api.errors import BadRequest
from api.util import validate_content_type
from applications.blog.models import Post

app = FastAPI()


@app.middleware("http")
async def jsonapi_request_validation_middleware(request: Request, call_next):
    if request.method.lower() in {"post", "put", "patch"}:
        content_type = request.headers.get("Content-Type")
        try:
            validate_content_type(content_type)
        except BadRequest as err:
            return JsonApiResponse(
                content={"ok": False, "detail": str(err)},
                status_code=status.HTTP_400_BAD_REQUEST,
            )
    return await call_next(request)


class JsonApiResponse(JSONResponse):
    media_type = JSONAPI_CONTENT_TYPE


@app.get("/api/blog/post/", response_class=JsonApiResponse)
def all_posts() -> schema.PostsJsonApi:
    posts = Post.objects.all()

    payload = schema.PostsJsonApi(data=list(posts))

    return payload


@app.get("/api/blog/post/{post_id}/", response_class=JsonApiResponse)
def single_post(post_id: int = Path(...)):
    post = Post.objects.filter(id=post_id).first()
    if not post:
        raise HTTPException(
            detail=f"post with id={post_id} not found",
            status_code=404,
        )

    payload = schema.PostJsonApi(data=post)

    return payload


@app.post(
    "/api/blog/post/",
    response_class=JsonApiResponse,
    response_model_exclude_unset=True,
    status_code=status.HTTP_201_CREATED,
)
def create_new_post(post: schema.Post) -> schema.PostJsonApi:
    obj = Post(
        content=post.content,
        image=post.image,
        title=post.title,
    )
    obj.save()

    payload = schema.PostJsonApi(data=obj)

    return payload
