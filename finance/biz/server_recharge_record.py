import json
import time
import decimal

from finance.models.recharge_record import RechargeRecord
from finance.enums.recharge import RechargeStatusEnum
from system.models.keyValue import KeyValue
from system.enums.keyValue import Keys
from game_setting.enums.recharge import RechargeType
from player.models.player import Player


def search(**params):
    result = RechargeRecord.search_server(**params)
    result['ls'] = [{
        'id': d['id'],
        'create_at': d['create_at'].strftime("%Y-%m-%d"),
        'player_name': d['player__name'],
        'depositor': d['depositor'],
        'pay_money': d['pay_money'],
        'type': d['type'],
        'payee': d['payee'],
        'account_id': d['account_id'],
        'status': d['status'],
        'reviewer_name': d['reviewer__username']
    } for d in result['ls']]
    return result


def check(**params):
    if params['allow'] == RechargeStatusEnum.SUCCEED.value:
        ok, obj = RechargeRecord.check_recharge(**params)
        ok, player = Player.update_player_gold(obj.player.token, obj.pay_money)
        recharge_strategy(obj.player.token, obj.pay_money)
        return ok, player
    elif params['allow'] == RechargeStatusEnum.FAILED.value:
        ok, _ = RechargeRecord.check_recharge(**params)
        return ok, None
    return False, None


def recharge_strategy(player_token, value):
    value = decimal.Decimal(value)
    activate = KeyValue.get_value(Keys.RECHARGE_TACTICS_ACTIVATE.value)
    if activate != str(True):
        return
    info = KeyValue.get_value(Keys.RECHARGE_TACTICS_INFO.value)
    if info is None or info == {}:
        return
    info = json.loads(info)
    now_time = int(time.strftime("%Y%m%d%H%M%S"))
    reward = 0
    if int(info['range'][0]) < now_time < int(info['range'][1]):
        if info['method'] == "INTERVAL":  # 区间
            for v in info['value']:
                if decimal.Decimal(v['min']) <= value < decimal.Decimal(v['max']):
                    reward = v['reward']
                    break
        if info['method'] == "FIXED":  # 固定值
            for v in info['value']:
                if decimal.Decimal(v['recharge_amount']) == value:
                    reward = v['reward_amount']
                    break
        if info['method'] == "PERCENTAGE":  # 百分比
            x = decimal.Decimal(info['value']) / 100
            reward = value * x
        if reward == 0:
            return
        if info['type'] == RechargeType.GOLD.value:
            Player.update_player_gold(player_token, reward)
        elif info['type'] == RechargeType.INTEGRAL.value:
            Player.update_player_integral(player_token, reward)
