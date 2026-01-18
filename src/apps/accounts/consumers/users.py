from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.contrib.auth.models import AnonymousUser

from src.apps.accounts.models import User


class AsyncUserConsumer(AsyncJsonWebsocketConsumer):
    COMMON_ROOMS = ("system",)

    async def join_groups(self, user: User):
        for room in self.COMMON_ROOMS:
            await self.channel_layer.group_add(room, self.channel_name)

        await self.channel_layer.group_add(f"user_{user.id}", self.channel_name)

    async def leave_groups(self, user: User):
        for room in self.COMMON_ROOMS:
            await self.channel_layer.group_discard(room, self.channel_name)

        await self.channel_layer.group_discard(f"user_{user.id}", self.channel_name)

    def get_user(self) -> User | AnonymousUser:
        return self.scope["user"]

    def should_close(self, user: User) -> bool:
        return not user.is_authenticated or not user.is_active

    async def connect(self):
        await self.accept()

        user = self.get_user()

        if self.should_close(user=user):
            await self.close()

        await self.join_groups(user=user)

    async def disconnect(self, close_code):
        user = self.get_user()
        await self.leave_groups(user=user)

    async def send_notification(self, event):
        notification = event["notification"]
        await self.send_json(notification)
