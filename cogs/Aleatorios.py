import discord
from time import sleep
from random import randint
from discord.ext import commands
from discord.ext import commands
from discord import app_commands
import entorno

GUILD_ID = discord.Object(id = entorno.GUILD_ID)
class prueba(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="moneda",description="Lanza una moneda y anuncia el resultado")
    async def moneda(self,interaction: discord.Interaction):
        if(randint(0,1)==0):
            await interaction.response.send_message(f'Ha salido: CRUZ')
        else:
            await interaction.response.send_message(f'Ha salido: CARA')
            
    async def dado(self,interaction: discord.Interaction,message:str):
        caras = int(message)
        if caras.isnumeric() == False:
            await interaction.response.send_message(f'El parametro introducido no es un numero')
        else:
            if caras < 3:
                await interaction.response.send_message(f'El dado no puede tener menos de 3 caras')
            else:
                resultado = randint(1,caras)
                await interaction.response.send_message(f'El resultado del dado de un d{caras} es: {resultado}')
        
    async def cog_load(self):
        #Registro de comnados en el arbol del cog actual
        self.bot.tree.add_command(self.moneda, guild=GUILD_ID)

# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(prueba(bot))