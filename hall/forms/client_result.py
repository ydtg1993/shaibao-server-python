from django import forms


class LotteryRecordForms(forms.Form):
    hall_tag = forms.CharField(required=True)
