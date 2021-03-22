from django.forms import DecimalField
from django.forms import Form
from django.views.generic import FormView

from applications.task310.logic import parse_decimal
from applications.task310.logic import solution1
from applications.task310.logic import solution2


class Task310Form(Form):
    money = DecimalField(
        decimal_places=2,
        max_digits=10,
        max_value=9999999,
        min_value=0,
        required=False,
    )


class IndexView(FormView):
    form_class = Task310Form
    success_url = "/tasks/310/"
    template_name = "task310/index.html"

    def form_valid(self, form):
        data = {
            "task310money": None,
            "task310result": None,
        }

        money = form.cleaned_data.get("money", "")
        if money:
            money = parse_decimal(money)

            result1 = solution1(money)
            result2 = solution2(money)

            data.update(
                {
                    "task310money": str(money),
                    "task310result": {
                        "methodic": result1,
                        "additional": result2,
                    },
                }
            )

        self.request.session.update(data)

        return super().form_valid(form)
