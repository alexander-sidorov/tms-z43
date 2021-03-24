from django import forms
from django.views.generic import FormView

TEMPLATE = "tasks/lesson01/task103.html"


class Task103Form(forms.Form):
    age1 = forms.IntegerField(required=False)
    age2 = forms.IntegerField(required=False)
    age3 = forms.IntegerField(required=False)


class IndexView(FormView):
    form_class = Task103Form
    success_url = "/tasks/103/"
    template_name = "task103/index.html"

    def form_valid(self, form):
        data = {
            "task103age1": None,
            "task103age2": None,
            "task103age3": None,
            "task103ages": None,
            "task103avg": None,
            "task103sum": None,
        }

        ages = (age1, age2, age3) = [
            form.cleaned_data.get(f"age{i}") for i in "123"
        ]

        if all(_a is not None for _a in ages):
            age_sum = sum(ages)
            age_avg = age_sum / len(ages)

            data.update(
                {
                    "task103ages": ages,
                    "task103avg": age_avg,
                    "task103sum": age_sum,
                }
            )

        data.update(
            {
                "task103age1": age1,
                "task103age2": age2,
                "task103age3": age3,
            }
        )

        self.request.session.update(data)

        return super().form_valid(form)
