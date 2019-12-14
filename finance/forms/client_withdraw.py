from django import forms


class WithdrawForm(forms.Form):
    value = forms.CharField(required=True)


class WithdrawSearchForm(forms.Form):
    current_page = forms.IntegerField(required=True)
    page_size = forms.IntegerField(required=True)
