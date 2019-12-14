from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from announcement.biz.client_pig import pig_info, pig_open


class PigController(BaseController):

    def info(self):
        """
        @api {post} /three/announcement/pig/info 金猪活动详情
        @apiVersion 1.0.0
        @apiName pigInfo
        @apiGroup Announcement
        @apiSuccessExample {json} 返回样例:
        {
            "code": 20000,
            "message": "Succeed",
            "data": {
                "player_integral": 9000,
                "total": 999999,
                "record": [
                    {"name": "亚托克斯", "gold": 500},
                    {"name": "维鲁斯", "gold": 500},
                    {"name": "拉亚斯特", "gold": 500}
                ]
            }
        }
        """
        data = pig_info()
        data['player_integral'] = self.request.player.integral
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def open(self):
        """
        @api {post} /three/announcement/pig/open 砸金猪接口
        @apiVersion 1.0.0
        @apiName pigOpen
        @apiGroup Announcement
        @apiSuccessExample {json} 返回样例:
        {
            "code": 20000,
            "message": "Succeed",
            "data": {
                "gold": 50
            }
        }
        """
        data = pig_open(self.request.player.id, self.request.player.token)
        return self.json(ResultCode.CODE_20000.value, {'gold': data}, ResultMsg.MSG_20000.value)
