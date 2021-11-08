# import discord
# Cog Stuff
from discord.ext import commands
import random


class OldSlack(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, hidden=True)
    async def askdrake(self, ctx):
        # Drake yes or no
        yesno = ['<:emoji_name:drakeyes:>', '<:emoji_name:drakeno:>']
        drake_says = random.choice(yesno)
        await ctx.trigger_typing()
        return await ctx.send(drake_says)

    @commands.command(pass_context=True, hidden=True)
    async def magic8ball(self, ctx):
        # Magic 8ball
        magic_ball = ['EQ would approve', 'FCs would agree', 'Your CEO is behind you',
                      'Like EM damage rips through Sansha', 'As much as VOLT is dead', 'You would get SRP', 'Yes',
                      'You might get SRP', 'Leave the SEBO behind', 'Wrong channel there friend',
                      'Lets see what the battle report says', 'My prediction is cyno jammed',
                      'Why are you ratting when there is a CTA going on?', 'No chance of SRP for that', 'No',
                      'EQ says NO', 'FCs say NO', 'I think Trony is waiting for you on the undock.']
        magic_ball_says = random.choice(magic_ball)
        await ctx.trigger_typing()
        return await ctx.send(magic_ball_says)


def setup(bot):
    bot.add_cog(OldSlack(bot))