from django import forms


class NoticeForm(forms.Form):
    content = forms.CharField(required=True)


class NoticeIDForm(forms.Form):
    obj_id = forms.CharField(required=True)


class SearchNoticeForm(forms.Form):
    current_page = forms.IntegerField(required=True)
    page_size = forms.IntegerField(required=True)
