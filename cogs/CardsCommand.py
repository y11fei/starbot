from discord.ext import commands
import discord
from cogs.readings import thecards


class CardsCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # single card reading
    @commands.command(name="single")
    async def single_card(self, ctx):
        card = thecards.get_card()
        direction = thecards.get_direction().capitalize()

        embed = discord.Embed(
            title=f'{thecards.card_name(card)} ({direction})',
            description=card['description'],
            color=discord.Colour.purple()
        )
        embed.set_author(name="StarBot",
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

    # yes no reading
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

    # card meaning
    @commands.command(name="card")
    async def specific_card(self, ctx, *args):
        if not args:
            await ctx.send("In order to get information on a specific Tarot card, please try like this: '*!card ace of pentacles*' \N{crystal ball}")
        else:
            card = thecards.find_card(args)
            if type(card) == str:
                await ctx.send(card)
            else:
                embed = discord.Embed(
                    title=thecards.card_name(card),
                    description=card['description'],
                    color=discord.Colour.purple()
                )
                embed.set_author(name="StarBot",
                                 icon_url="https://i.imgur.com/zZMmLsN.png")
                embed.set_thumbnail(url=thecards.get_image(card))
                embed.add_field(name="*Keywords*",
                                value=thecards.card_keywords(card), inline=True)
                embed.add_field(name="*Fortune Telling*",
                                value=thecards.get_fortunes(card), inline=True)
                embed.add_field(name="*Meaning (Upright)*",
                                value=thecards.card_meanings(card, 'upright'), inline=False)
                embed.add_field(name="*Meanings (Reversed)*",
                                value=thecards.card_meanings(card, 'reversed'), inline=False)
                embed.add_field(name="*Questions to Ask Yourself*",
                                value=thecards.get_questions(card), inline=False)
                await ctx.send(embed=embed)

    # list of all cards
    @commands.command(name="list")
    async def card_list(self, ctx):
        trump = thecards.arcana_cards('Trump')
        cups = thecards.arcana_cards('Cups')
        pentacles = thecards.arcana_cards('Pentacles')
        wands = thecards.arcana_cards('Wands')
        swords = thecards.arcana_cards('Swords')

        embed = discord.Embed(
            title="List of Cards",
            description="List of all 78 Tarot Cards separated by Suit",
            color=discord.Colour.purple()
        )
        embed.set_thumbnail(url="https://i.imgur.com/eXXeMlj.jpg")
        embed.set_author(name="StarBot",
                         icon_url="https://i.imgur.com/zZMmLsN.png")
        embed.add_field(name="Trump", value=trump, inline=True)
        embed.add_field(name="Cups", value=cups, inline=True)
        embed.add_field(name="Pentacles", value=pentacles, inline=True)
        embed.add_field(name="Swords", value=swords, inline=True)
        embed.add_field(name="Wands", value=wands, inline=True)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(CardsCommand(bot))
