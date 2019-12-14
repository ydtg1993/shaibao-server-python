from sign.models.sign import SignRecord
from sign.models.sign_reward import SignReward
from sign.enums.week import Week
from three_server.utils.time import get_current_week
from sign.enums.sign_reward import RewardType
from player.models.player import Player
import time


def continuous_sign(player_id):
    """
    玩家连续签到
    :param player_id: 玩家ID
    :return:
    """
    # TODO 此代码块未完成
    obj = SignRecord.find_by_player_id(player_id)
    if obj is None or time.strftime("%A") == Week.MONDAY.value:
        params = init_sign()
        SignRecord.create_or_update(player_id, **params)
        return True
    now_time = int(time.strftime("%Y%m%d"))
    if now_time - obj.end_time == 1:
        params = {'start_time': obj.start_time, 'end_time': now_time, 'total': obj.total + 1}
        SignRecord.create_or_update(player_id, **params)
        return True
    SignRecord.create_or_update(player_id, **init_sign())
    return True


def random_sign(player_id):
    """
    玩家周内任意签到
    :param player_id: 玩家ID
    :return:
    """
    # 查询玩家签到记录
    obj = SignRecord.find_by_player_id(player_id)
    # 不存在签到 或 今日为周一 则初始化签到
    if obj is None or time.strftime("%A") == Week.MONDAY.value:
        return create_or_update(player_id, **init_sign())
    # 判断玩家上次签到是否在本周
    s_time, e_time = get_current_week()
    if s_time <= obj.end_time <= e_time:
        now_time = int(time.strftime("%Y%m%d"))
        params = {'start_time': obj.start_time, 'end_time': now_time, 'total': obj.total + 1}
        return create_or_update(player_id, **params)
    # 不在本周初始化签到
    return create_or_update(player_id, **init_sign())


def create_or_update(player_id, **params):
    """
    创建或者修改签到
    :param player_id: 玩家id
    :param params: 签到参数
    :return: 奖励
    """
    SignRecord.create_or_update(player_id, **params)
    SignReward.find_by_day(params['total'])
    reward = SignReward.find_by_day(params['total'])
    if reward.reward_type == RewardType.GOLD.value:
        Player.update_gold_by_id(player_id, reward.reward_value)
    return {'type': reward.reward_type, 'value': reward.reward_value}


def check_sign(player_id):
    """
    检查今日是否签到
    :param player_id: 玩家ID
    :return:
    """
    now_time = int(time.strftime("%Y%m%d"))
    return SignRecord.check_sign(player_id, now_time)


def init_sign():
    """
    初始换一个签到
    :return:
    """
    init_time = int(time.strftime("%Y%m%d"))
    params = {
        'start_time': init_time,
        'end_time': init_time,
        'total': 1,
    }
    return params
