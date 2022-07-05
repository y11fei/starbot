from discord.ext import commands
import discord
from cogs.astrology import signs

class AstroCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='sign')
    async def get_horoscope(self, ctx, *args):
        if not args:
            await ctx.send("In order to get a Horoscope, please submit a query like this *'!sign aquarius today'*. You can get a horoscope reading for *today, yesterday, and tomorrow* \N{slightly smiling face}")
        else:
            data = signs.get_data(args[0], args[1])
            if type(data) != dict:
                await ctx.send("Invalid query. Please try again like this *'!sign aquarius today'* \N{crystal ball}")
            else:
                embed = discord.Embed(
                    title=args[0].capitalize(),
                    description=data['description'],
                    color=discord.Colour.purple()
                )
                embed.set_author(name="StarBot",
                                 icon_url="https://i.imgur.com/zZMmLsN.png")
                embed.add_field(name="Date Range",
                                value=data['date_range'], inline=True)
                embed.add_field(name="Compatibility",
                                value=data['compatibility'], inline=True)
                embed.add_field(name="Mood", value=data['mood'], inline=True)
                embed.add_field(name="Color", value=data['color'], inline=True)
                embed.add_field(name="Lucky Number",
                                value=data['lucky_number'], inline=True)
                embed.add_field(name='Lucky Time',
                                value=data['lucky_time'], inline=True)
                await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(AstroCommands(bot))
