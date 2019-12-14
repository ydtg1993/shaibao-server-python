from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from hall.forms.result import ResultSearchForm
from hall.biz.server_result import search_result


class ResultController(BaseController):

    def search(self):
        form = ResultSearchForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        data = search_result(**form.data)
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)
