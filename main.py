import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import json
from pathlib import Path
import random
load_dotenv()

def get_prefix(bot, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    

    return prefixes[str(message.guild.id)]
prefixes = ["?","shiz ","Shiz", 's!']
bot = commands.Bot(command_prefix=prefixes, intents=discord.Intents.all())



@bot.event
async def when_mentioned():
    await bot.send("My prefixes are `s!`, `?`, `shizuku`")


@bot.command()
async def quote(ctx):
        file = open('quotes.txt', encoding="utf-8")
        contents = file.read()

        x = contents.split("@")
        y = random.choice(x)
        await ctx.send(y)

if __name__ == "__main__":
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename != "__init__.py":
            bot.load_extension(f'cogs.{filename[:-3]}')

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
bot.run(TOKEN)
