import botpy
import os
from botpy.message import Message
from botpy.channel import Channel
from botpy.ext.cog_yaml import read
test_config = read("./config2.yaml")

class MyClient(botpy.Client):
    async def on_at_message_create(self, message: Message):
        try:
            # await self.api.mute_all(guild_id=message.guild_id, mute_seconds="1000")
            # await self.api.mute_member(guild_id=message.guild_id, user_id="13564051022262235489",  mute_seconds="10")
            members = await self.api.get_guild_members(message.guild_id, limit=10)
            print(members)
            for member in members:
                if member['nick']=="白瞎子":
                    await message.reply(content=f"昵称:{member['nick']},user_id:{member['user']['id']}")
                    break
            # await self.api.get_delete_member(
            #     guild_id=message.guild_id,
            #     user_id=member['user']['id'],
            #     add_blacklist=False,
            #     delete_history_msg_days=0
            # )
            await self.api.mute_all(message.guild_id,mute_seconds='11000')
            # await self.api.mute_all(guild_id, mute_seconds="100")

        except:
            # await self.api.post_message(message.channel_id, content=f"{message.author}权限不足！请赋予禁言权限！")
            await message.reply(content='权限不足！')
intents = botpy.Intents(public_guild_messages=True)
client = MyClient(intents=intents)
client.run(appid=test_config["appid"], token=test_config["token"])