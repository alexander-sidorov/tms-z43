from django import forms
from django.views.generic import FormView


class Task302Form(forms.Form):
    a = forms.IntegerField(required=False)
    b = forms.IntegerField(required=False)


class IndexView(FormView):
    form_class = Task302Form
    success_url = "/tasks/302/"
    template_name = "task302/index.html"

    def form_valid(self, form):
        a = form.cleaned_data.get("a")
        b = form.cleaned_data.get("b")

        data = {
            "task302a": a,
            "task302b": b,
            "task302result": None,
        }

        if a and b:
            result = f"{a} плюс {b} равно {a + b}"
            data.update(
                {
                    "task302result": result,
                }
            )

        self.request.session.update(data)

        return super().form_valid(form)
