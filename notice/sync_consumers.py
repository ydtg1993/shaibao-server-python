from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from system.cache.channel_name import set_channel_name, get_channel_name
from player.biz.client_player import auth_token, reset_token


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        user_token = self.scope['url_route']['kwargs']['user_token']
        self.room_group_name = 'hall'

        set_channel_name(user_token, self.channel_name)

        if not auth_token(user_token):
            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name,
                self.channel_name
            )
            self.accept()
            # async_to_sync(self.channel_layer.group_send)(
            #     self.room_group_name,
            #     {
            #         'type': 'chat_message',
            #         'message': 'token过期'
            #     }
            # )
            self.close(code=3002)
        else:
            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name,
                self.channel_name
            )
            self.accept()

    def disconnect(self, close_code):
        # print('close_code', close_code)
        token = get_channel_name
        reset_token(str(token).split('_')[1])
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))

    def push_message(self, structs):
        message = structs['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))