from channels.generic.websocket import AsyncJsonWebsocketConsumer


class AsyncNotificationConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()

        self.room_name = "notifications"
        await self.channel_layer.group_add(self.room_name, self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive_json(self, content, **kwargs):
        message_type = content.get("type", "message")
        message = content.get("message", "")

        if message_type == "chat_message":
            await self.handle_chat_message(message)
        elif message_type == "status_check":
            await self.send_json({"status": "ready"})

    async def handle_chat_message(self, message):
        await self.channel_layer.group_send(
            self.room_name,
            {
                "type": "chat.message",
                "message": message,
            },
        )

    async def chat_message(self, event):
        message = event["message"]
        await self.send_json({"message": message})
