import re
import discord
from discord.ext import commands
from discord import Message, Forbidden
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

cor = 0xFF0000


class cotacao(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='test')
    async def test(self, ctx):
        bnz_price = cg.get_price(ids="benzene", vs_currencies = ['usd', 'brl'])
        ada_price = cg.get_price(ids="Cardano", vs_currencies = ['usd', 'brl'])
        slp_price = cg.get_price(ids="smooth-love-potion", vs_currencies = ['usd', 'brl'])
        bzn_usd = bnz_price['benzene']['usd']
        bzn_brl = bnz_price['benzene']['brl']
        slp_usd = slp_price['smooth-love-potion']['usd']
        slp_brl = slp_price['smooth-love-potion']['brl']
        embed = discord.Embed() \
            .set_author(name="Cotação BZN",
                        icon_url="https://i.imgur.com/1sj9bou.png") \
            .add_field(name=":flag_us: 1 BZN",
                       value=f'**Dolar:** {bzn_usd}',
                       inline=False) \
            .add_field(name=":flag_br: 1 BZN",
                       value=f'**Real:** {bzn_brl}',
                       inline=False) \
            .set_footer(text="Benzene",
                        icon_url="https://i.imgur.com/1sj9bou.png")


        channel = self.bot.get_channel(855106908461203468)     
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(cotacao(bot))