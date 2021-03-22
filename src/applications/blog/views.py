from django.views.generic import TemplateView


class AllPostsView(TemplateView):
    template_name = "blog/all-posts.html"
