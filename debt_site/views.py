from django.forms import BaseForm
from django.http import HttpResponse
from django.views.generic.edit import FormView

from debt_site.forms import DebtForm
from debt_site.repositories import DebtRepository
from debt_site.services import DebtCreationService


class DebtView(FormView):
    template_name = 'debt.html'
    form_class = DebtForm
    success_url = '/'

    service = DebtCreationService(DebtRepository())

    def form_valid(self, form: BaseForm) -> HttpResponse:
        form_data = form.cleaned_data
        self.service.run(
            first_name=form_data['first_name'],
            last_name=form_data['last_name'],
            debt_amount=form_data['debt_amount'],
        )
        return super().form_valid(form)
