import discord
from discord.ext import commands
from decouple import config
# from os import listdir
# from os.path import isfile, join
# import sys
# import traceback

token = config('TOKEN')

bot = commands.Bot(command_prefix='?')


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.command(name="hello")
async def hello(ctx):
    username = str(ctx.author.name)
    await ctx.send(f"Hello, {username}. I am {bot.user} \N{slightly smiling face}.")


@bot.command(name="bye")
async def bye(ctx):
    username = str(ctx.author.name)
    await ctx.send(f'Goodbye, {username}. It was speaking with you \N{crystal ball}')

# cogs_dir = "cogs"

# if __name__ == '__main__':
#     for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
#         try:
#             bot.load_extension(cogs_dir + "." + extension)
#         except (discord.ClientException, ModuleNotFoundError):
#             print(f'Failed to load extension {extension}.')
#             traceback.print_exc()


bot.run(token)
