from player.models.player import Player, BetRecord
from system.cache.player import get_player_hall
from hall.biz.public_result import get_hall_new_sequence
from hall.biz.game_chip import check_value
from hall.biz.game_bet import check_bet
from hall.biz.game_hall import find_by_id
from decimal import Decimal
from player.biz.public_player import update_player_gold
from game.forms.bet_form import BetForm
from game.notice.notice import bet_error, bet_success
from system.cache.channel_name import get_player_token
from system.cache.hall import get_hall_tag
from hall.enums.hall import HallStage
from notice.enums.server_code import ServerCode, ServerMsg
from game.enums.notice_event import NoticeEvent

import logging

log = logging.getLogger('game')


def bet(channel_name, **params):
    """
    @api {post} /ReqBet 游戏下注接口
    @apiVersion 1.0.0
    @apiName ReqBet
    @apiGroup WebSocket-Receive
    @apiSuccessExample {json} 通知样例:
    {
        "event": "ReqBet",
        "data": {
            "bet_amount": 200,
            "dice_type": "SUM_THREE"
        }
    }
    """
    log.info('*****************************************')
    log.info(params)
    player_token = get_player_token(channel_name)
    hall_id = get_player_hall(player_token)
    log.info(player_token)
    log.info(hall_id)
    event = NoticeEvent.GameBetErrorNotice.value
    ok, hall = find_by_id(hall_id)
    if not ok:
        log.info('未查询到大厅')
        # bet_error(channel_name, hall.tag)
        return create_result(hall.tag, event, {'code': ServerCode.CODE41001.value, 'msg': ServerMsg.CODE41001.value, 'gold': params['bet_amount']})
    if hall.stage != HallStage.BetStage.value:
        log.info("大厅当前阶段【%s】当前阶段不允许下注" % hall.stage)
        bet_error(channel_name, hall.tag)
        return create_result(hall.tag, event, {'code': ServerCode.CODE41002.value, 'msg': ServerMsg.CODE41002.value, 'gold': params['bet_amount']})
    form = BetForm(params)
    if not form.is_valid():
        log.info(form.errors)
        return create_result(hall.tag, event, {'code': ServerCode.CODE41006.value, 'msg': ServerMsg.CODE41006.value, 'gold': params['bet_amount']})
        # bet_error(channel_name, hall_tag)
    ok, player = Player.find_by_token(player_token)
    if not ok:
        log.info('未查询到玩家')
        return create_result(hall.tag, event, {'code': ServerCode.CODE41003.value, 'msg': ServerMsg.CODE41003.value, 'gold': params['bet_amount']})
        # bet_error(channel_name, hall_tag)
    # 获取大厅ID
    hall_id = get_player_hall(player_token)
    sequence = get_hall_new_sequence(hall_id, hall.tag)
    # 检查下注金额
    if not check_value(hall_id, params['bet_amount']):
        log.info('下注金额不正确')
        return create_result(hall.tag, event, {'code': ServerCode.CODE41004.value, 'msg': ServerMsg.CODE41004.value, 'gold': params['bet_amount']})
        # bet_error(channel_name, hall_tag)
    # 检查下注类型
    ok, odds = check_bet(hall_id, params['dice_type'])
    if not ok:
        log.info('下注类型不正确')
        return create_result(hall.tag, event, {'code': ServerCode.CODE41005.value, 'msg': ServerMsg.CODE41005.value, 'gold': params['bet_amount']})
        # bet_error(channel_name, hall_tag)
    if Decimal(params['bet_amount']) > player.gold:
        log.info('玩家金额不足')
        return create_result(hall.tag, event, {'code': ServerCode.CODE41007.value, 'msg': ServerMsg.CODE41007.value, 'gold': 0})
    # 计算下注奖金
    bonus = Decimal(params['bet_amount']) * Decimal(odds)
    # 扣除玩家金币
    update_player_gold(player.token, -params['bet_amount'])
    # 创建下注记录
    BetRecord.create(player.id, sequence, params['bet_amount'], params['dice_type'], bonus)
    return None


def create_result(hall_tag, event, data):
    return {
        "hall_tag": hall_tag,
        "event": event,
        "data": data
    }
