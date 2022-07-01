import discord

TOKEN = "OTkyMjg1MjA3NzE1NjU1Njgw.GWHhzp.4zDoZ8GRUt-q_Gx0Hw3O5UILpxKJNFnXn1kHv8"

client = discord.Client()


@client.event
async def on_ready():
    print(f"Hello I am {client.user}")

client.run(TOKEN)
