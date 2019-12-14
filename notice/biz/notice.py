from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import logging

log = logging.getLogger('game')
group_name = 'hall'


def notice_group(hall_tag, event, data):
    log.info('------------------------' + event + '------------------------')
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        group_name,
        {
            'type': "push.message",
            'hall_tag': hall_tag,
            'event': event,
            'data': data
        }
    )


def notice_player(player_name, hall_tag, event, data):
    log.info('------------------------' + event + '------------------------')
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.send)(
        player_name,
        {
            'type': "push.message",
            'hall_tag': hall_tag,
            'event': event,
            'data': data
        }
    )


def test_notice_player(player_name, hall_tag, event, data):
    channel_layer = get_channel_layer()
    print(player_name, event)
    channel_layer.group_send(
        group_name,
        {
            'type': "push.message",
            'hall_tag': hall_tag,
            'event': event,
            'data': data
        }
    )
