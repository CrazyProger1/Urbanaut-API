from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.conf import settings
from django.contrib.auth.models import AnonymousUser

from src.apps.accounts.models import User


class AsyncUserConsumer(AsyncJsonWebsocketConsumer):

    async def join_groups(self, user: User):
        for room in settings.WEBSOCKET_COMMON_GROUPS:
            await self.channel_layer.group_add(room, self.channel_name)

        await self.channel_layer.group_add(settings.WEBSOCKET_USER_GROUP.format(id=user.id), self.channel_name)

    async def leave_groups(self, user: User):
        for room in settings.WEBSOCKET_COMMON_GROUPS:
            await self.channel_layer.group_discard(room, self.channel_name)

        await self.channel_layer.group_discard(settings.WEBSOCKET_USER_GROUP.format(id=user.id), self.channel_name)

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

    async def send_event(self, event):
        event_type = event.pop("event", None)
        event_data = event.pop("data", None)

        if event_type:
            await self.send_json(
                {
                    "type": event_type,
                    "data": event_data,
                }
            )
