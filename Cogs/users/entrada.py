import pytz
import discord
from discord.colour import Color, Colour
from discord.ext import commands
from pymongo.collection import Collection
from datetime import date, datetime

class Entrada(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def entrada(self, ctx):
        now = datetime.utcnow().astimezone(pytz.timezone("America/Sao_Paulo"))

        horarios: Collection = self.bot.db['horarios']
        
        try:
            horarios.insert_one({
                '_id': ctx.author.id,
                'horario': now,
            })
        except:
            await ctx.send("Você já bateu seu ponto hoje!")
            
        embed = discord.Embed() \
            .set_author(name="Bate ponto",
                        icon_url="https://i.imgur.com/1sj9bou.png") \
            .add_field(name="Você bateu o ponto!!",
                       value=f'⠀⠀⠀⠀⠀',
                       inline=False) 
        return await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Entrada(bot))
