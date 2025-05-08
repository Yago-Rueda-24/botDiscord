import discord
import os
import asyncio
import requests
import entorno
from discord.ext import commands
from discord import app_commands


intents = discord.Intents.default()
intents.message_content = True
GUILD_ID = discord.Object(id = entorno.GUILD_ID)
client = commands.Bot(command_prefix='$', intents=intents)

#Evento que se ejecuta cuando el bot esta iniciado
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    try:
        # Llamada para cargar todos los cogs
        await load_cogs()
        # LLamada para sincronizar todos los comandos en el bot del server con id = GUILD_ID
        synced = await client.tree.sync(guild=GUILD_ID)  
        print(f'Slash Commands sincronizados: {len(synced)}')
    except Exception as e:
        print(f'Error al sincronizar Slash Commands: {e}')

@client.tree.command(name="ayuda", description="Muestra la ayuda del bot", guild=GUILD_ID)
async def ayuda(interaction: discord.Interaction):
    embed = discord.Embed(
            title="Lista de Comandos",
            description="Aquí tienes los comandos que puedes usar:",
            color=discord.Color.green()
    )
    for command in client.tree.get_commands():
        embed.add_field(name=f"/{command.name}", value=command.description, inline=False)
        
    embed.set_footer(text="Si necesitas ayuda con algun comando, escribelo sin argumentos para que este te de la ayuda")
        
    await interaction.response.send_message(embed=embed)

# Función que añade todos los cogs al bot
async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f'cogs.{filename[:-3]}')
                
client.run(entorno.TOKEN)