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
        yesno = ['<:drakeyes:907396138922029066>', '<:DrakeNo:851900301307936768>']
        drake_says = random.choice(yesno)
        await ctx.trigger_typing()
        return await ctx.send(drake_says)

    @commands.command(pass_context=True, hidden=True)
    async def staging(self, ctx):
        await ctx.trigger_typing()
        staging = "Current Staging is TBD we are moving south." \
                  " Please move doctrine ships to Barleguet Baguette Bakery for moing down south.\n" \
                  "None doctrine ships should be moved to highsec for moving in the future.\n"
        staging += "Last updated 8th Jan 2022\n"
        return await ctx.send(staging)

    @commands.command(pass_context=True, hidden=True)
    async def donate(self, ctx):
        await ctx.trigger_typing()
        return await ctx.send("Please donate your iskies to <@136757840403628032> the poor.")

    # @commands.command(pass_context=True, hidden=True)
    # async def askbender(self, ctx):
    #     # Bender yes or no
    #     yesno = ['<:drakeyes:907396138922029066>', '<:DrakeNo:851900301307936768>']
    #     bender_says = random.choice(yesno)
    #     await ctx.trigger_typing()
    #     return await ctx.send(bender_says)

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
