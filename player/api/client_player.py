import re
from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from player.forms.client_player import PlayerInfoForm, LeaderBoardForm
from player.biz.client_bet import leader_board
from player.biz.client_player import find_by_token

import logging

log = logging.getLogger('call_back')


class ClientPlayerController(BaseController):

    def leader_board(self):
        """
        @api {post} /three/player/player/leader_board 排行榜
        @apiVersion 1.0.0
        @apiName leader_board
        @apiGroup Player
        @apiDescription ranking:-1 则是未上榜
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
                        "ranking": 1,
                        "name": "孙坚",
                        "profit": 12345
                    },
                    {
                        "id": 2,
                        "ranking": 2,
                        "name": "孙策",
                        "profit": 12345.88
                    },
                    {
                        "id": 3,
                        "ranking": 3,
                        "name": "孙权",
                        "profit": 1245.88
                    }
                ],
                "own": {
                    "ranking": 3,
                    "name": "孙权",
                    "profit": 1245.88
                }
                "total": 20
            }
        }
        """
        form = LeaderBoardForm(self.body_data())
        if not form.is_valid():
            log.info(form.errors)
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        player = self.request.player
        data = leader_board(form.data['current_page'], form.data['page_size'], player)
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)

    def player_info(self):
        """
        @api {post} /three/player/player/player_info 获取玩家信息
        @apiVersion 1.0.0
        @apiName player_info
        @apiGroup Player
        @apiParam (参数) {String} token 玩家Token
        @apiSuccessExample {json} 返回样例:
        {
            "code": 20000,
            "message": "Succeed",
            "data": {
                "name": "苹果",
                "phone": "18009230222",
                "gold": 1023
            }
        }
        """
        _, player = find_by_token(self.request.player.token)
        data = {
            "serial": player.serial,
            "avatar": player.avatar,
            "name": player.name,
            "phone": player.phone,
            "gold": player.gold,
            "token": player.token
        }
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)
