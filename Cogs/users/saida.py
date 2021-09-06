import discord
from discord.ext import commands
from pymongo.collection import Collection
from datetime import datetime, timezone, timedelta


class Saida(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def saida(self, ctx):

        horarios: Collection = self.bot.db['horarios']

        horario = horarios.find_one({'_id': ctx.author.id})

        if horario:
            horarios.delete_one({'_id': ctx.author.id})

            horario = horario['horario'].replace(
                tzinfo=timezone.utc).astimezone(timezone(-timedelta(hours=3)))

            now = datetime.now(timezone(-timedelta(hours=3)))
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
                .set_author(name="Event Log",
                            icon_url="https://i.imgur.com/1sj9bou.png") \
                .add_field(name=":inbox_tray: Entrada:",
                           value=f'{texto(horario)}',
                           inline=False) \
                .add_field(name=":outbox_tray: Saida:",
                           value=f'{texto(now)}',
                           inline=False) \
                .add_field(name=":label:  Tempo jogado:",
                           value=f'{time}',
                           inline=False)

            channel = self.bot.get_channel(881007084974514186)

            return await channel.send(ctx.author.mention, embed=embed)
        await ctx.send("Voce não registrou seu horário, use !entrada")


def texto(date: datetime) -> str:
    text = f'{date.day:0>2}/{date.month:0>2}/{date.year} {date.hour:0>2}:{date.minute:0>2}'
    return text


def s(count: int, s: str) -> str:
    return f'{count} {s}{"s" if count != 1 else ""}'


def setup(bot):
    bot.add_cog(Saida(bot))
