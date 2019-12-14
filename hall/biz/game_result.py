from hall.models.hall import Result


def init_result(hall_id, sequence):
    """
    初始化记录
    :param hall_id: 大厅ID
    :param sequence: 期号
    :return: Result
    """
    return Result.init(hall_id, sequence)


def set_result(seq, result):
    """
    设置本期开奖结果
    :param seq: 序列
    :param result: 开奖结果
    :return: ok?
    """
    return Result.set_result(seq, result)


def update_bonus_and_bet_count(sequence, bonus, bet_count):
    """
    设置本期下注金额,开奖金额
    :param sequence:
    :param bonus:
    :param bet_count:
    :return:
    """
    Result.update_bonus_and_bet_count(sequence, bonus, bet_count)
