import asyncio
from discord.ext import commands


class CommandErrorHandler(commands.Cog):
    def __init__(self, hart):
        self.hart = hart

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
            canal_commandbot = self.hart.get_channel(574997304931647505)
        #try:
            #elif isinstance(error, commands.CommandNotFound):
            #    command = ctx.message.content[len(ctx.prefix):].split(' ')[0]
            #    await ctx.send(embed = discord.Embed(color=color(self.zt), description=f'<{self.zt.emoji("Error")}> {self.zt.lang(ctx, "CommandErrorHandler")["CommandNotFound"].replace("commandname", command)}'), delete_after=15)
            #    await asyncio.sleep(15)
            #    await ctx.message.delete()
            if isinstance(error, commands.CommandOnCooldown):
                await canal_commandbot.send(f'Comando em cooldown espere {int(error.retry_after)} segundos')
                await asyncio.sleep(error.retry_after)
                await ctx.message.delete()

        #except:
            pass
        
def setup(hart):
    hart.add_cog(CommandErrorHandler(hart))