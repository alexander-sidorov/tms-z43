from django.forms import CharField
from django.forms import Form
from django.views.generic import FormView

from applications.task311.logic import solution


class Task311Form(Form):
    email = CharField(
        max_length=2000,
        required=False,
    )


class IndexView(FormView):
    form_class = Task311Form
    success_url = "/tasks/311/"
    template_name = "task311/index.html"

    def form_valid(self, form):
        data = {
            "task311email": None,
            "task311result": None,
        }

        email = form.cleaned_data.get("email", "")
        if email:
            try:
                solution(email)
                result = email
            except ValueError as err:
                result = str(err)

            data.update(
                {
                    "task311email": email,
                    "task311result": result,
                }
            )

        self.request.session.update(data)

        return super().form_valid(form)
