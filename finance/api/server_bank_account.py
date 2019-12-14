from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from finance.forms.server_bank_account import BankAccountForm, SearchBankAccountForm, BankAccountIDForm
from finance.biz.server_bank_account import search, add, remove, switch


class ServerBankAccountController(BaseController):

    def search(self):
        form = SearchBankAccountForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        data = search(**form.data)
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def add(self):
        form = BankAccountForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        add(**form.data)
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)

    def remove(self):
        form = BankAccountIDForm(self.get_arguments())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        remove(form.data['obj_id'])
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)

    def switch(self):
        form = BankAccountIDForm(self.get_arguments())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        switch(form.data['obj_id'])
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)
