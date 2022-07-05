import discord
from discord.ext import commands


class HelpCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def on_help(self, ctx):
        embed = discord.Embed(
            title="Help Commands",
            description="I am *AstroBot*, a Tarot Reading Bot created by *yifei#0799*. I am here to guide you and provide you answers on these magical Tarot Cards. These are my commands and my prefix is \"!\". Happy Tarot Reading \N{ringed planet}",
            color=discord.Colour.purple(),
        )
        embed.set_author(name="StarBot",
                         icon_url="https://i.imgur.com/zZMmLsN.png")
        embed.set_thumbnail(
            url="https://upload.wikimedia.org/wikipedia/commons/f/ff/RWS_Tarot_21_World.jpg")
        embed.add_field(name="*!hello*", value="Returns a Hello", inline=False)
        embed.add_field(name="*!bye*", value="Returns a Goodbye", inline=False)
        embed.add_field(
            name="*!single*", value="Returns a single tarot card reading", inline=False)
        # embed.add_field(
        #     name="!*three*", value="Returns a past, present, future reading", inline=False)
        embed.add_field(name="*!yesno*",
                        value="Returns an answer to a yes or no question", inline=False)
        embed.add_field(
            name="*!tarot*", value="Information on the different type of readings", inline=False)
        embed.add_field(name="*!card <name of card>*",
                        value="Detailed information of a specific card", inline=False)
        embed.add_field(
            name="*!list*", value="Returns a list of all Tarot Cards", inline=False)
        embed.add_field(
            name="*!advice*", value="Returns an advice message for you", inline=False)
        embed.set_footer(
            text="For any bugs or suggestions, please dm yifei#0799")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(HelpCommands(bot))
