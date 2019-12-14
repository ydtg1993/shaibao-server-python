from django import forms


class CheckWithdrawForm(forms.Form):
    obj_id = forms.CharField(required=True)
    remark = forms.CharField(required=True)
    allow = forms.IntegerField(required=True)


class WithdrawSearchForm(forms.Form):
    current_page = forms.IntegerField(required=True)
    page_size = forms.IntegerField(required=True)
