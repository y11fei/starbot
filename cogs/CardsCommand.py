from discord.ext import commands
import discord
from cogs.readings import thecards


class CardsCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="single")
    async def single_card(self, ctx):
        card = thecards.get_card()
        direction = thecards.get_direction()

        if direction == "shadow":
            shape = "Reversed"
        else:
            shape = "Upright"

        embed = discord.Embed(
            title=f'{thecards.card_name(card)} ({shape})',
            description=thecards.card_description(card),
            color=discord.Colour.purple()
        )
        embed.set_author(name="AstroBot",
                         icon_url="https://i.imgur.com/zZMmLsN.png")
        embed.set_thumbnail(
            url=thecards.get_image(card))
        embed.add_field(name="*Keywords*",
                        value=thecards.card_keywords(card), inline=True)
        embed.add_field(name="*Fortune Telling*",
                        value=thecards.get_fortunes(card), inline=True)
        embed.add_field(name="*Meanings*",
                        value=thecards.card_meanings(card, direction), inline=False)
        embed.add_field(name="*Questions to Ask Yourself*",
                        value=thecards.get_questions(card))

        await ctx.send(embed=embed)

    @commands.command(name="yesno")
    async def yes_no(self, ctx):
        cards = thecards.get_3cards()
        count = thecards.yes_no(cards)
        names = thecards.get_attribute(cards, 'name')
        if count == 0 or 1:
            response = "No"
            answer = "Insufficient Ace Cards to provide a Yes"
        else:
            response = "yes"
            answer = "You got 2 Ace Cards"
        embed = discord.Embed(
            title=f"The Answer to Your Question is a {response}",
            color=discord.Colour.purple()
        )
        embed.set_author(name="AstroBot",
                         icon_url="https://i.imgur.com/zZMmLsN.png")
        embed.add_field(name="*Your Cards*", value=names)
        embed.add_field(name="*Interpretation*", value=answer)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(CardsCommand(bot))
