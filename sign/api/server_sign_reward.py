from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from sign.biz.server_sign_reward import search_server, init_reward
from sign.forms.client_sign_reward import SearchForm


class ServerSignRewardController(BaseController):

    def search(self):
        form = SearchForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        data = search_server(**form.data)
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def init_reward(self):
        init_reward()
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)
