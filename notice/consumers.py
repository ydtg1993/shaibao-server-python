import json
from player.biz.client_player import auth_token
from system.cache.channel_name import set_channel_name, get_player_token, del_channel_name
from channels.generic.websocket import AsyncWebsocketConsumer
from notice.enums.connection_code import ConnectionCode
from notice.api_router import router
import logging

log = logging.getLogger('game')


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        """
        @api {get} ws://10.10.13.153:8000/ws/three/<player_token> WebSocket 连接
        @apiVersion 1.0.0
        @apiName WebSocket 连接
        @apiGroup WebSocket-Connection
        """
        self.room_group_name = 'hall'
        user_token = self.scope['url_route']['kwargs']['user_token']
        set_channel_name(user_token, self.channel_name)
        await self.accept()
        if not auth_token(user_token):
            await self.close(code=ConnectionCode.VerificationFailed.value)
        else:
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )

    async def disconnect(self, close_code):
        # 重置Token
        player_token = get_player_token(self.channel_name)
        # reset_token(token)
        # Leave room group
        del_channel_name(player_token, self.channel_name)
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        log.info('>////////////////[' + '接收消息' + ']////////////////<')
        log.info(text_data)
        log.info(bytes_data)
        params = bytes_data.decode()
        log.info(params)
        data_json = json.loads(params)
        message = data_json['event']
        result = router[message](self.channel_name, **data_json['data'])
        if result is not None:
            await self.channel_layer.send(
                self.channel_name,
                {
                    'type': 'chat_message',
                    'data': result
                }
            )
        log.info('>/////////////////////////////////////////////////<')

    async def chat_message(self, structs):
        from game.enums.notice_event import NoticeEventMsg
        log.info('>////////////////[' + NoticeEventMsg[structs['data']['event']].value + ']////////////////<')
        msg = structs['data']
        log.info(msg)
        body = json.dumps(msg).encode('utf-8')
        # tx_msg = '%s%s%s' % ('STX', json.dumps(msg), 'ETX')
        # body = tx_msg.encode('utf-8')
        # log.info(body)
        log.info('>/////////////////////////////////////////////////<')
        await self.send(bytes_data=body)

    async def push_message(self, structs):
        from game.enums.notice_event import NoticeEventMsg
        log.info('>////////////////[' + NoticeEventMsg[structs['event']].value + ']////////////////<')
        msg = {
            "hall_tag": structs['hall_tag'],
            "event": structs['event'],
            "data": structs['data']
        }
        log.info(msg)
        body = json.dumps(msg).encode('utf-8')
        # tx_msg = '%s%s%s' % ('STX', json.dumps(msg), 'ETX')
        # body = tx_msg.encode('utf-8')
        # log.info(body)
        log.info('>/////////////////////////////////////////////////<')
        await self.send(bytes_data=body)
