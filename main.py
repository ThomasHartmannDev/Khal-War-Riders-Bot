import json
import discord
import traceback
import asyncio
from discord.ext import commands
import itertools
import pymongo
from pymongo import *
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

def prefix_format(prefixes):
    formatted = []
    for prefix in prefixes:
        for fprefix in map(''.join, itertools.product(*zip(prefix.upper(), prefix.lower()))):
            if not fprefix in formatted:
                formatted.append(fprefix)
    return formatted


if __name__ == "__main__":
    #dev_mode = input("Abrir em modo desensolvedor?(Sim = 1 | Não = 0) ")
    #config_file = 'config_dev.json' if dev_mode == '1' else 'config.json'
    config_file = 'secret.json'
    with open(f'./data/{config_file}') as config:
        config = json.load(config)

    bot = commands.Bot(command_prefix=prefix_format(
        config['prefixes']), case_insensitive=True, help_command=None)
    bot.config = config
    bot.db = pymongo.MongoClient(config['mongoURL'])['KhalBotWarRiders']

    @bot.event
    async def on_ready():
        print('Logado com sucesso :D')
        
        await bot.change_presence(activity=discord.Game(name=''), status=discord.Status.online)
        while not bot.is_closed():
            bnz_price = cg.get_price(ids="benzene", vs_currencies = ['usd', 'brl'])
            slp_price = cg.get_price(ids="smooth-love-potion", vs_currencies = ['usd', 'brl'])
            bzn_usd = bnz_price['benzene']['usd']
            bzn_brl = bnz_price['benzene']['brl']
            slp_usd = slp_price['smooth-love-potion']['usd']
            slp_brl = slp_price['smooth-love-potion']['brl']
            bzn_embed = discord.Embed() \
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

            slp_embed = discord.Embed() \
            .set_author(name="Cotação SLP",
                        icon_url="https://i.imgur.com/ySbo5n8.png") \
            .add_field(name=":flag_us: 1 SLP",
                       value=f'**Dolar:** {slp_usd}',
                       inline=False) \
            .add_field(name=":flag_br: 1 SLP",
                       value=f'**Real:** {slp_brl}',
                       inline=False) \
            .set_footer(text="Smooth Love Potions",
                        icon_url="https://i.imgur.com/ySbo5n8.png") \
            
            channel_bzn = bot.get_channel(881386157064204328)
            channel_slp = bot.get_channel(881387064740941905)         
            await channel_bzn.send(embed=bzn_embed)
            await channel_slp.send(embed=slp_embed)
            await asyncio.sleep(1800)
        

        
    for ext in config['ext']:
        try:
            bot.load_extension('Cogs.' + ext)
            print('cogs.' + ext + ' carregado com sucesso')
        except Exception as error:
            traceback.print_exception(Exception, error, None)
            print(f'\n')

    bot.run(config['token'])
