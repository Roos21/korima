# consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User
from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.sender = self.scope['user']
        self.receiver_id = self.scope['url_route']['kwargs']['receiver_id']
        self.receiver = await self.get_receiver()

        self.room_name = f"chat_{self.sender.id}_{self.receiver.id}"
        self.room_group_name = f"chat_{self.sender.id}_{self.receiver.id}_group"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.save_message(message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender_id': self.sender.id,
                'receiver_id': self.receiver.id
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender_id = event['sender_id']
        receiver_id = event['receiver_id']

        await self.send(text_data=json.dumps({
            'message': message,
            'sender_id': sender_id,
            'receiver_id': receiver_id
        }))

    async def get_receiver(self):
        try:
            receiver = User.objects.get(id=self.receiver_id)
            return receiver
        except User.DoesNotExist:
            return None

    async def save_message(self, message):
        Message.objects.create(sender=self.sender, receiver=self.receiver, content=message)