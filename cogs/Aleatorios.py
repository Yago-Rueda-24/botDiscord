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
    @app_commands.command(name="dado",description="Lanza un dado de n caras y anuncia el resultado")       
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
    @app_commands.command(name="ruleta",description="Lanza la ruleta y anuncia el resultado")
    async def ruleta(self,interaction: discord.Interaction):
        # Números rojos en la ruleta europea
        rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18,
         19, 21, 23, 25, 27, 30, 32, 34, 36]
        
        resultado = randint(0,36)
        if resultado == 0:
            embed = discord.Embed(
            title="Resultado de la ruleta",
            description="El resultado de la ruleta es: 0",
            color=discord.Color.green()
            )
            await interaction.response.send_message(embed=embed)
        else:
            # Determinar la paridad
            if resultado % 2 == 0:
                paridad = "par"
            else:
             paridad = "impar"
            # Determinar el color
            if resultado in rojos:
                color = "rojo"
            else:
                color = "negro"

            embed = discord.Embed(
            title="Resultado de la ruleta",
            description=f"El resultado de la ruleta es: {resultado}", 
            color=discord.Color.red() if color == "rojo" else discord.Color.dark_grey()

            )
            embed.add_field(name="El número es {paridad}",inline=False)
            embed.add_field(name="El color es {color}",inline=False)
            await interaction.response.send_message(embed=embed)


    async def cog_load(self):
        #Registro de comnados en el arbol del cog actual
        self.bot.tree.add_command(self.moneda, guild=GUILD_ID)
        self.bot.tree.add_command(self.dado, guild=GUILD_ID)    
        self.bot.tree.add_command(self.ruleta, guild=GUILD_ID)

# Añadir el cog al bot
async def setup(bot):
    await bot.add_cog(prueba(bot))