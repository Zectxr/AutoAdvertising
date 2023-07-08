import sys
sys.path.insert(0, 'discord.py-self')
import discord
from discord.ext import commands

import json
import asyncio
import tracemalloc

tracemalloc.start()

with open('config/config.json') as f:
    config = json.load(f)
    token = config['token']
    prefix = config['prefix']
    channel_id = int(config['channel'])

bot = commands.Bot(command_prefix=prefix, self_bot=True)
looping = True  # Set looping to True by default

@bot.event
async def on_ready():
    print("=============================================")
    print(f"Logged in as {bot.user.name} ({bot.user.id})")
    print("=============================================")
    channel = bot.get_channel(channel_id)
    await loop_message(channel)

async def loop_message(channel):
    print("Looping started.")
    while looping:
        message = await channel.send("?clan XWbaftbvmk Global <:gold:413758059152670720><:diamond:413758091088232449> \n\n =========== SAVED #2023 =========== \n\n Join Saved #2023: The premier critical ops community to showcase your __clips, share lineups, and connect with awesome people__. Experience the ultimate gaming camaraderie now! \n __We are looking for:__ \n• Community \n • Mods \n • Partnership \n\n __We offer:__ \n • giveaway \n • Host room \n • Inner Scrim (to improve your skills and awareness) \n ")
        print(f"Message sent: {channel_id}")
        await asyncio.sleep(3600)
    print("Looping stopped.")

bot.run(token)
