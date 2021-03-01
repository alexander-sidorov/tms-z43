from django.http import HttpRequest
from django.http import HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("hello from django app 402")


def index2(request: HttpRequest) -> HttpResponse:
    return HttpResponse("zzzzzzzzzzz")
