import discord
import os
import asyncio
import requests
import entorno
from discord.ext import commands
from discord import app_commands


import discord


intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='$', intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        
client.run(entorno.TOKEN)