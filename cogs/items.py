import pymongo
from discord.errors import *
from discord.ext import commands
import discord
import asyncio

mongo_urls1 = "mongodb+srv://ShizukuTest:yeet123LMAO@cluste.gmxuc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
clusterr = pymongo.MongoClient(mongo_urls1)
db1 = clusterr["ShizukuTest"]
collec = db1['test']

mongo_url = "mongodb+srv://Tei:yeet123LMAO@shizukudb.rt4ys.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
cluster = pymongo.MongoClient(mongo_url)
db = cluster["ShizukuDB"]
collection = db['new']

async def create_role(ctx, name, color):
        try:
            guild = ctx.guild
            await guild.create_role(name=name, color=color)
        except InvalidArgument:
            await ctx.send(f"{ctx.author.mention} invalid color hex")

class Items(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="command is a work in progress")
    async def purchase(self, ctx):
        await ctx.message.delete()
        stats = collec.find_one({'_id':ctx.author.id})
        if not ctx.message.author.bot:
            if stats is None:
                post = {'_id':ctx.author.id,
                'Role Pass':0,
                'Role ID':0,
                'Custom Command':0,
                "Owner's Blessing":0
                }
                collec.insert_one(post)
            else:
                try:
                    await ctx.send(f"{ctx.author.mention} which item would you like to purchase")
                    def check(m):
                        return m.author == ctx.author and m.channel == ctx.channel
                    msg = await self.bot.wait_for('message', timeout=30, check=check)
                    if msg == "Role" or 'Custom role' or 'role' or 'custom role':
                        ms = collection.find({'_id':ctx.author.id})
                        for i in ms:
                            money = i['Wallet']
                            if money < 100000:
                                await ctx.send(f"{ctx.author.mention} you don't have enough points to purchase a role")
                                return
                            else:
                                await ctx.send(f'{ctx.author.mention} what should the name of your role be?')
                                name = await self.bot.wait_for('message', check=check)
                                await ctx.send(f'{ctx.author.mention} provide a hex for your role')
                                color = await self.bot.wait_for('message', check=check)
                                colors = "0x"+str(color)
                                role = await create_role(ctx, name=name, color = int(colors))
                                embed=discord.Embed(title = f'role create pass for {ctx.author.display_name}',
                                description = f"Successfully created role {name}", colour = discord.Colour(colors))
                                collec.update({'_id':ctx.author.id}, {'$set':{'Role ID':role.id}})
                                print(role)
                                await ctx.send(embed=embed)
                                collection.update_one({'_id':ctx.author.id}, {'$inc':{'Wallet':-1000000}}, upsert=True)
                except asyncio.TimeoutError:
                    await ctx.send("You didn't respond in time...".delete(seconds=5))
    @commands.command(brief="command is a work in progress")
    async def use(self, ctx, item):
        if item == 'role' or 'Custom Role' or 'custom role':
            stats = collec.find_one({'_id':ctx.author.id})
            if not ctx.message.author.bot:
                if stats is None:
                    post = {'_id':ctx.author.id,
                    'Role Pass':0,
                    'Role Id':0,
                    'Custom Command':0,
                    "Owner's Blessing":0
                    }
                    collec.insert_one(post)
            else:
                m = collec.find_one({'_id':ctx.author.id})
                for x in m:
                    role = x['Role Pass']
                if role < 1:
                    await ctx.send(f"{ctx.author.mention} You dont have a custom role pass to use")
                    return
                else:
                    b = collec.find_one({'_id':ctx.author.id})
                    for x in b:
                        id = x['Role ID']


        
def setup(bot):
    bot.add_cog(Items(bot))
