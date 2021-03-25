from django.urls import path

from . import views

urlpatterns = [
    path("", views.PostListView.as_view()),
    path("new/", views.PostCreateView.as_view()),
    path("p/<int:pk>/", views.PostDetailView.as_view()),
    path("p/<int:pk>/delete/", views.PostDeleteView.as_view()),
    path("p/<int:pk>/update/", views.PostUpdateView.as_view()),
]
