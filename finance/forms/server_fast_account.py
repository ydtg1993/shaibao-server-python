from django import forms


class FastAccountForm(forms.Form):
    account_name = forms.CharField(required=True)
    account_number = forms.CharField(required=True)
    qr_code = forms.CharField(required=True)


class SearchFastAccountForm(forms.Form):
    current_page = forms.IntegerField(required=True)
    page_size = forms.IntegerField(required=True)


class FastAccountIDForm(forms.Form):
    obj_id = forms.IntegerField(required=True)
