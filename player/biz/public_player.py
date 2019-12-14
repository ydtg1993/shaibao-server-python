from player.models.player import Player
import decimal


def update_player_gold(token, value, lock_gold=0):
    """
    更新玩家金币
    :param lock_gold:
    :param token: 玩家Token
    :param value: 变动金额
    :return: Boolean
    """
    return Player.update_player_gold(token, value, lock_gold)


def check_player_gold(token, value):
    """
    检查玩家金币
    :param token: 玩家Token
    :param value: 变动金额
    :return: Boolean
    """
    ok, gold = Player.get_player_gold(token)
    if not ok or decimal.Decimal(value) > gold:
        return False
    return True


