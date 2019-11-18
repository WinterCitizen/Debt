from django import forms

class DebtForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    debt_amount = forms.IntegerField(label='Debt amount')