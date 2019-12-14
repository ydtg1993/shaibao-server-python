from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg


class ClientBankAccountController(BaseController):

    def search(self):
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)
