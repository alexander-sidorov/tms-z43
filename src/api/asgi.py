from django.contrib.auth import authenticate
from fastapi import Body
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Path
from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.responses import Response

from api import schema
from api.consts import JSONAPI_CONTENT_TYPE
from api.errors import BadRequest
from api.util import get_or_404
from api.util import update_normal_fields
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
                content="xxx",  # schema.ErrorsJsonApi(errors=[str(err)]),
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
    post = get_or_404(Post, pk=post_id)

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
        author_id=post.author_id,
        content=post.content,
        image=post.image,
        title=post.title,
    )

    obj.save()

    payload = schema.PostJsonApi(data=obj)

    return payload


@app.put(
    "/api/blog/post/{post_id}/",
)
def replace_post(
    request: Request,
    post: schema.Post = Body(...),
    post_id: int = Path(...),
) -> JsonApiResponse:
    obj, is_new_obj = Post.objects.update_or_create(id=post_id)
    update_normal_fields(obj, post)

    if is_new_obj:
        payload = schema.PostJsonApi(data=obj)
        payload.meta.details = "object has been created"
        response = JsonApiResponse(
            content=jsonable_encoder(schema.PostJsonApi(data=obj)),
            status_code=status.HTTP_201_CREATED,
        )
    else:
        response = Response(status_code=status.HTTP_204_NO_CONTENT)

    response.headers["Content-Location"] = request.url.path

    return response


@app.patch(
    "/api/blog/post/{post_id}/",
    response_model_exclude_unset=True,
)
def update_post(
    post: schema.Post = Body(...),
    post_id: int = Path(...),
) -> schema.PostJsonApi:
    obj = get_or_404(Post, pk=post_id)
    update_normal_fields(obj, post, exclude_unset=True)

    payload = schema.PostJsonApi(data=obj)
    payload.meta.details = "object has been partially updated"

    return payload


@app.delete(
    "/api/blog/post/{post_id}/",
)
def delete_post(post_id: int = Path(...)):
    Post.objects.filter(id=post_id).delete()

    response = Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )

    return response


@app.post("/api/user/", response_class=JsonApiResponse)
def auth_user(user: schema.User) -> schema.UserJsonApi:
    obj = authenticate(
        username=user.username,
        password=user.password,
    )

    payload = schema.UserJsonApi(data=obj)
    payload.data.password = "*****"

    return payload
