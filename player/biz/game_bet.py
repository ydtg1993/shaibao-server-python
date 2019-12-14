from player.models.player import BetRecord


def get_win_players(seq, win_types):
    """
    获取赢家
    :param seq: 期号
    :param win_types: 赢骰型
    :return: 赢家集合
    """
    return BetRecord.search_win(seq, win_types)


def set_lose(sequence, win_types):
    """
    设置输家
    :param sequence:
    :param win_types:
    :return:
    """
    BetRecord.set_lose(sequence, win_types)


def set_win(sequence, win_types):
    """
    设置赢家
    :param sequence:
    :param win_types:
    :return:
    """
    BetRecord.set_win(sequence, win_types)


def sum_win_bonus(sequence, win_types):
    """
    统计赢家奖金
    :return:
    """
    result = BetRecord.sum_win(sequence, win_types)
    if len(result) == 0:
        return 0
    return result[0]['bonus']


def sum_bet(sequence):
    """
    统计下注金额
    :return:
    """
    result = BetRecord.sum_bet(sequence)
    if len(result) == 0:
        return 0
    return result[0]['sum_bet_amount']
