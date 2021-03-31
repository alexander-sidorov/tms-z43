from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Path
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.responses import Response

from api import schema
from api.consts import JSONAPI_CONTENT_TYPE
from api.errors import BadRequest
from api.util import validate_content_type
from applications.blog.models import Post

app = FastAPI(
    docs_url="/api/docs/",
    openapi_url="/api/openapi.json",
)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JsonApiResponse(
        status_code=exc.status_code,
        content=exc.detail,
    )


@app.middleware("http")
async def jsonapi_request_validation_middleware(request: Request, call_next):
    if request.method.lower() in {"post", "put", "patch"}:
        content_type = request.headers.get("Content-Type")
        try:
            validate_content_type(content_type)
        except BadRequest as err:
            return JsonApiResponse(
                content=schema.ErrorsJsonApi(errors=[str(err)]),
                status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            )
    resp: Response = await call_next(request)
    return resp


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
        errors = schema.ErrorsJsonApi(
            errors=[f"post with id={post_id} not found"]
        )
        errors.meta.ok = False

        raise HTTPException(
            detail=errors.dict(),
            status_code=status.HTTP_404_NOT_FOUND,
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
