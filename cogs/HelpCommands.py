import discord
from discord.ext import commands


class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def on_help(self, ctx):
        embed = discord.Embed(
            title="Help Commands",
            description="You can use these commands to return a value",
            color=discord.Colour.purple(),
        )
        embed.set_author(name="AstroBot",
                         icon_url="https://i.imgur.com/zZMmLsN.png")
        embed.set_thumbnail(
            url="https://upload.wikimedia.org/wikipedia/commons/f/ff/RWS_Tarot_21_World.jpg")
        embed.add_field(name="*!hello*", value="Returns a Hello", inline=False)
        embed.add_field(name="*!bye*", value="Returns a Goodbye", inline=False)
        embed.add_field(
            name="*!single*", value="Returns a single tarot card reading", inline=False)
        embed.add_field(
            name="!*three*", value="Returns a past, present, future reading", inline=False)
        embed.add_field(
            name="*!info*", value="Information on the different type of readings", inline=False)
        embed.add_field(name="*!card <name of card>*",
                        value="Detailed information of a specific card", inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(HelpCommands(bot))
