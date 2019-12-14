from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from sign.biz.client_sign import check_sign, random_sign


class ClientSignController(BaseController):

    def sign(self):
        """
        @api {post} /three/sign/sign/sign 玩家签到
        @apiVersion 1.0.0
        @apiName sign
        @apiGroup Sign
        @apiSuccessExample {json} 返回样例:
        {
            "code": 20000,
            "message": "Succeed",
            "data": {
                "type": "GOLD",
                "value": "19.88",
            }
        }
        """
        player = self.request.player
        is_sign = check_sign(player.id)
        if is_sign:
            return self.json(ResultCode.CODE_60003.value, None, ResultMsg.MSG_60003.value)
        data = random_sign(player.id)
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)
