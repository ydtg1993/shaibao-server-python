from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from finance.forms.server_fast_account import FastAccountForm, SearchFastAccountForm, FastAccountIDForm
from finance.biz.server_fast_account import search, add, remove, switch, activation


class ServerFastAccountController(BaseController):

    def search(self):
        form = SearchFastAccountForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        data = search(**form.data)
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def add(self):
        form = FastAccountForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        add(**form.data)
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)

    def remove(self):
        form = FastAccountIDForm(self.get_arguments())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        remove(form.data['obj_id'])
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)

    def active(self):
        form = FastAccountIDForm(self.get_arguments())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        activation(form.data['obj_id'])
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)

    def switch(self):
        form = FastAccountIDForm(self.get_arguments())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        switch(form.data['obj_id'])
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)
