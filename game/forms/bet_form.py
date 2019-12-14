from django import forms


class BetForm(forms.Form):
    bet_amount = forms.IntegerField(required=True)
    dice_type = forms.CharField(required=True)

