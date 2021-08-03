import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import random
load_dotenv()


prefixes = ["?","shiz ","Shiz", 's!']
bot = commands.Bot(command_prefix=prefixes, intents=discord.Intents.all())


@bot.event
async def on_message(message):
    empty_array = []
    modmail_channel = discord.utils.get(bot.get_all_channels(), name="hand-pics")

    if message.author == bot.user:
        return
    if str(message.channel.type) == "private":
        if message.attachments != empty_array:
            files = message.attachments
            await modmail_channel.send("[" + message.author.display_name + f":{message.author.id}" + "]")

            for file in files:
                await modmail_channel.send(file.url)
        else:
            await modmail_channel.send("[" + message.author.display_name + "] " + message.content)

    elif str(message.channel) == "hand-pics" and message.content.startswith("<"):
        member_object = message.mentions[0]
        if message.attachments != empty_array:
            files = message.attachments
            await member_object.send("[" + message.author.display_name + "]")

            for file in files:
                await member_object.send(file.url)
        else:
            index = message.content.index(" ")
            string = message.content
            mod_message = string[index:]
            await member_object.send("[" + message.author.display_name + "]" + mod_message)

    await bot.process_commands(message)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name='s!help | ur questionable', url='https://www.twitch.tv/chillhopmusic'))
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))
    channel = bot.get_channel(845354439204012052)
    await channel.send("Bot is now online")
    bruh = os.getcwd()
    print(bruh)


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
            print(f"loaded: {filename}")
            bot.load_extension(f'cogs.{filename[:-3]}')

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
bot.run(TOKEN)
