from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from applications.blog.models import Post


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/b/"


class PostCreateView(LoginRequiredMixin, CreateView):
    fields = ["title", "content", "image"]
    model = Post

    def form_valid(self, form):
        r = super().form_valid(form)
        self.object.author = self.request.user
        self.object.save()
        return r


class PostUpdateView(LoginRequiredMixin, UpdateView):
    fields = ["title", "content", "image"]
    model = Post
