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
        embed = discord.Embed(
            title="Lista de Comandos",
            description="Aquí tienes los comandos que puedes usar:",
            color=discord.Color.green()
        )
        embed.add_field(name="$hola", value="Saludar al bot.", inline=False)
        embed.add_field(name="$help", value="Mostrar este mensaje de ayuda.", inline=False)
        embed.set_footer(text="Si necesitas ayuda con algun comando, escribelo sin argumentos para que este te de la ayuda")
        await message.channel.send(embed=embed)
        
client.run(entorno.TOKEN)