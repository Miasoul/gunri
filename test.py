import discord
import asyncio
import os
import datetime
from discord.ext import commands
from discord.utils import get


client = discord.Client()
client = commands.Bot(command_prefix="~")


@client.command()
async def ban(ctx, member : discord.Member, reason):
    channel = '792606160419029022'
    embed = discord.Embed(title="처리결과", description="", color=0x62c1cc)
    embed.add_field(name="이름",value=member.name)
    embed.add_field(name="사유",value=reason)
    embed.add_field(name="처벌",value="밴")
    await member.ban(reason = reason)
    await client.get_channel(int(channel)).send(embed=embed)
    await ctx.message.delete()

acces_token = os.environ["BOT_TOKEN"]    
client.run(acces_token)    
