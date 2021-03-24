from django import forms
from django.views.generic import FormView


class Task301Form(forms.Form):
    name = forms.CharField(required=False)


class IndexView(FormView):
    form_class = Task301Form
    success_url = "/tasks/301/"
    template_name = "task301/index.html"

    def form_valid(self, form):
        name = form.cleaned_data.get("name")

        data = {
            "task301greeting": None,
            "task301name": name,
        }

        if name:
            data.update(
                {
                    "task301greeting": name or "anonymous",
                }
            )

        self.request.session.update(data)

        return super().form_valid(form)
