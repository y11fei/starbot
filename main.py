import discord
from discord.ext import commands
from decouple import config
from os import listdir
from os.path import isfile, join

token = config('TOKEN')

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

"""misc commands"""


@bot.command(name="hello")
async def hello(ctx):
    username = str(ctx.author.name)
    await ctx.send(f"Hello, {username}. I am {bot.user} \N{slightly smiling face}.")


@bot.command(name="bye")
async def bye(ctx):
    username = str(ctx.author.name)
    await ctx.send(f'Goodbye, {username}. It was speaking with you \N{crystal ball}')


"""importing cogs"""
cogs_dir = "cogs"

if __name__ == '__main__':
    for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
        bot.load_extension(cogs_dir + "." + extension)


bot.run(token)
