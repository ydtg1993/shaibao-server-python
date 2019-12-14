from django import forms


class CardForm(forms.Form):
    name = forms.CharField(required=True)
    number = forms.CharField(required=True)
    bank_id = forms.CharField(required=True)
    bank_branch = forms.CharField()


