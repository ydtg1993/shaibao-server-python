from player.models.player import Player


def search(params):
    """
    查询玩家列表
    :param params:
    :return:
    """
    result = Player.search(params)
    result['ls'] = [{
        'name': d['name'],
        'serial': d['serial'],
        'phone': d['phone'],
        'gold': d['gold'],
        'status': d['status']
    } for d in result['ls']]
    return result
