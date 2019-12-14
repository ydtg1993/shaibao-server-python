from django import forms


class EnterHallForm(forms.Form):
    hall_tag = forms.CharField(required=True)
    # player_id = forms.IntegerField(required=True)
