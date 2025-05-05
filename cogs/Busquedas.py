import discord
from time import sleep
from random import randint
from discord.ext import commands
from discord.ext import commands
from discord import app_commands
from google import genai
import entorno

GEMINI_KEY = entorno.GEMINI_KEY
GUILD_ID = discord.Object(id = entorno.GUILD_ID)
client = genai.Client(api_key=GEMINI_KEY)
class busquedas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="gemini",description="Realiza una busqueda en usando el LLM de Google")
    async def google_search(self,interaction: discord.Interaction, message: str):
        response =client.models.generate_content(model="gemini-2.0-flash", contents=message)
        await interaction.response.send_message(f'Buscando en Google: {response.text}')

    async def cog_load(self):
       self.bot.tree.add_command(self.google_search, guild=GUILD_ID)

    
# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(busquedas(bot))