from django.contrib import admin
from django.urls import path

from project import views

urlpatterns = [
    path("", views.index),
    path("admin/", admin.site.urls),
]
