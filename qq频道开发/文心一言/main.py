# -*- coding: utf-8 -*-
import asyncio
import os

import botpy
from botpy import logging
from botpy.ext.cog_yaml import read
from botpy.message import Message
import reply
test_config = read(os.path.join(os.path.dirname(__file__), "config/config3.yaml"))

_log = logging.get_logger()


class MyClient(botpy.Client):
    async def on_ready(self):
        _log.info(f"robot 「{self.robot.name}」 on_ready!")

    async def on_at_message_create(self, message: Message):
        _log.info(message.author.avatar)
        _log.info(message.author.username)
        print(message.mentions[0].id)
        print(message.content)
        id = len(str(message.mentions[0].id))+5
        print(id)
        content = message.content[id::]
        answer = reply.reply(content)
        await self.api.post_message(channel_id=message.channel_id, content=answer, msg_id=message.id)


if __name__ == "__main__":
    # 通过预设置的类型，设置需要监听的事件通道
    # intents = botpy.Intents.none()
    # intents.public_guild_messages=True

    # 通过kwargs，设置需要监听的事件通道
    intents = botpy.Intents.all()
    client = MyClient(intents=intents)
    client.run(appid=test_config["appid"], token=test_config["token"])
