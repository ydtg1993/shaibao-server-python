from django import forms


class BankAccountForm(forms.Form):
    bank_name = forms.CharField(required=True)
    number = forms.CharField(required=True)
    user_name = forms.CharField(required=True)
    amount_max = forms.CharField(required=True)
    amount_min = forms.IntegerField(required=True)


class SearchBankAccountForm(forms.Form):
    current_page = forms.IntegerField(required=True)
    page_size = forms.IntegerField(required=True)


class BankAccountIDForm(forms.Form):
    obj_id = forms.IntegerField(required=True)
