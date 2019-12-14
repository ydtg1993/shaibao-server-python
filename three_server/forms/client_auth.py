from django import forms


class ClientLoginForm(forms.Form):
    phone = forms.CharField(required=True, max_length=11, min_length=11)
    password = forms.CharField(required=True, max_length=18, min_length=6)


class ClientRegisteredForm(forms.Form):
    phone = forms.CharField(required=True, max_length=11, min_length=11)
    code = forms.CharField(required=True, max_length=4, min_length=4)
    password = forms.CharField(required=True, max_length=18, min_length=6)
    invite_code = forms.CharField(max_length=18, min_length=6)


class ClientResetPasswordForm(forms.Form):
    phone = forms.CharField(required=True, max_length=11, min_length=11)
    code = forms.CharField(required=True, max_length=4, min_length=4)
    password = forms.CharField(required=True, max_length=18, min_length=6)


class SendCodeForm(forms.Form):
    phone = forms.CharField(required=True, max_length=11, min_length=11)
