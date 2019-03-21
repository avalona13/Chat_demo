import asyncio
import json
from django.contrib.auth.models import User
from django.utils import timezone
from channels.db import database_sync_to_async
from channels.consumer import AsyncConsumer
from .models import Message


class MessageConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        await self.send({
            'type': 'websocket.accept'
            })
        await self.channel_layer.group_add(
            'mainchat',
            self.channel_name
        )

    async def websocket_receive(self, event):
        new_message_data = event.get('text')
        new_message = json.loads(new_message_data)
        author = new_message['author']
        message_time = (timezone.now()).strftime('%Y-%m-%d %H:%M:%S')
        message_text = new_message['message_text']
        await self.create_message(author, message_text)
        message = {
            'message_text': message_text,
            'author': author,
            'message_time': message_time,
         }
        await self.channel_layer.group_send(
            'mainchat',
            {
                'type': 'show_message',
                'text': json.dumps(message)
            }
        )
        await asyncio.sleep(0.01)

    @database_sync_to_async
    def create_message(self, author, message_text):
        author = User.objects.get(username=author)
        Message.objects.create(author=author, message_text=message_text, was_read=False)

    async def show_message(self, event):
        await self.send({
            'type': 'websocket.send',
            'text': event['text']
        })
