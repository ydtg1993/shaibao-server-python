from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from finance.biz.client_pay import pay_method, record, to_pay
from finance.forms.client_pay import PayForm, PayRecordForm


class ClientPayController(BaseController):

    def pay_method(self):
        """
        @api {post} /three/finance/pay/pay_method 查询支付方式
        @apiVersion 1.0.0
        @apiName pay_method
        @apiGroup Finance

        @apiSuccessExample {json} 返回样例:
        {
            "code": 20000,
            "message": "Succeed",
            "data": {
                "fast": {
                    "0": {
                        "id": "1",
                        "name": "奥利瑞安·索尔",
                        "number": "123456789",
                        "qr_code": "base64****",
                    }
                },
                "banks": {
                    "0": {
                        "id": "1",
                        "bank_name": "中国邮政银行",
                        "interval": "5000-100000",
                        "name": "123456789",
                        "number": "123456789",
                    },
                    "1": {
                        "id": "2",
                        "bank_name": "中国建设银行",
                        "interval": "5000-8000",
                        "name": "123456789",
                        "number": "123456789",
                    },
                },
            }
        }
        """
        data = pay_method()
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def to_pay(self):
        """
        @api {post} /three/finance/pay/to_pay 支付
        @apiVersion 1.0.0
        @apiName to_pay
        @apiGroup Finance
        @apiParam (参数) {String} pay_type 支付类型
        @apiParam (参数) {String} account_id 方式ID
        @apiParam (参数) {String} player_name 玩家名称
        @apiParam (参数) {String} pay_money 支付金额
        @apiSuccessExample {json} 返回样例:
        {
            "code": 20000,
            "message": "Succeed",
            "data": {}
        }
        """
        form = PayForm(self.body_data())
        if not form.is_valid():
            print(form.errors)
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        form.data['player_id'] = self.request.player.id
        if not to_pay(**form.data):
            return self.json(ResultCode.CODE_60008.value, None, ResultMsg.MSG_60008.value)
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)

    def record(self):
        """
        @api {post} /three/finance/pay/record 支付记录
        @apiVersion 1.0.0
        @apiName pay_record
        @apiGroup Finance
        @apiParam (参数) {Number} current_page 当前页
        @apiParam (参数) {Number} page_size 页行数
        @apiSuccessExample {json} 返回样例:
        {
            "code": 20000,
            "message": "Succeed",
            "data": {
                "ls": [
                    {
                        "id": 1,
                        "type": "快捷支付",
                        "pay_money": "987.00",
                        "create_at": "2019.09.20",
                        "status": 1,
                    },
                    {
                        "id": 2,
                        "type": "银行支付",
                        "pay_money": "987.00",
                        "create_at": "2019.09.20",
                        "status": 0,
                    },
                ],
                "total": 20
            }
        }
        """
        form = PayRecordForm(self.body_data())
        if not form.is_valid():
            print(form.errors)
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        data = record(**form.data)
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def recharge(self):
        # test(10)
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)
