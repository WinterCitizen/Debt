from django.http import HttpResponseRedirect  # type: ignore
from django.views.generic.edit import FormView  # type: ignore

from debt_site.forms import DebtForm
from debt_site.models import Debt


class DebtView(FormView):  # type: ignore
    template_name = 'debt.html'
    form_class = DebtForm
    success_url = "/"

    def form_valid(self, form: DebtForm) -> HttpResponseRedirect:
        data = form.cleaned_data
        Debt.objects.create(first_name=data["first_name"],
                            last_name=data["last_name"],
                            debt_amount=data["debt_amount"])
        return super().form_valid(form)
