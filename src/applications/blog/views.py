from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView

from applications.blog.models import Post


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostDeleteView(DeleteView):
    model = Post
    success_url = "/b/"
