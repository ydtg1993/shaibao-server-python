from django import forms


class PayForm(forms.Form):
    pay_type = forms.CharField(required=True)
    account_id = forms.CharField(required=True)
    player_name = forms.CharField(required=True)
    pay_money = forms.CharField(required=True)


class PayRecordForm(forms.Form):
    current_page = forms.IntegerField(required=True)
    page_size = forms.IntegerField(required=True)
