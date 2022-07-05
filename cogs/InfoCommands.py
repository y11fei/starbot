from discord.ext import commands
import discord


class InfoCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='tarot')
    async def on_info(self, ctx):
        embed = discord.Embed(
            title="Different Types of Readings",
            description="Using these commands you can get a reading. I am here to give you information through these readings \N{smiling face with smiling eyes}",
            color=discord.Colour.purple()
        )
        embed.set_author(name="AstroBot",
                         icon_url="https://i.imgur.com/zZMmLsN.png")
        embed.set_thumbnail(
            url="https://i.imgur.com/fukwh3e.jpg")
        embed.add_field(
            name="__*!single*__", value="A single card is not a spread, however, when in need of quick advice, this reading can provide it.", inline=False)
        # embed.add_field(name="__*!three*__ or past, present, reading",
        #                 value="This three-card spread lets you see the past influences or conditions regarding a situation, the present state of the matter, and what's likely to occur in the future.", inline=False)
        embed.add_field(name="__*!yesno*__", value="This reading will provide an answer to a yes or no question through the delivery of Ace cards. Think about your question before the expectancy of an answer. Out of three cards, if two of them are Upright, then the answer is *yes*. But if only one or none are Upright cards, then the answer is *no*")
        embed.set_footer(
            text="For suggestions so these can implemented in the future, please dm yifei#0799")

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(InfoCommands(bot))
