from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from hall.models.hall import Hall
from hall.forms.hall import HallSearchForm, HallCreateForm, HallEditForm, StartHallForm
from hall.forms.hall import SwitchForm
from hall.enums.hall import HallTag, HallTagMsg, LotteryType, LotteryTypeMsg
from game.stage import start_stage
import logging

log = logging.getLogger('game')


class HallController(BaseController):

    def create(self):
        form = HallCreateForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        Hall.create(form.data)
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)

    def switch(self):
        form = SwitchForm(self.get_arguments())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        ok, hall = Hall.switch(form.data['obj_id'])
        if not ok:
            return self.json(ResultCode.CODE_60009.value, None, ResultMsg.MSG_60009.value)
        if hall.active:
            start_stage.delay(hall.id, hall.tag)
            return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)
        # start_stage.apply_async((hall.id,),
        # countdown=10)

    def search(self):
        form = HallSearchForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        data = Hall.search(form.data)
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def edit(self):
        form = HallEditForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        data = Hall.edit(form.data)
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def hall_options(self):
        data = Hall.hall_options()
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def start(self):
        form = StartHallForm(self.get_arguments())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)

    def send_msg(self):
        # data = self.get_arguments()
        # if data['type'] == '1':
        #     notice_group('大厅标识', '事件', '返回数据')
        # else:
        #     notice_player(data['obj'], '大厅标识', '事件', '返回数据')
        from player.models.player import BetRecord
        ls = BetRecord.sum_bet('Fast-1909175025')

        # BetRecord.set_lose('Fast-1909101583', ['BIG2'])
        # BetRecord.set_win('Fast-1909101583', ['BIG'])
        return self.json(ResultCode.CODE_20000.value, ls, ResultMsg.MSG_20000.value)

    def tag_options(self):
        data = [{'label': HallTagMsg[state.value].value, 'value': state.value} for state in HallTag]
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def lottery_options(self):
        data = [{'label': LotteryTypeMsg[state.value].value, 'value': state.value} for state in LotteryType]
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def start_hall(self):
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)
