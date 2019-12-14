from django import forms


class GroupForm(forms.Form):
    group_id = forms.CharField(required=False)
    group_name = forms.CharField(required=True)
    permissions = forms.CharField(required=False)


class FindGroupForm(forms.Form):
    current_page = forms.CharField(required=True)
    page_size = forms.CharField(required=True)
