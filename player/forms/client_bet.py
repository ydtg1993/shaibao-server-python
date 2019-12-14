from django import forms


class ClientBetRecordForm(forms.Form):
    current_page = forms.IntegerField(required=True)
    page_size = forms.IntegerField(required=True)
    types = forms.CharField(required=False)
