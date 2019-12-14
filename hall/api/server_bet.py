from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from hall.models.hall import HallBetOption
from hall.forms.bet import HallSearchBetForm, EditBetForm
from hall.forms.hall import SwitchForm
from hall.biz.server_bet import get_bets


class BetController(BaseController):

    def switch(self):
        form = SwitchForm(self.get_arguments())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        HallBetOption.switch(form.data['obj_id'])
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)

    def search(self):
        form = HallSearchBetForm(self.get_arguments())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        data = get_bets(form.data['hall_id'])
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def edit(self):
        form = EditBetForm(self.get_arguments())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        HallBetOption.edit(form.data['bet_id'], form.data['odds'])
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)
