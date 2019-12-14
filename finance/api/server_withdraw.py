from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from finance.forms.server_withdraw import CheckWithdrawForm, WithdrawSearchForm
from finance.biz.server_withdraw import search_server, check


class ServerWithdrawController(BaseController):

    def search(self):
        form = WithdrawSearchForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        data = search_server(**form.data)
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def check(self):
        form = CheckWithdrawForm(self.body_data())
        if not form.is_valid():
            print(form.errors)
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        form.data['reviewer_id'] = self.request.user.id
        if not check(**form.data):
            return self.json(ResultCode.CODE_60006.value, None, ResultMsg.MSG_60006.value)
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)
