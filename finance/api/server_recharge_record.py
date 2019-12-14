from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from finance.forms.server_recharge_record import RechargeRecordForm, CheckRechargeForm
from finance.biz.server_recharge_record import search, check
from player.notice.player_notice import update_player_info


class ServerRechargeRecordController(BaseController):

    def search(self):
        form = RechargeRecordForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        data = search(**form.data)
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def check(self):
        form = CheckRechargeForm(self.body_data())
        if not form.is_valid():
            print(form.errors)
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        form.data['reviewer_id'] = self.request.user.id
        ok, player = check(**form.data)
        if not ok:
            return self.json(ResultCode.CODE_60006.value, None, ResultMsg.MSG_60006.value)
        if player is not None:
            update_player_info(player)
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)
