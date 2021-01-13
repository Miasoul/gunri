import discord
import asyncio
import os
import datetime
from discord.ext import commands
from discord.utils import get


client = discord.Client()

@client.event
async def on_message(message):
    site = ['https','http']
    role = discord.utils.get(message.guild.roles, name = "링크")
    for i in site:
        if i in message.content:
            if message.author.guild_permissions.manage_channels:
                return
            elif role in message.author.roles:
                return
            else:
                await message.delete()  



acces_token = os.environ["BOT_TOKEN"]    
client.run(acces_token)    
