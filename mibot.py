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
GUILD_ID = discord.Object(id = 1365653490055254038)
client = commands.Bot(command_prefix='$', intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    try:
        synced = await client.tree.sync(guild=GUILD_ID)  
        print(f'Slash Commands sincronizados: {len(synced)}')
    except Exception as e:
        print(f'Error al sincronizar Slash Commands: {e}')

@client.tree.command(name="hola", description="Saluda al bot", guild=GUILD_ID)
async def hola(interaction: discord.Interaction):
    await interaction.response.send_message(f'¡Hola, {interaction.user.name}, estoy conectado y listo para el servicio')
    
@client.tree.command(name="help", description="Muestra la ayuda del bot", guild=GUILD_ID)
async def help(interaction: discord.Interaction):
    embed = discord.Embed(
            title="Lista de Comandos",
            description="Aquí tienes los comandos que puedes usar:",
            color=discord.Color.green()
    )
    embed.add_field(name="/hola", value="Saludar al bot.", inline=False)
    embed.add_field(name="/help", value="Mostrar este mensaje de ayuda.", inline=False)
    embed.add_field(name="/decir", value="Repite el mensaje que le digas", inline=False)
    embed.set_footer(text="Si necesitas ayuda con algun comando, escribelo sin argumentos para que este te de la ayuda")
        
    await interaction.response.send_message(embed=embed)
    
@client.tree.command(name="decir", description="Digo lo que me mandes", guild=GUILD_ID)
async def help(interaction: discord.Interaction,message:str):
        
    await interaction.response.send_message(message)
                
client.run(entorno.TOKEN)