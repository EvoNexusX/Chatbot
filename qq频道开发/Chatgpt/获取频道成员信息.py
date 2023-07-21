import time

import qqbot

import botpy

from botpy.message import Message
import os
from botpy.message import Message
from botpy.ext.cog_yaml import read
test_config = read("./config2.yaml")

class MyClient(botpy.Client):
    async def on_at_message_create(self, message: Message):

        # await self.api.mute_all(guild_id=message.guild_id, mute_seconds="1000")
        members = await self.api.get_guild_members(message.guild_id,limit=10)
        # print(member,)

        for member in members:
            print(member['nick'])
            if member['nick']=="白瞎子":
                a = await self.api.create_dms(guild_id=message.guild_id, user_id=member['user']['id'])
                print(a['guild_id'],message.guild_id)
                await self.api.post_dms(guild_id=a['guild_id'],content='test')
                await message.reply(content=f"昵称:{member['nick']},user_id:{member['user']['id']}")
            # print(111)
            # if member["nick"]=="频道助手":


        # await self.api.post_message(message.channel_id, content=f"{1}")

intents = botpy.Intents.all()
client = MyClient(intents=intents)
client.run(appid=test_config["appid"], token=test_config["token"])
