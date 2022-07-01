import discord
from decouple import config

token = config('TOKEN')
client = discord.Client()


@client.event
async def on_ready():
    print(f"Hello I am {client.user}")

client.run(token)
