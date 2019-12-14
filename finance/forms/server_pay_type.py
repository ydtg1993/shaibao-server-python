from django import forms


class PayTypeForm(forms.Form):
    name = forms.CharField(required=True)


class SearchPayTypeForm(forms.Form):
    current_page = forms.IntegerField(required=True)
    page_size = forms.IntegerField(required=True)


class PayTypeIDForm(forms.Form):
    obj_id = forms.IntegerField(required=True)
