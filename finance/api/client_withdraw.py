from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from finance.biz.client_withdraw import add, search_client
from player.biz.public_player import check_player_gold
from finance.forms.client_withdraw import WithdrawSearchForm, WithdrawForm


class ClientWithdrawController(BaseController):

    def add(self):
        """
        @api {post} /three/finance/withdraw/add 提现申请
        @apiVersion 1.0.0
        @apiName withdraw_add
        @apiGroup Finance
        @apiParam (参数) {Number} value 兑换金额
        @apiSuccessExample {json} 返回样例:
        {
            "code": 20000,
            "message": "Succeed",
            "data": {}
        }
        """
        form = WithdrawForm(self.body_data())
        if not form.is_valid():
            print(form.errors)
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        # 验证金额
        if not check_player_gold(self.request.player.token, form.data['value']):
            return self.json(ResultCode.CODE_40005.value, None, ResultMsg.MSG_40005.value)
        # 创建订单
        add(player_id=self.request.player.id, amount=form.data['value'])
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)

    def search(self):
        """
        @api {post} /three/finance/withdraw/search 查询提现记录
        @apiVersion 1.0.0
        @apiName withdraw_search
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
                        "sequence": 1,
                        "create_at": 2019-09-30,
                        "amount": 56,
                        "status": 0
                    },
                    {
                        "sequence": 1,
                        "create_at": 2019-09-30,
                        "amount": 56,
                        "status": -1
                    },
                    {
                        "sequence": 2,
                        "create_at": 2019-09-29,
                        "amount": 193.9,
                        "status": 1
                    },
                ],
                "total": 20
            }
        }
        """
        form = WithdrawSearchForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        form.data['player_id'] = self.request.player.id
        data = search_client(**form.data)
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)
