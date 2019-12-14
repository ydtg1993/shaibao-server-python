from sign.models.sign_reward import SignReward


def search_server(**params):
    """
    后台查询奖励列表
    :return:
    """
    result = SignReward.search_server(**params)
    result['ls'] = [{
        'id': d['id'],
        # 'date': d['create_at'].strftime("%Y-%m-%d %H:%M:%S"),
        'day': d['sign_day'],
        # 'type': RewardTypeMsg[d['reward_type']].value,
        'value': d['reward_value'],
    } for d in result['ls']]
    return result


def init_reward():
    SignReward.delete_all()
    SignReward.init_sign_reward()
