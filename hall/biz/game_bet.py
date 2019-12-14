from hall.models.hall import HallBetOption
from three_server.enums.dice_type import DiceLabel


def get_bets(hall_id):
    """
    查询下注选项
    :param hall_id: 大厅ID
    :return: Array
    """

    return [{
        'id': bet['id'],
        'position': bet['position'],
        'dice_type': DiceLabel[bet['dice_type']].value,
        'odds': bet['odds'],
        'active': bet['active']
    } for bet in HallBetOption.find_by_hall_id(hall_id)]


def check_bet(hall_id, bet_type):
    """
    检查下注类型
    :param hall_id: 大厅ID
    :param bet_type: 下注类型
    :return: Boolean,
    """
    for bet in HallBetOption.find_by_hall_id(hall_id):
        if bet['dice_type'] == bet_type:
            return True, bet['odds']
    return False, None
