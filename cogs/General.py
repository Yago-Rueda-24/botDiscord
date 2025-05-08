import discord
from time import sleep
from random import randint
from discord.ext import commands
from discord.ext import commands
from discord import app_commands
import entorno

GUILD_ID = discord.Object(id = entorno.GUILD_ID)
class general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Función para que el bot salude al usuario
    @app_commands.command(name="hola", description="Saluda al bot")
    async def hola(self,interaction: discord.Interaction):
        await interaction.response.send_message(f'¡Hola, {interaction.user.name}, estoy conectado y listo para el servicio')
    
    #Función que repite el mensaje del usuario
    @app_commands.command(name="decir", description="Digo lo que me mandes")
    async def decir(self,interaction: discord.Interaction,message:str):
        await interaction.response.send_message(message)
        
    async def cog_load(self):
        #Registro de comnados en el arbol del cog actual
        self.bot.tree.add_command(self.hola, guild=GUILD_ID)
        self.bot.tree.add_command(self.decir, guild=GUILD_ID)

# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(general(bot))