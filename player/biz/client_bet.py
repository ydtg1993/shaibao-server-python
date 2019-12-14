from player.models.player import Player, BetRecord
from ast import literal_eval
from three_server.utils.time import get_now


def find_by_seq(req):
    """
    根据期号查询下注记录
    :param req: 期号
    :return: 下注集合
    """
    return BetRecord.find_by_seq(req)


def leader_board(current_page, page_size, player):
    """
    玩家排行榜
    :param current_page:
    :param page_size:
    :param player:
    :return:
    """
    time_range = get_now()
    data = BetRecord.leader_board(current_page, page_size, time_range)
    ls = []
    data['own'] = {}
    for index, d in enumerate(data['ls']):
        ls.append({
            'ranking': index + 1,
            'id': d['player_id'],
            'name': d['player__name'],
            'profit': d['total'],
        })
        data['own'] = ls[index]
    data['ls'] = ls
    if not data['own'] == {}:
        return data
    own = BetRecord.sum_player_bet(player.id, time_range)
    if len(own) == 0:
        data['own'] = {
            'ranking': -1,
            'name': player.name,
            'profit': "0"
        }
    else:
        data['own'] = {
            'ranking': -1,
            'name': own[0]['player__name'],
            'profit': own[0]['total']
        }
    return data


def bet_record(**params):
    """
    查询下注记录
    :param params:
    :return:
    """
    return [{
        "hall_tag": d['sequence'].split('-')[0],
        "sequence": d['sequence'].split('-')[1],
        "create_at": d['sequence__create_at'].strftime("%H:%M:%S"),
        "result": [] if d['sequence__result'] == '' or d['sequence__result'] is None else literal_eval(d['sequence__result']),
        "state": d['state'],
        "bonus": d['bonus'],
        "bet_type": d['bet_type'],
        "bet_amount": d['bet_amount'],
    } for d in BetRecord.search_bet_record(**params)]
