import discord
import asyncio
from discord.ext import commands
cor = 0xFF0000


channel_id = 944757804185563228 #COLOCAR ID DA SALA

class Feedback(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["reclamação", "reclamaçao", "reclamacao"])
    async def feedback(self, ctx):
        user = ctx.message.author
        channel = await user.create_dm()
        await ctx.message.delete()
        try:
            Start2 = discord.Embed(color=cor)
            Start2.set_author(
                name="Olá, seja bem vindo ao centro de reclamações.", icon_url="https://i.imgur.com/c7fWRRb.png")
            Start2.add_field(name=f'**{ctx.message.author.display_name} Seja claro ao fazer sua reclamação e tambem seja paciente alguem de nossa Staff entrará em contato.**',
                             value=f"\u200b", inline=False)
            start2 = await channel.send(embed=Start2)

            try:
                mention_user = await ctx.send(ctx.author.mention)
                Start = discord.Embed(color=cor)
                Start.set_author(
                    name="Centro de Reclamações", icon_url="https://i.imgur.com/c7fWRRb.png")
                Start.add_field(name=f'** Olá {ctx.message.author.name}**',
                                value="`Será enviado uma mensagem no seu Privado. Por favor Responda.`", inline=False)
                Start.set_footer(
                    text=f"Aguardamos sua resposta!!", icon_url="https://i.imgur.com/c7fWRRb.png")
                start1 = await ctx.send(embed=Start)
                await asyncio.sleep(10)
                await start1.delete()
                await mention_user.delete()
                await start2.delete()

                p1 = discord.Embed(color=0xFF0000)
                p1.set_author(name="Qual sua reclamação ou Feedback ?",
                              icon_url="https://i.imgur.com/c7fWRRb.png")
                p1.add_field(name="Seja claro e direto ao ponto.",
                             value="`Envie tudo em apenas uma mensagem.`", inline=False)
                await channel.send(embed=p1)
                msg1 = await self.bot.wait_for('message', timeout=600.0, check=lambda x: x.channel == channel and x.author.id == user.id)

                fim = discord.Embed(color=0xFF0000)
                fim.set_author(name="Muito Obrigado!!")
                fim.add_field(name="Agradecemos muito seu feedback",
                              value="`Embreve alguem da Staff entrará em contato!!`", inline=False)
                fim.set_footer(text="Khal Special Forces agradece sua mensagem!", icon_url="https://i.imgur.com/c7fWRRb.png")
                await channel.send(embed=fim)

                channel = self.bot.get_channel(channel_id)
                
                
                await channel.send(f"{ctx.message.guild.default_role} **Reclamação ou Feedback** {ctx.author.mention}")
                fim = discord.Embed(color=0xFF0000)
                fim.set_author(name=f"Reclamação / Feedback {ctx.author.name}")
                fim.set_footer(text="Khal Special Forces Feedback", icon_url="https://i.imgur.com/c7fWRRb.png")
                await channel.send(embed=fim)
                await channel.send(msg1.content)

            except Exception as e:
                embed = discord.Embed(color=0xFF0000)
                embed.set_author(name="O Seu tempo acabou!!")
                
                embed.add_field(name="Você excedeu o tempo limite da resposta...",
                                value="`Volte ao chat e execute o comando novamente!!`", inline=False)
                embed.set_footer(text="Khal Special Forces",icon_url="https://i.imgur.com/c7fWRRb.png")
                await channel.send(embed=embed)
                await start1.delete()
                await mention_user.delete()
                print(e)

        except Exception as e:
            info_erro = discord.Embed(
                colour=cor, description=f'** Olá {ctx.message.author.name}#{ctx.message.author.discriminator}, se você deseja fazer uma reclamação, porfavor mantenha o seu Privado aberto.**')
            info_erro.add_field(
                name='Infelizmente não foi possivel enviar mensagem no seu privado.', value='⠀⠀⠀⠀', inline=False)

            info_erro.add_field(
                name='Como resolver ?', value='Vá na configuração de privacidade do servidor e habilite para receber mensagem privadas.', inline=False)
            info_erro.set_footer(text="Khal Special Forces | Essa mensagem será excluida em 60 segundos.",icon_url="https://i.imgur.com/c7fWRRb.png")
            info_error = await ctx.send(embed=info_erro)
            await asyncio.sleep(60)
            await info_error.delete()
            print(e)


def setup(bot):
    bot.add_cog(Feedback(bot))
