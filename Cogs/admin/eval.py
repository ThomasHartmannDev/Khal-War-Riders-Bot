import discord
from discord.ext import commands

class Eval(commands.Cog):
    def __init__(self, hart):
        self.hart = hart

    @commands.command(name='eval')
    async def _eval(self, ctx, *, query):
        if not ctx.author.id in self.hart.config['ownerId']: return
        try:
            if 'await ' in query:
                query = query.replace('await ', '')
                await ctx.send(await eval(query))
            else:
                await ctx.send(eval(query))
        except Exception as e:
            await ctx.send(e)
        
def setup(hart):
    hart.add_cog(Eval(hart))