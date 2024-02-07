import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Room, Message
from authentication.models import CustomUser as User

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

        # Send existing messages when a new user connects
        self.send_existing_messages()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = self.scope["user"].username

        # Save message to database
        self.save_message(username, self.room_name, message)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.message", "message": message, "username": username}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]
        username = event["username"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message, "username": username}))

    def save_message(self, username, room_slug, message):
        user = User.objects.get(username=username)
        room = Room.objects.get(slug__contains=username)
        
        Message.objects.create(user=user, room=room, content=message)

    def send_existing_messages(self):
        # Fetch existing messages from the database
        room = Room.objects.get(slug__contains=self.room_name)
        messages = Message.objects.filter(room=room).order_by('date_added')

        # Send existing messages to the WebSocket
        for message in messages:
            self.send(text_data=json.dumps({
                "message": message.content,
                "username": message.user.username
            }))
