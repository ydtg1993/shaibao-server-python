from django import forms


class BetForm(forms.Form):
    event = forms.CharField(required=True)
    data = forms.CharField(required=True)
