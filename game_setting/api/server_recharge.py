import json

from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from game_setting.biz.server_recharge import methods, types, create, info, switch
from game_setting.forms.server_recharge import RechargeForm


class ServerRechargeController(BaseController):

    def methods(self):
        data = methods()
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def types(self):
        data = types()
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def switch(self):
        switch()
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)

    def save(self):
        form = RechargeForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        create(json.dumps(form.data))
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)

    def info(self):
        data = info()
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)
