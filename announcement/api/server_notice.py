from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from announcement.forms.server_notice import NoticeForm, NoticeIDForm, SearchNoticeForm
from announcement.biz.server_notice import create_notice, remove_notice, search_server


class ServerNoticeController(BaseController):

    def create(self):
        form = NoticeForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        create_notice(form.data['content'])
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)

    def remove(self):
        form = NoticeIDForm(self.get_arguments())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        remove_notice(form.data['obj_id'])
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)

    def search_server(self):
        form = SearchNoticeForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        data = search_server(**form.data)
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)
