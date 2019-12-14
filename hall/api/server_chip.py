from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from hall.models.hall import HallChipOption
from hall.forms.chip import HallSearchChipForm, EditChipForm
from hall.forms.hall import SwitchForm
from hall.biz.server_chip import get_chips


class ChipController(BaseController):

    def switch(self):
        form = SwitchForm(self.get_arguments())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        HallChipOption.switch(form.data['obj_id'])
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)

    def search(self):
        form = HallSearchChipForm(self.get_arguments())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        data = get_chips(form.data['hall_id'])
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def edit(self):
        form = EditChipForm(self.get_arguments())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        HallChipOption.edit(form.data['chip_id'], form.data['value'])
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)
