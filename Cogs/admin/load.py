import discord
from discord.ext import commands


class Load(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='load')
    async def load(self, ctx, cog_ca: str = None):
        await ctx.send(ctx.author.id)
        if cog_ca is None:
            cog_ca_e = discord.Embed(
                description="Digite Uma Cog para eu carregar")
            await ctx.send(embed=cog_ca_e)
        else:
            try:
                self.bot.load_extension('Cogs.' + cog_ca)
                await ctx.send(f"Cog [{cog_ca}] Carregada !!!")
            except Exception as ex:
                await ctx.send(f"Ocorreu um erro ao carregar a Cog `{cog_ca}`: {ex}")

    @commands.command(name='unload')
    async def unload(self, ctx, cog_ca: str = None):
        await ctx.send(ctx.author.id)
        if cog_ca is None:
            cog_ca_e = discord.Embed(
                description="Digite Uma Cog para eu descarregar")
            await ctx.send(embed=cog_ca_e)
        else:
            try:
                self.bot.unload_extension('Cogs.' + cog_ca)
                await ctx.send(f"Cog [{cog_ca}] Descarregada !!!")
            except Exception as ex:
                await ctx.send(f"Ocorreu um erro ao descarregar a Cog `{cog_ca}`: {ex}")

    @commands.command(name='reload')
    async def reload(self, ctx, cog_ca: str = None):
        await ctx.send(ctx.author.id)
        if cog_ca is None:
            cog_ca_e = discord.Embed(
                description="Digite Uma Cog para eu recarregar")
            await ctx.send(embed=cog_ca_e)
        else:
            try:
                self.bot.unload_extension('Cogs.' + cog_ca)
                self.bot.load_extension('Cogs.' + cog_ca)
                await ctx.send(f"Cog [{cog_ca}] Recarregada !!!")
            except Exception as ex:
                await ctx.send(f"Ocorreu um erro ao recarregar a Cog `{cog_ca}`: {ex}")


def setup(bot):
    bot.add_cog(Load(bot))
