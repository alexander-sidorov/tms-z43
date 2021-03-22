from django.urls import path

from . import views

urlpatterns = [
    path("", views.handle_index),
    path("api/", views.ApiView.as_view()),
]
