from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from hall.biz.client_result import search
from hall.forms.client_result import LotteryRecordForms


class ClientResultController(BaseController):
    """
    @api {post} /three/hall/result/lottery_record 开奖记录
    @apiVersion 1.0.0
    @apiName lottery_record
    @apiGroup Hall
    @apiParam (参数) {String} hall_tag 大厅标识
    @apiSuccessExample {json} 返回样例:
    {
        "code": 20000,
        "message": "Succeed",
        "data": {
            "ls": [
                {
                    "id": 1,
                    "sequence": 0001,
                    "result": [1,2,3],
                    "big": False,
                    "even": True,
                    "sum": 6
                },
                ...
            ]
        }
        """
    def lottery_record(self):
        form = LotteryRecordForms(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        data = search(form.data['hall_tag'])
        return self.json(ResultCode.CODE_20000.value, {'ls': data}, ResultMsg.MSG_20000.value)
