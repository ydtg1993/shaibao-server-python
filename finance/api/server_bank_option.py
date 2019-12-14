from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from finance.forms.server_bank import ServerAddBankForm, ServerSearchBankForm, ServerBankIdForm
from finance.biz.server_bank_option import search, add, remove, find_by_name, init_option, delete_all, switch


class ServerBankOptionController(BaseController):

    def search(self):
        form = ServerSearchBankForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        data = search(**form.data)
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def add(self):
        form = ServerAddBankForm(self.get_arguments())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        if find_by_name(form.data['name']) is not None:
            return self.json(ResultCode.CODE_60004.value, None, ResultMsg.MSG_60004.value)
        add(form.data['name'])
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)

    def remove(self):
        form = ServerBankIdForm(self.get_arguments())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        remove(form.data['obj_id'])
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)

    def switch(self):
        form = ServerBankIdForm(self.get_arguments())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        switch(form.data['obj_id'])
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)

    def init_bank(self):
        delete_all()
        init_option()
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)
