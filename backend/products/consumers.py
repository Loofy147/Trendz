import json
from channels.generic.websocket import AsyncWebsocketConsumer


class PriceUpdateConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("price_updates", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("price_updates", self.channel_name)

    async def price_update(self, event):
        await self.send(
            text_data=json.dumps(
                {
                    "type": "price_update",
                    "product_id": event["product_id"],
                    "new_price": event["new_price"],
                    "change": event["change"],
                }
            )
        )
