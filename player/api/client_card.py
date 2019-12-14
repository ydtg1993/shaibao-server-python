from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from player.forms.client_card import CardForm
from player.biz.client_card import create, player_card


class ClientCardController(BaseController):

    def add(self):
        """
        @api {post} /three/player/card/add 添加银行卡
        @apiVersion 1.0.0
        @apiName card_add
        @apiGroup Player
        @apiParam (参数) {String} name 名称
        @apiParam (参数) {String} number 银行卡号
        @apiParam (参数) {Number} bank_id 开户行
        @apiParam (参数) {String} bank_branch 支行
        @apiSuccessExample {json} 返回样例:
        {
            "code": 20000,
            "message": "Succeed",
            "data": {}
        }
        """
        form = CardForm(self.body_data())
        if not form.is_valid():
            print(form.errors)
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        form.data['player_id'] = self.request.player.id
        print(form.data)
        create(form.data)
        return self.json(ResultCode.CODE_20000.value, None, ResultMsg.MSG_20000.value)

    def info(self):
        """
        @api {post} /three/player/card/info 获取玩家银行卡
        @apiVersion 1.0.0
        @apiName player_card
        @apiGroup Player
        @apiSuccessExample {json} 返回样例:
        {
            "code": 20000,
            "message": "Succeed",
            "data": {
                "name": "藤田",
                "number": "23123123123",
                "bank_name": "交通银行",
                "bank_branch": "支行",
            }
        }
        """
        data = player_card(self.request.player.id)
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)
