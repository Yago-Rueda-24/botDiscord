import discord
from time import sleep
from random import randint
from discord.ext import commands
from discord.ext import commands
from discord import app_commands
from google import genai
import entorno

GUILD_ID = discord.Object(id = entorno.GUILD_ID)
class busquedas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @app_commands.command(name="busqueda",description="Realiza una busqueda en google")
    async def google_search(self,interaction: discord.Interaction, message: str):
        
        await interaction.response.send_message(f'Buscando en Google: {message}')

    async def cog_load(self):
        #Registro de comnados en el arbol del cog actual
        return

# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(busquedas(bot))