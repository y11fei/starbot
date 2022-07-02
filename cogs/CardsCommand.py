from discord.ext import commands
import discord
from cogs.readings import thecards


class CardsCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="single")
    async def single_card(self, ctx):
        card = thecards.get_card()
        direction = thecards.get_direction().capitalize()

        embed = discord.Embed(
            title=f'{thecards.card_name(card)} ({direction})',
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
        names = thecards.get_attribute(cards, 'name')
        helper = thecards.get_shapes(names)
        count = thecards.yes_no(helper)
        shapes = thecards.helper(helper)
        if count == 0 or count == 1:
            response = "No"
            answer = "Insufficient Upright Cards to provide a Yes"
        else:
            response = "Yes"
            answer = f"You got {count} Upright Cards"
        embed = discord.Embed(
            title=f"The Answer to Your Question is a {response}",
            color=discord.Colour.purple()
        )
        embed.set_author(name="AstroBot",
                         icon_url="https://i.imgur.com/zZMmLsN.png")
        embed.add_field(name="*Your Cards*", value=shapes)
        embed.add_field(name="*Why?*", value=answer)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(CardsCommand(bot))
