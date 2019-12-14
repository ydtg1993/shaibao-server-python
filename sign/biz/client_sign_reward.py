from sign.models.sign_reward import SignReward
from sign.models.sign import SignRecord
from three_server.utils.time import get_current_week
import time


def search_client(player_id):
    """
    客户端查询奖励列表
    :return:
    """
    player_record = SignRecord.find_by_player_id(player_id)
    result = SignReward.search_client()
    if player_record is None:
        return {
            d['sign_day']: {
                'day': d['sign_day'],
                'is_sign': False,
                'allow': d['sign_day'] == 1
            } for d in result}
    s_time, e_time = get_current_week()
    now_time = int(time.strftime("%Y%m%d"))
    if s_time <= player_record.end_time <= e_time:
        return {
            d['sign_day']: {
                'day': d['sign_day'],
                'is_sign': player_record.total > d['sign_day'] or player_record.total == d['sign_day'],
                'allow': now_time != player_record.end_time and (player_record.total + 1) == d['sign_day']
            } for d in result}
    return {d['sign_day']: {'day': d['sign_day'], 'is_sign': False, 'allow': d['sign_day'] == 1} for d in result}


