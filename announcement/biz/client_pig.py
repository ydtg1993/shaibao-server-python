from announcement.model.pig import PigRecord
from player.models.player import Player
from system.models.keyValue import KeyValue
from system.enums.keyValue import Keys
import random
from player.notice.player_notice import update_player_info


def pig_info():
    """
    查看金猪详情
    :return: map
    """
    return {
        'total': KeyValue.get_value(Keys.GOLDEN_PIG.value),
        'record': [{
            'player': d['player__name'],
            'gold': d['gold'],
        } for d in PigRecord.client_search()]
    }


def pig_open(player_id, token):
    """
    开奖
    :return: gold
    """
    gold = random.randint(1, 50)
    Player.update_player_integral(token, -500)
    ok, player = Player.update_player_gold(token, gold, gold)
    value = int(KeyValue.get_value(Keys.GOLDEN_PIG.value))
    KeyValue.update_value(Keys.GOLDEN_PIG.value, (value - 1))
    PigRecord.create(player_id=player_id, gold=gold)
    update_player_info(player)
    return gold
