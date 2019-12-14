from django import forms


class HallSearchChipForm(forms.Form):
    hall_id = forms.IntegerField(required=True)


class EditChipForm(forms.Form):
    chip_id = forms.IntegerField(required=True)
    value = forms.IntegerField(required=True)
