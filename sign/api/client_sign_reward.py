from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from sign.biz.client_sign_reward import search_client


class ClientSignRewardController(BaseController):

    def search(self):
        """
        @api {post} /three/sign/reward/search 签到奖励列表
        @apiVersion 1.0.0
        @apiName search
        @apiGroup Sign
        @apiSuccessExample {json} 返回样例:
        {
            "code": 20000,
            "message": "Succeed",
            "data": [
                "1": {
                    "day":"1",
                    "is_sign": False,
                    "allow": True,
                },
                "2": {
                    "day":"2",
                    "is_sign": False,
                    "allow": False,
                }
            ]
        }
        """
        data = search_client(self.request.player.id)
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)
