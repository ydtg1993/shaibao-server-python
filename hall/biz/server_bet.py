from hall.models.hall import HallBetOption
from three_server.enums.dice_type import DiceLabel


def get_bets(hall_id):
    return [{
        'id': bet['id'],
        'position': bet['position'],
        'dice_type': DiceLabel[bet['dice_type']].value,
        'odds': bet['odds'],
        'active': bet['active']
    } for bet in HallBetOption.find_by_hall_id(hall_id)]
