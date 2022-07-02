from discord.ext import commands
import discord
from cogs.readings import single


class SingleCard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="single")
    async def single_card(self, ctx):
        card = single.get_card()
        direction = single.get_direction()

        if direction == "shadow":
            shape = "Reversed"
        else:
            shape = "Upright"

        embed = discord.Embed(
            title=f'{single.card_name(card)} ({shape})',
            description=single.card_description(card),
            color=discord.Colour.purple()
        )
        embed.set_author(name="AstroBot",
                         icon_url="https://i.imgur.com/zZMmLsN.png")
        embed.set_thumbnail(
            url=single.get_image(card))
        embed.add_field(name="*Keywords*",
                        value=single.card_keywords(card), inline=True)
        embed.add_field(name="*Fortune Telling*",
                        value=single.get_fortunes(card), inline=True)
        embed.add_field(name="*Meanings*",
                        value=single.card_meanings(card, direction), inline=False)
        embed.add_field(name="*Questions to Ask Yourself*",
                        value=single.get_questions(card))

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(SingleCard(bot))
