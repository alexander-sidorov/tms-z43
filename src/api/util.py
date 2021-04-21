from typing import Optional
from typing import Type

from fastapi import HTTPException
from starlette import status

from api import schema
from api.consts import JSONAPI_CONTENT_TYPE
from api.errors import BadRequest


def validate_content_type(content_type: Optional[str]):
    if content_type != JSONAPI_CONTENT_TYPE:
        supported_cts = sorted([JSONAPI_CONTENT_TYPE])
        errmsg = (
            f"Unsupported content type {content_type}."
            f" Supported content types: {supported_cts}."
        )

        raise BadRequest(errmsg)


def get_or_404(model: Type, pk: int):
    if pk:
        obj = model.objects.filter(pk=pk).first()
        if obj:
            return obj

    errors = schema.ErrorsJsonApi(
        errors=[f"object of {model.__name__} with pk={pk} not found"]
    )
    errors.meta.ok = False

    raise HTTPException(
        detail=errors.dict(),
        status_code=status.HTTP_404_NOT_FOUND,
    )


def update_normal_fields(orm_obj, schema_obj, *, exclude_unset=False) -> None:
    kw = schema_obj.dict(exclude_unset=exclude_unset)

    for fn in {"id"}:
        if fn in kw:
            del kw[fn]

    for name, value in kw.items():
        setattr(orm_obj, name, value)

    orm_obj.save()
