import discord
import os
import requests
import json
from discord.ext.commands import Bot
from discord.ext import commands
from keep_alive import keep_alive
import random

bot = Bot("<")
#client = Bot("$")

def get_quote():
    response = requests.get("https://BadAdviceDiscord.ghostbusterjeff.repl.co/api")
    json_data = json.loads(response.text)
    quote = json_data['advice']
    return (quote)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("<Whomadeyou"):
        await message.channel.send("GhostbusterJeffrey#2139")

    if message.content.startswith('<hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('<advice'):
        quote = get_quote()
        await message.channel.send(quote)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Game('Family Guy: Back to the Multiverse'))

keep_alive()
bot.run(os.getenv('TOKEN'))