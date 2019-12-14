from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from player.forms.server_form import PlayerSearchForm
from player.biz.server_player import search


class ServerPlayerController(BaseController):

    def search(self):
        form = PlayerSearchForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        data = search(form.data)
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)
