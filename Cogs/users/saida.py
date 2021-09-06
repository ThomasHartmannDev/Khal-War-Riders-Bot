import pytz
import discord
from discord.ext import commands
from pymongo.collection import Collection
from datetime import datetime, timedelta


class Saida(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def saida(self, ctx):

        horarios: Collection = self.bot.db['horarios']

        horario = horarios.find_one({'_id': ctx.author.id})

        if horario:
            horarios.delete_one({'_id': ctx.author.id})
            horario = horario['horario']

            now = datetime.utcnow().astimezone(pytz.timezone("America/Sao_Paulo"))
            diff: timedelta = now - horario
            time = ''
            times = []
            hours, seconds = map(int, divmod(diff.total_seconds(), 3600))
            minutes, seconds = map(int, divmod(seconds, 60))

            if hours > 0:
                times.append(s(hours, 'hora'))
            if minutes > 0:
                times.append(s(minutes, 'minuto'))
            if seconds > 0:
                times.append(s(seconds, 'segundo'))
            
            if len(times) == 0:
                time += '0 segundos'

            for index, item in enumerate(times):
                if index == len(times)-1 and len(times) > 1:
                    time += f' e '
                elif index != 0:
                    time += f', '
                time += item



            embed = discord.Embed() \
            .set_author(name="Bate Ponto",
                        icon_url="https://i.imgur.com/1sj9bou.png") \
            .add_field(name=":inbox_tray: Entrada:",
                       value=f'{texto(horario)}',
                       inline=False) \
            .add_field(name=":outbox_tray: Saida:",
                       value=f'{texto(now)}',
                       inline=False) \
            .add_field(name=":label:  Tempo jogado:",
                       value=f'{time}',
                       inline=False) \

            return await ctx.send(embed=embed)
            #channel = self.bot.get_channel(881007084974514186)     
            # favor fazer o bot mencionar a pessoa que o !saida no já no canal correto.
            #return await channel.send(embed=embed)
        await ctx.send("Voce não bateu o ponto de entrada!")


def texto(date: datetime) -> str:
    text = f'{date.day:0>2}/{date.month:0>2}/{date.year} {date.hour:0>2}:{date.minute:0>2}'
    return text


def s(count: int, s: str) -> str:
    return f'{count} {s}{"s" if count != 1 else ""}'


def setup(bot):
    bot.add_cog(Saida(bot))
