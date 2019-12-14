from hall.utils.sequence import get_sequence
from three_server.utils.time import get_now
from hall.models.hall import Result


def get_hall_new_sequence(hall_id, hall_tag):
    """
    获取最新的期号
    :param hall_tag: 大厅标签
    :param hall_id: 大厅ID
    :return: 最新的期号
    """
    count = Result.sum_now(hall_id, get_now())
    return get_sequence(hall_tag, count)


def get_hall_next_sequence(hall_id, hall_tag):
    """
    获取下一次的期号
    :param hall_tag: 大厅标签
    :param hall_id: 大厅ID
    :return: 下一次的期号
    """
    count = Result.sum_now(hall_id, get_now())
    return get_sequence(hall_tag, count + 1)


def get_hall_previous_sequence(hall_id, hall_tag):
    """
    获取上一次的期号
    :param hall_tag: 大厅标签
    :param hall_id: 大厅ID
    :return: 上一次的期号
    """
    count = Result.sum_now(hall_id, get_now())
    return None if count is 0 else get_sequence(hall_tag, count - 1)


def get_result(seq):
    """
    获取本期开奖结果
    :param seq: 序列
    :return: ok?
    """
    return Result.get_result(seq)
