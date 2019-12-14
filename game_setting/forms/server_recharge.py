from django import forms


class RechargeForm(forms.Form):
    method = forms.CharField(required=True)
    type = forms.CharField(required=True)
    range = forms.CharField(required=True)
    value = forms.CharField(required=True)
