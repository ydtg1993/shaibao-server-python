from django import forms


class ServerAddBankForm(forms.Form):
    name = forms.CharField(required=True)


class ServerSearchBankForm(forms.Form):
    current_page = forms.IntegerField(required=True)
    page_size = forms.IntegerField(required=True)


class ServerBankIdForm(forms.Form):
    obj_id = forms.IntegerField(required=True)
