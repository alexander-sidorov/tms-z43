from django.forms import CharField
from django.forms import Form
from django.views.generic import FormView

from applications.task307.logic import solution


class Task307Form(Form):
    sentence = CharField(required=False)


class IndexView(FormView):
    form_class = Task307Form
    success_url = "/tasks/307/"
    template_name = "task307/index.html"

    def form_valid(self, form):
        sentence = form.cleaned_data.get("sentence")
        result = solution(sentence)

        self.request.session["task307result"] = result
        self.request.session["task307sentence"] = sentence

        return super().form_valid(form)
