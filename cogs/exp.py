import discord
from discord.ext import commands
import pymongo
import asyncio
import time
import datetime

bot = discord.Client(intents=discord.Intents.all())

talk_channels = [856738508500500490, 840708474680770610, 840667958115172403, 857446049857011732, 845354439204012052]

mongo_urls = "mongodb+srv://brian:brianisawesome@cluster0.2tora.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
clusters = pymongo.MongoClient(mongo_urls)
dbs = clusters['ShizukuVouches']
col = dbs['Vouches']

class Exp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_voice_state_update(self, member):
        now = datetime.now(); current_time = now.strftime("%H:%M:%S")
        pass
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id in talk_channels:
            stats = col.find_one({'_id':message.author.id})
            if not message.author.bot:
                if stats is None:
                    newuser = {'_id':message.author.id, 'xp':100}
                    col.insert_one(newuser)
                else:
                    xp = stats['xp'] + 1
                    col.update_one({'_id':message.author.id}, {'$set':{'xp':xp}})
                    lvl = 0
                    while True:
                        if xp < ((50*(lvl**2))+(50*(lvl-1))):
                            break
                        lvl += 1
                    xp -= ((50*(lvl-1)**2)+(50*(lvl-1)))
                    if xp == 0:
                        await(await message.channel.send(f"Good stuff {message.author.display_name} has leveled up to **level {lvl}**").delete(delay=5))

    @commands.command()
    async def rank(self, ctx):
        stats = col.find_one({'_id':ctx.author.id})
        if stats is None:
            embed = discord.Embed(color = ctx.author.color, description = f"{ctx.author.mention} you haven't gotten any xp yet, you don't have a rank")
            await ctx.channel.send(embed=embed)
        else:
            xp = stats['xp']
            lvl = 0
            rank = 0
            while True:
                if xp < ((50*(lvl**2))+(50*(lvl-1))):
                    break
                lvl += 1
            xp -= ((50*(lvl-1)**2)+(50*(lvl-1)))
            boxes = int((xp/(200*((1/2) * lvl)))*20)
            rankings = col.find().sort("xp",-1)
            for x in rankings:
                rank += 1 
                if stats["_id"] == x["_id"]:
                    break
            embed = discord.Embed(title="{}'s level stats".format(ctx.author.name))
            embed.add_field(name = "Name", value = ctx.author.mention, inline = True)
            embed.add_field(name = "XP", value = f"{xp}/{int(200*((1/2)*lvl))}", inline = True)
            embed.add_field(name = "Rank", value = f"{rank}/{ctx.guild.member_count}", inline = True)
            embed.add_field(name = "Progress", value = boxes * ":blue_square:" + (20-boxes) * ":white_large_square:", inline = False)
            embed.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.channel.send(embed=embed)

    
    @commands.command()
    async def dashboard(self, ctx):
        if (ctx.channel.id == talk_channels):
            rankings = col.find().sort("xp",-1)
            i = 1
            embed = discord.Embed(title = "Rankings:")
            for x in rankings:
                try:
                    temp = ctx.guild.get_members(x['_id'])
                    tempxp = x['xp']
                    embed.add_field(name = f"{i}: {temp.name}", value = f"Total XP: {tempxp}", inline = False)
                    i += 1
                except:
                    pass 
                if i == 11:
                    break 
            await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Exp(bot))