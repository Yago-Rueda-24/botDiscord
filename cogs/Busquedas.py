import discord
from time import sleep
from random import randint
import requests
import json
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
    
    @app_commands.command(name="magic",description="Busca una carta de magic the gathering por su nombre")
    async def magic_search(self,interaction: discord.Interaction, message: str):
        url = f"https://api.scryfall.com/cards/named?fuzzy={message}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            card_name = data['name']
            card_image = data['image_uris']['normal']
            card_set = data['set_name']
            card_type = data['type_line']
            card_text = data['oracle_text']
            embed = discord.Embed(title=card_name, description=f"Set: {card_set}\nType: {card_type}\nText: {card_text}")
            embed.set_image(url=card_image)
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message(f'No se encontró la carta: {message}')

    async def cog_load(self):
       self.bot.tree.add_command(self.google_search, guild=GUILD_ID)
       self.bot.tree.add_command(self.magic_search, guild=GUILD_ID)

    
# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(busquedas(bot))