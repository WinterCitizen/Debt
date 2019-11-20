from django import forms  # type: ignore


class DebtForm(forms.Form):  # type: ignore
    first_name = forms.CharField(label='First name', max_length=30)
    last_name = forms.CharField(label='Last name', max_length=30)
    debt_amount = forms.IntegerField(label='Debt amount')
