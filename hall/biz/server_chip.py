from hall.models.hall import HallChipOption


def get_chips(hall_id):
    return [{
        'id': bet['id'],
        'position': bet['position'],
        'value': bet['value'],
        'active': bet['active']
    } for bet in HallChipOption.find_by_hall_id(hall_id)]
