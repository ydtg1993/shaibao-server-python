from hall.models.hall import HallChipOption


def get_chips(hall_id):
    """
    查询大厅筹码选项
    :param hall_id:
    :return:
    """
    return [{
        'id': bet['id'],
        'position': bet['position'],
        'value': bet['value'],
        'active': bet['active']
    } for bet in HallChipOption.find_by_hall_id(hall_id)]


def check_value(hall_id, value):
    """
    检查下注金额
    :param hall_id: 大厅ID
    :param value: 下注金额
    :return: Boolean
    """
    for chip in HallChipOption.find_by_hall_id(hall_id):
        if value == chip['value']:
            return True
    return False

