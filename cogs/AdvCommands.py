from cmath import e
from discord.ext import commands
import discord
from cogs.readings import advice


class AdvCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="advice")
    async def get_advice(self, ctx):
        adv = advice.get_adv()
        username = ctx.author.name
        embed = discord.Embed(
            title=f"Advice for {username}",
            description=adv,
            color=discord.Colour.purple()
        )
        embed.set_author(name="StarBot",
                         icon_url="https://i.imgur.com/zZMmLsN.png")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(AdvCommands(bot))
