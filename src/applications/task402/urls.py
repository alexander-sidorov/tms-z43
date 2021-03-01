from django.urls import path

from .views import index
from .views import index2

urlpatterns = [
    path("", index),
    path("z/", index2),
]
