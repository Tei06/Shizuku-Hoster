import aiohttp
import discord
import random
from discord.ext import commands

class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="gives u cat pic")
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("http://aws.random.cat/meow") as r:
                data = await r.json()
                embed = discord.Embed(title = "Catto")
                embed.set_image(url=data['file'])
                embed.set_footer(text = "Shizuku Cat pics :')")
                await ctx.send(embed=embed)
    
    @commands.command(brief="dog pics")
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/dog')
            dogjson = await request.json()
            request2 = await session.get('https://some-random-api.ml/facts/dog')
            factjson = await request2.json()

        embed = discord.Embed(title="doggo", color=discord.Color.purple())
        embed.set_image(url=dogjson['link'])
        embed.set_footer(text=factjson['fact'])
        await ctx.send(embed=embed)
    
    
    



def setup(bot):
    bot.add_cog(Images(bot))
