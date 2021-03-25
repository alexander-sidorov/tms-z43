from django.contrib import admin

from applications.blog.models import Post


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    pass
