from django.views.generic import DetailView
from django.views.generic import ListView

from applications.blog.models import Post


class AllPostsView(ListView):
    model = Post
    template_name = "blog/all-posts.html"


class PostView(DetailView):
    model = Post
