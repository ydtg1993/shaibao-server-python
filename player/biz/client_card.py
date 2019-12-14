from player.models.card import Card


def create(params):
    Card.create_card(**params)


def player_card(player_id):
    ls = Card.find_by_player(player_id)
    if len(ls) == 0:
        return {}
    return {
        "name": ls[0]['name'],
        "number": ls[0]['number'],
        # "bank_name": ls[0]['bank__name'],
        "bank_id": str(ls[0]['bank__id']),
        "bank_branch": ls[0]['bank_branch'],
    }
