from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from mail.forms.server_mail import CreateMailForm, MailListForm, MailIDForm
from mail.biz.server_mail import content_types, mail_types, annex_types
from mail.biz.server_mail import create_mail, search, delete_mail


class ServerMailController(BaseController):

    def create(self):
        form = CreateMailForm(self.body_data())
        print(form.data)
        if not form.is_valid():
            print(form.errors)
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        create_mail(**form.data)
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)

    def search(self):
        form = MailListForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        data = search(**form.data)
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def delete_mail(self):
        form = MailIDForm(self.get_arguments())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        delete_mail(form.data['mail_id'])
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)

    def content_types(self):
        data = content_types()
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def mail_types(self):
        data = mail_types()
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def annex_types(self):
        data = annex_types()
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)
