from django.urls import path

from . import views

urlpatterns = [
    path("", views.PostListView.as_view()),
    path("p/<int:pk>/", views.PostDetailView.as_view()),
]
