from django import forms


class UserForm(forms.Form):
    user_id = forms.CharField(required=True)
    user_name = forms.CharField(required=True)
    # pid = forms.CharField(required=True)
    password = forms.CharField(required=True)
    role = forms.CharField(required=True)


class UpdateUserPasswordForm(forms.Form):
    password = forms.CharField(required=True)
    new_password = forms.CharField(required=True)


class ShowUserForm(forms.Form):
    roles = forms.CharField(required=False)
    username = forms.CharField(required=False)
    current_page = forms.CharField(required=True)
    page_size = forms.CharField(required=True)
