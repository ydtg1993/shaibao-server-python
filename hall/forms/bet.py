from django import forms


class HallSearchBetForm(forms.Form):
    hall_id = forms.IntegerField(required=True)


class EditBetForm(forms.Form):
    bet_id = forms.IntegerField(required=True)
    odds = forms.DecimalField(required=True)
