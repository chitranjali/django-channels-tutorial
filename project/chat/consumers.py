from channels.generic.websocket import AsyncJsonWebsocketConsumer
import json

class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % room_name
        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name)

    async def receive_json(self, data):
        data['type'] = 'chat_message'
        await self.channel_layer.group_send(self.room_group_name, data)

    async def chat_message(self, data):
        del data['type']
        await self.send_json(data)
