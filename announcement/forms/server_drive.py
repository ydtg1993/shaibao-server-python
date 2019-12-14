from django import forms


class DriveForm(forms.Form):
    title = forms.CharField(required=True, max_length=6)
    content_type = forms.CharField(required=True)
    content = forms.CharField(required=True)
    drive_type = forms.CharField(required=True)


class DriveIDForm(forms.Form):
    obj_id = forms.CharField(required=True)


class SearchDriveForm(forms.Form):
    current_page = forms.IntegerField(required=True)
    page_size = forms.IntegerField(required=True)
