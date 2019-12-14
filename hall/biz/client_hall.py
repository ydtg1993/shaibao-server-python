from hall.models.hall import Hall, HallBetOption, HallChipOption
from hall.biz.public_result import get_hall_new_sequence, get_hall_previous_sequence, get_result
from ast import literal_eval
import time
import pytz
import logging
log = logging.getLogger('info')


def hall_info(hall_id=None, hall_tag=None):
    """
    获取大厅详情
    :param hall_tag:
    :param hall_id:
    :return:
    """
    ok, obj = Hall.hall_info(hall_id=hall_id, hall_tag=hall_tag)
    if not ok:
        return False, None
    hall = model_to_dict(obj)
    hall['sequence'] = get_hall_new_sequence(obj.id, obj.tag)[-4:]
    result = get_result(get_hall_previous_sequence(obj.id, obj.tag))
    hall['previous_result'] = [] if result == '' or result is None else literal_eval(result)
    hall['bet_option'] = hall_bet_option(obj.id)
    hall['chip_option'] = hall_chip_option(obj.id)
    return True, hall


def hall_bet_option(hall_id):
    """
    获取下注选项
    :param hall_id:
    :return:
    """
    return {
        bet['position']: {
            'dice_type': bet['dice_type'],
            'odds': str(bet['odds']).split('.')[0] if str(bet['odds']).split('.')[1] == '00' else bet['odds']}
        for bet in HallBetOption.find_by_hall_id_c(hall_id)
    }


def hall_chip_option(hall_id):
    """
    获取筹码选项
    :param hall_id:
    :return:
    """
    return {chip['position']: {
        'label': chip_format(chip['value']),
        'value': chip['value'],
    } for chip in HallChipOption.find_by_hall_id_c(hall_id)}


def model_to_dict(hall):
    """
    对象转字典
    :param hall:
    :return:
    """
    f_time = hall.lottery_time.astimezone(pytz.timezone('Asia/Shanghai'))
    return {
        # 'name': hall.name,
        # 'lottery_type': hall.bet_type,
        'id': hall.id,
        'game_date': hall.game_date,
        'stage': hall.stage,
        'total': hall.total,
        'lottery_time': time.mktime(hall.lottery_time.timetuple()),
        'countdown': int(time.mktime(f_time.timetuple())) - int(time.time())
    }


def chip_format(value):
    if value < 1000:
        return str(value)
    elif value < 10000:
        return "{0}{1}".format(int(value / 1000), '千')
    elif value < 100000000:
        return "{0}{1}".format(int(value / 10000), '万')
    else:
        return "{0}{1}".format(int(value / 100000000), '亿')
