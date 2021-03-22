from django.forms import CharField
from django.forms import Form
from django.views.generic import FormView

from applications.task305.logic import solution


class Task305Form(Form):
    sentence = CharField(required=False)


class IndexView(FormView):
    form_class = Task305Form
    success_url = "/tasks/305/"
    template_name = "task305/index.html"

    def form_valid(self, form):
        sentence = form.cleaned_data.get("sentence")
        result = solution(sentence) if sentence else ""

        self.request.session["task305result"] = result
        self.request.session["task305sentence"] = sentence

        return super().form_valid(form)
