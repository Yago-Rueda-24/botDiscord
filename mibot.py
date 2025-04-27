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

    if message.content.startswith('$hola'):
        await message.channel.send('Hola, estoy conectado y listo para el servicio')
    if message.content.startswith('$help'):
        lista =['$hola: Saludar al bot','$help: Imprimir la ayuda de comandos del bot']
        await message.channel.send('\n'.join(lista))
        
client.run(entorno.TOKEN)