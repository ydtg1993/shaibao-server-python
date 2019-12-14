from django import forms


class MailListForm(forms.Form):
    current_page = forms.IntegerField(required=True)
    page_size = forms.IntegerField(required=True)


class MailIDForm(forms.Form):
    obj_id = forms.CharField(required=True)
