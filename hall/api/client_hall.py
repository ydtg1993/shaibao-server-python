from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from hall.forms.client_hall import EnterHallForm
from hall.biz.client_hall import hall_info
from system.cache.player import set_player_hall


class ClientHallController(BaseController):

    def enter_hall(self):
        """
        @api {post} /three/hall/client/enter_hall 进入大厅
        @apiVersion 1.0.0
        @apiName enter_hall
        @apiGroup Hall
        @apiParam (参数) {String} hall_tag 大厅标识
        @apiSuccessExample {json} 返回样例:
        {
            "code": 20000,
            "message": "Succeed",
            "data": {
                "id": 1,
                "name": "极速快三",
                "lottery_type": "Self",
                "lottery_time": 1212121212,
                "game_date": "极速快三",
                "stage": "BetStage",
                "total": "100",
                "sequence": 1909050001,
                "previous_result": [],
                "bet_option": {
                    "1": {
                        "dice_type": "BIG",
                        "odds": 1
                    },
                    "2": {
                        "dice_type": "SMALL",
                        "odds": 1
                    },
                    ...
                },
                "chip_option": {
                    "1": {
                        "label": "100",
                        "value": 100,
                    },
                    "2": {
                        "label": "1千",
                        "value": 1000,
                    },
                    "3": {
                        "label": "1万",
                        "value": 10000,
                    },
                    ...
                },
                "player": {
                    "gold": 99
                }
            }
        """
        form = EnterHallForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        ok, result = hall_info(hall_tag=form.data['hall_tag'])
        if not ok:
            return self.json(ResultCode.CODE_60007.value, None, ResultMsg.MSG_60007.value)
        player = self.request.player
        result['player'] = {'gold': player.gold}
        set_player_hall(player.token, result['id'])
        return self.json(ResultCode.CODE_20000.value, result, ResultMsg.MSG_20000.value)
