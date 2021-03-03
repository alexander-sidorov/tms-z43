from django.contrib import admin
from django.urls import include
from django.urls import path

from project import views

urlpatterns = [
    path("", views.index),
    path("admin/", admin.site.urls),
    path("tasks/103/", include("applications.task103.urls")),
    path("tasks/301/", include("applications.task301.urls")),
    path("tasks/402/", include("applications.task402.urls")),
]
