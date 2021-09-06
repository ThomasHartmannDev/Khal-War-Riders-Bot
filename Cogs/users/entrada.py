import discord
from discord.ext import commands
from pymongo.collection import Collection
from datetime import datetime, timezone, timedelta

class Entrada(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def entrada(self, ctx):
        now = datetime.utcnow()

        horarios: Collection = self.bot.db['horarios']
        
        try:
            horarios.insert_one({
                '_id': ctx.author.id,
                'horario': now,
            })
        except:
            return await ctx.send("Você já registrou seu horario!")
            
        embed = discord.Embed() \
            .set_author(name="Event Log",
                        icon_url="https://i.imgur.com/1sj9bou.png") \
            .add_field(name="Você registrou o seu horario!!",
                       value=f'⠀⠀⠀⠀⠀',
                       inline=False) 
        return await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Entrada(bot))
