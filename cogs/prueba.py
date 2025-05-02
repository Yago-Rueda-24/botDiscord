from discord.ext import commands
import discord
from discord.ext import commands
from discord import app_commands
import entorno

GUILD_ID = discord.Object(id = entorno.GUILD_ID)
class prueba(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="saludar")
    async def saludar(self,interaction: discord.Interaction):
        await interaction.response.send_message(f'¡Hola, {interaction.user.name}, estoy conectado y listo para el servicio')
        
    async def cog_load(self):
        #Registro de comnados en el arbol del cog actual
        self.bot.tree.add_command(self.saludar, guild=GUILD_ID)

# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(prueba(bot))