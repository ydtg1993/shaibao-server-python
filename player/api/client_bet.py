from three_server.base.controller import BaseController
from three_server.base.result import ResultCode, ResultMsg
from player.biz.client_bet import bet_record
from player.forms.client_bet import ClientBetRecordForm


class ClientBetController(BaseController):

    def bet_record(self):
        """
        @api {post} /three/player/bet/bet_record 下注记录
        @apiVersion 1.0.0
        @apiName bet_record
        @apiGroup Player
        @apiDescription ranking:-1 则是未上榜
        @apiParam (参数) {Number} current_page 当前页
        @apiParam (参数) {Number} page_size 页行数
        @apiParam (参数) {Array} types 类型 未开奖：0 赢：1 输：-1
        @apiSuccessExample {json} 返回样例:
        {
            "code": 20000,
            "message": "Succeed",
            "data": {
                "ls": [
                    {
                        "hall_tag": "Fast",
                        "sequence": "201908151281",
                        "create_at": "21:01:00",
                        "result": [1,2,4],
                        "state": 1,
                        "bonus": 200,
                        "bet_type": "BIG",
                        "bet_amount": 200,
                    },
                    {
                        "hall_tag": "Fast",
                        "sequence": "201908151281",
                        "create_at": "21:01:00",
                        "result": [1,2,4],
                        "state": 1,
                        "bonus": 200,
                        "bet_type": "BIG",
                        "bet_amount": 200,
                    }
                ],
                "total": 20
            }
        }
        @apiSuccess (响应备注) {String} hall_tag 大厅标签
        @apiSuccess (响应备注) {String} sequence 期号
        @apiSuccess (响应备注) {String} create_at 时间
        @apiSuccess (响应备注) {Array} result 开奖结果
        @apiSuccess (响应备注) {String} state 状态 0:未开奖 1:赢 -1:输
        @apiSuccess (响应备注) {String} bonus 奖金
        @apiSuccess (响应备注) {String} bet_type 下注类型
        @apiSuccess (响应备注) {String} bet_amount 下注金额
        """
        form = ClientBetRecordForm(self.body_data())
        if not form.is_valid():
            return self.json(ResultCode.CODE_40003.value, None, ResultMsg.MSG_40003.value)
        player = self.request.player
        form.data['player_id'] = player.id
        data = bet_record(**form.data)
        return self.json(ResultCode.CODE_20000.value, data, ResultMsg.MSG_20000.value)


