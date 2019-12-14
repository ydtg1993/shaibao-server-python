from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from finance.biz.client_bank_option import search


class ClientBankOptionController(BaseController):

    def search(self):
        """
        @api {post} /three/finance/bank/search 查询银行卡选项
        @apiVersion 1.0.0
        @apiName bank_search
        @apiGroup Finance
        @apiSuccessExample {json} 返回样例:
        {
            "code": 20000,
            "message": "Succeed",
            "data": {
                "1": "中国银行",
                "2": "平安银行",
                "3": "邮政银行",
            }
        }
        """
        data = search()
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)
