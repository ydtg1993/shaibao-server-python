from django import forms


class HallCreateForm(forms.Form):
    name = forms.CharField(required=True)
    game_date = forms.CharField(required=True)
    total = forms.CharField(required=True)
    hall_tag = forms.CharField(required=True)
    lottery_type = forms.CharField(required=True)


class HallEditForm(forms.Form):
    hall_id = forms.CharField(required=True)
    name = forms.CharField(required=True)
    game_date = forms.CharField(required=True)
    total = forms.CharField(required=True)


class HallSearchForm(forms.Form):
    current_page = forms.IntegerField(required=True)
    page_size = forms.IntegerField(required=True)


class SwitchForm(forms.Form):
    obj_id = forms.IntegerField(required=True)


class StartHallForm(forms.Form):
    obj_id = forms.IntegerField(required=True)
