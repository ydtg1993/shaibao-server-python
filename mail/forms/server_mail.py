from django import forms


class CreateMailForm(forms.Form):
    mail_type = forms.CharField(required=True)          # 邮件类型
    tag = forms.CharField(required=True)                # 邮件标签
    title = forms.CharField(required=True)              # 邮件标题
    content_type = forms.CharField(required=True)       # 内容类型
    content = forms.CharField(required=True)            # 邮件内容
    exist_annex = forms.CharField(required=True)        # 存在附件
    annex = forms.CharField(required=False)             # 附件内容
    player_ids = forms.CharField(required=False)        # 玩家编号


class MailListForm(forms.Form):
    current_page = forms.IntegerField(required=True)
    page_size = forms.IntegerField(required=True)


class MailIDForm(forms.Form):
    mail_id = forms.CharField(required=True)  # 邮件ID