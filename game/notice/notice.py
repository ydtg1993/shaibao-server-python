from notice.biz.notice import notice_group, notice_player, test_notice_player
from game.enums.notice_event import NoticeEvent
from system.cache.channel_name import get_channel_name
from three_server.enums.dice_type import Positions
from hall.biz.public_result import get_hall_previous_sequence, get_result
from ast import literal_eval
import time


def enter_notice(hall_id, hall_tag):
    """
    @api {post} /EnterNotice 进入房间通知
    @apiVersion 1.0.0
    @apiName EnterNotice
    @apiGroup WebSocket-Notice
    @apiSuccessExample {json} 通知样例:
    {
        "hall_tag": "Fast",
        "event": "EnterNotice",
        "data": {
            "player":{
                "gold": 1023,
                "bet_ls": []
            },
            "hall":{
                "stage": "BetStage",
                "past_result": [1, 2, 3],
                "bet_end_time": Date
            }
        }
    }
    """
    notice_player('用户连接名', hall_tag, NoticeEvent.EnterNotice.value, '返回数据')


def start_notice(hall_id, hall_tag, sequence):
    """
    @api {post} /GameStartNotice 游戏开始通知
    @apiVersion 1.0.0
    @apiName GameStartNotice
    @apiGroup WebSocket-Notice
    @apiSuccessExample {json} 通知样例:
    {
        "hall_tag": "Fast",
        "event": "GameStartNotice",
        "data": {
            "sequence": 1909060001,
            "previous_result": [1,2,3],
        }
    }
    """
    previous_sequence = get_hall_previous_sequence(hall_id, hall_tag)
    result = get_result(previous_sequence)
    result = [] if result == '' or result is None else literal_eval(result)
    notice_group(hall_tag, NoticeEvent.GameStartNotice.value, {
        'sequence': sequence[-4:],
        'previous_result': result
    })


def bet_notice(hall_tag, lottery_time, countdown):
    """
    @api {post} /StartBetNotice 游戏下注通知
    @apiVersion 1.0.0
    @apiName StartBetNotice
    @apiGroup WebSocket-Notice
    @apiSuccessExample {json} 通知样例:
    {
        "hall_tag": "Fast",
        "event": "StartBetNotice",
        "data": {
            "hall": {
                "lottery_time": Date
                "countdown": 5
            }
        }
    }
    """
    data = {
        'lottery_time': time.mktime(lottery_time.timetuple()),
        'countdown': countdown
    }
    notice_group(hall_tag, NoticeEvent.StartBetNotice.value, data)


def lottery_notice(hall_tag):
    """
    @api {post} /GameLotteryNotice 游戏开奖通知
    @apiVersion 1.0.0
    @apiName GameLotteryNotice
    @apiGroup WebSocket-Notice
    @apiSuccessExample {json} 通知样例:
    {
        "hall_tag": "Fast",
        "event": "GameLotteryNotice",
        "data": {}
    }
    """
    notice_group(hall_tag, NoticeEvent.GameLotteryNotice.value, {})


def lottery_result_notice(hall_tag, result):
    """
    @api {post} /GameLotteryResultNotice 游戏结果通知
    @apiVersion 1.0.0
    @apiName GameLotteryResultNotice
    @apiGroup WebSocket-Notice
    @apiSuccessExample {json} 通知样例:
    {
        "hall_tag": "Fast",
        "event": "GameLotteryResultNotice",
        "data": {
            "result": [1,2,3],
            "wins": ["BIG", "EVEN", "SUM_SIXTEEN"],
            "positions": [1,2,3]
        }
    }
    """
    result['positions'] = [Positions[d_type].value for d_type in result['wins']]
    notice_group(hall_tag, NoticeEvent.GameLotteryResultNotice.value, result)


def settle_notice(hall_tag):
    """
    @api {post} /GameSettleNotice 游戏结算通知
    @apiVersion 1.0.0
    @apiName GameSettleNotice
    @apiGroup WebSocket-Notice
    @apiSuccessExample {json} 通知样例:
    {
        "hall_tag": "Fast",
        "event": "GameSettleNotice",
        "data": {}
    }
    """
    notice_group(hall_tag, NoticeEvent.GameSettleNotice.value, {})


def winning_notice(players, hall_tag, wins):
    """
    @api {post} /WinningNotice 玩家中奖通知
    @apiVersion 1.0.0
    @apiName WinningNotice
    @apiGroup WebSocket-Notice
    @apiSuccessExample {json} 通知样例:
    {
        "hall_tag": "Fast",
        "event": "WinningNotice",
        "data": {
            "win_gold": 20,
            "positions": [1,2,3]
        }
    }
    """
    positions = [Positions[d_type].value for d_type in wins]
    for player in players:
        notice_player(get_channel_name(player['player__token']), hall_tag, NoticeEvent.WinningNotice.value, {
            'win_gold': str(player['bonus']),
            'positions': positions
        })


def over_notice(hall_tag):
    """
    @api {post} /GameOverNotice 游戏结束通知
    @apiVersion 1.0.0
    @apiName GameOverNotice
    @apiGroup WebSocket-Notice
    @apiSuccessExample {json} 通知样例:
    {
        "hall_tag": "Fast",
        "event": "GameOverNotice",
        "data": {}
    }
    """
    notice_group(hall_tag, NoticeEvent.GameOverNotice.value, {})


def bet_error(channel_name, hall_tag):
    """
    @api {post} /GameBetErrorNotice 下注异常通知
    @apiVersion 1.0.0
    @apiName GameBetErrorNotice
    @apiGroup WebSocket-Notice
    @apiSuccessExample {json} 通知样例:
    {
        "hall_tag": "Fast",
        "event": "GameBetErrorNotice",
        "data": {
            "code": 41002,
            "msg": "当阶段不允许",
            "gold": 10
        }
    }
    """
    print('---------------------------')
    test_notice_player(channel_name, hall_tag, NoticeEvent.EnterNotice.value, {})


def bet_success(channel_name, hall_tag):
    """
    @api {post} /GameBetSuccessNotice 下注成功通知
    @apiVersion 1.0.0
    @apiName GameBetSuccessNotice
    @apiGroup WebSocket-Notice
    @apiSuccessExample {json} 通知样例:
    {
        "hall_tag": "Fast",
        "event": "GameBetSuccessNotice",
        "data": {}
    }
    """
    notice_player(channel_name, hall_tag, NoticeEvent.EnterNotice.value, {})
