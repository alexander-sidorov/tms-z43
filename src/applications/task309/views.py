from django.forms import BooleanField
from django.forms import CharField
from django.forms import Form
from django.views.generic import FormView

from applications.task309.logic import CoefficientsT
from applications.task309.logic import solution


class ComplexField(CharField):
    pass


class Task309Form(Form):
    a = ComplexField(required=True)
    b = ComplexField(required=True)
    c = ComplexField(required=True)
    can_into_complex = BooleanField(required=False)


class IndexView(FormView):
    form_class = Task309Form
    success_url = "/tasks/309/"
    template_name = "task309/index.html"

    def form_valid(self, form):
        a, b, c = [form.cleaned_data.get(_cf) for _cf in "abc"]
        can_into_complex = bool(form.cleaned_data.get("can_into_complex"))

        coefficients = CoefficientsT(a=a, b=b, c=c)
        try:
            result = solution(coefficients, can_into_complex)
            reason = None
        except ValueError as err:
            result = None
            reason = str(err)

        self.request.session.update(
            {
                "task309a": a,
                "task309b": b,
                "task309c": c,
                "task309cic": can_into_complex,
                "task309reason": reason,
                "task309result": result,
            }
        )

        return super().form_valid(form)
