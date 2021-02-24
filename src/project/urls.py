from django.contrib import admin
from django.urls import path

from project import views
from tasks.lesson01 import task103
from tasks.lesson03 import task301
from tasks.lesson03 import task302
from tasks.lesson03 import task303
from tasks.lesson03 import task304
from tasks.lesson03 import task305
from tasks.lesson03 import task306
from tasks.lesson03 import task307
from tasks.lesson03 import task309
from tasks.lesson03 import task310
from tasks.lesson03 import task311
from tasks.lesson04 import task402

urlpatterns = [
    path("", views.index),
    path("admin/", admin.site.urls),
    path("api/v1/tasks/402/", task402.handler_api),
    path("tasks/103/", task103.handler),
    path("tasks/301/", task301.handler),
    path("tasks/302/", task302.handler),
    path("tasks/303/", task303.handler),
    path("tasks/304/", task304.handler),
    path("tasks/305/", task305.handler),
    path("tasks/306/", task306.handler),
    path("tasks/307/", task307.handler),
    path("tasks/309/", task309.handler),
    path("tasks/310/", task310.handler),
    path("tasks/311/", task311.handler),
    path("tasks/402/", task402.handler),
]
