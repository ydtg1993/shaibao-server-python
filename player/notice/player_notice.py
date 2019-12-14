from notice.biz.notice import notice_player
from player.enums.notice_event import NoticeEvent
from system.cache.channel_name import get_channel_name


def update_player_info(player):
    """
    @api {post} /UpdatePlayerInfoNotice 更新用户信息通知
    @apiVersion 1.0.0
    @apiName UpdatePlayerInfoNotice
    @apiGroup WebSocket-Notice
    @apiSuccessExample {json} 通知样例:
    {
        "hall_tag": "Hall",
        "event": "UpdatePlayerInfoNotice",
        "data": {
            "name": "苹果",
            "phone": "18009230222",
            "gold": 1023,
        }
    }
    """
    print(player.token)
    print('/////////////////////////////////')
    print(get_channel_name(player.token))
    print('/////////////////////////////////')
    notice_player(get_channel_name(player.token), "Hall", NoticeEvent.UpdatePlayerInfoNotice.value, {
        'name': player.name,
        'phone': player.phone,
        'gold': str(player.gold)
    })
