from hall.models.hall import Hall


def next_hall_stage(hall_id):
    """
    大厅阶段切换
    :param hall_id:
    :return:
    """
    return Hall.next_hall_stage(hall_id)


def update_lottery_time(hall_id, value):
    """
    更新开奖时间
    :param hall_id: 大厅ID
    :param value: 新的开奖时间
    :return: Boolean
    """
    return Hall.update_lottery_time(hall_id, value)


def get_hall_bet_second(hall_id):
    """
    获取大厅倒计时
    :param hall_id:
    :return:
    """
    return Hall.get_bet_second(hall_id)


def find_by_id(hall_id):
    """
    根据ID查询
    :param hall_id:
    :return:
    """
    return Hall.hall_info(hall_id=hall_id)
