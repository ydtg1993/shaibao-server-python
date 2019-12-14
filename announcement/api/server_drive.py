from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from announcement.forms.server_drive import DriveForm, SearchDriveForm, DriveIDForm
from announcement.biz.server_drive import create_drive, search_server, remove, drive_type, drive_content_type


class ServerDriveController(BaseController):

    def create(self):
        form = DriveForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        create_drive(**form.data)
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)

    def remove(self):
        form = DriveIDForm(self.get_arguments())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        remove(form.data['obj_id'])
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)

    def search(self):
        form = SearchDriveForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        data = search_server(**form.data)
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def drive_type(self):
        ls = drive_type()
        return self.json(ResultCode.CODE_20000.value, ls, ResultMsg.MSG_20000.value)

    def drive_content_type(self):
        ls = drive_content_type()
        return self.json(ResultCode.CODE_20000.value, ls, ResultMsg.MSG_20000.value)
