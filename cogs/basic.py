from discord.ext import commands
import discord
import random
import asyncio
import requests
import json
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)


def last_replace(s, old, new):
    li = s.rsplit(old, 1)
    return new.join(li)

def text_to_owo(text):
    """ Converts your text to OwO """
    smileys = [';;w;;', '^w^', '>w<', 'UwU', '(・`ω\´・)', '(´・ω・\`)']

    text = text.replace('L', 'W').replace('l', 'w')
    text = text.replace('R', 'W').replace('r', 'w')

    text = last_replace(text, '!', '! {}'.format(random.choice(smileys)))
    text = last_replace(text, '?', '? owo')
    text = last_replace(text, '.', '. {}'.format(random.choice(smileys)))

    for v in vowels:
        if 'n{}'.format(v) in text:
            text = text.replace('n{}'.format(v), 'ny{}'.format(v))
        if 'N{}'.format(v) in text:
            text = text.replace('N{}'.format(v), 'N{}{}'.format(
                'Y' if v.isupper() else 'y', v))

    return text

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(brief="hacks someone in the server")
    async def hack(self, ctx, member: discord.Member):
        await ctx.message.delete()
        message = await ctx.channel.send(f"[▝]Logging in to {member.mention} <a:EE_loading:855933211644788757>")
        await asyncio.sleep(1.3)
        await message.edit(content = f"Bypassing 2fa information  <a:EE_loading:855933211644788757>")
        await asyncio.sleep(1.5)
        await message.edit(content = "Successfully bypassed 2fa")
        await asyncio.sleep(0.9)
        await message.edit(content = f"**Username:**`{member.name}ishorny24/7@gmail.com`\n**Password:**`{member.name}likesdragonsandrainbowsbling\n**or**\n`{member.name}wantstoeatabigbalonisandwichwithyourmother`")
        await asyncio.sleep(2.4)
        await message.edit(content = f"[▗]Successfully logged in as {member.name}")
        await asyncio.sleep(0.5)
        await message.edit(content = f"[▖]Accessing search history <a:EE_loading:855933211644788757>")
        await asyncio.sleep(1.5)
        await message.edit(content = f"[▘]Sending sus search history to {member.name}'s school principle  <a:EE_loading:855933211644788757>")
        await asyncio.sleep(1.4)
        await message.edit(content = f"[▝]johnny is disaapointed", tts = True)
        await asyncio.sleep(0.8)
        await message.edit(content = f"[▗]Fetching sus dm's *if you have any friends at all*")
        await asyncio.sleep(1.6)
        await message.edit(content = f"[▖]Sending blackmail on all {member.name}'s social media <a:EE_loading:855933211644788757>")
        await asyncio.sleep(1.5)
        await message.edit(content = f"[▘]Injecting ligma and sussybaka virus into {member.name}'s 2001 block of plastic <a:EE_loading:855933211644788757>")
        await asyncio.sleep(1.6)
        await message.edit(content = f"virus files has been unleashed into {member.name}'s computer")
        await asyncio.sleep(1.6)
        await message.edit(content = "||totally legit hack, you should check your computer for virus||")
        await asyncio.sleep(0.5)
        await ctx.channel.send(content = f"the concerning and sus hack has been completed on {member.name}")
    
    @commands.command(brief="sned ur message but in owo")
    async def owo(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(text_to_owo(message))
    
    @commands.command(aliases = ['av'], brief="shows the mentioned users avatar")
    async def avatar(self, ctx, *, member: discord.Member = None):
        if member == None:
            member = ctx.author
            embed = discord.Embed(title = f"{member.display_name}'s Avatar",
            color = ctx.author.color)
            embed.set_image(url = member.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title = f"{member.display_name}'s Avatar",
            color = ctx.author.color)
            embed.set_image(url = member.avatar_url)
            await ctx.send(embed=embed)
    
    @commands.command(brief="shows server stats")
    async def server(self, ctx):
        server = ctx.message.guild

        roles = str(len(server.roles))
        emojis = str(len(server.emojis))
        channels = str(len(server.channels))

        embeded = discord.Embed(title=server.name, description='Server Info', color=ctx.author.color)
        embeded.set_thumbnail(url=server.icon_url)
        embeded.add_field(name="Created on:", value=server.created_at.strftime('%d %B %Y at %H:%M UTC+3'), inline=False)
        embeded.add_field(name="Server ID:", value=server.id, inline=False)
        embeded.add_field(name="Users on server:", value=server.member_count, inline=True)
        embeded.add_field(name="Server owner:", value=server.owner, inline=True)


        embeded.add_field(name="Server Region:", value=server.region, inline=True)
        embeded.add_field(name="Verification Level:", value=server.verification_level, inline=True)

        embeded.add_field(name="Role Count:", value=roles, inline=True)
        embeded.add_field(name="Emoji Count:", value=emojis, inline=True)
        embeded.add_field(name="Channel Count:", value=channels, inline=True)

        await ctx.send(embed=embeded)
    @commands.command(brief="command is a work in progress")
    async def timer(self, ctx, number:int):
        try:
            if number < 0:
                await ctx.send('number cant be a negative')
            elif number > 300:
                await ctx.send('number must be under 300')
            else:
                embed=discord.Embed(title = f"{number}", color = discord.Color.random())
                t = await ctx.send(embed=embed)
                while number != 0:
                        number -= 1
                        embed2=discord.Embed(titel = f"{number}", color = discord.Color.random())
                        await t.edit(embed=embed2)
                        await asyncio.sleep(1)
                embed3 = discord.Embed(title = f"Timer has ended", color = discord.Color.random())
                await t.edit(embed=embed3)

        except ValueError:
            await ctx.send('time was not a number')
    @commands.command(aliases=['motiv', 'm'], brief="motivational quote")
    async def motivation(self, ctx):
        await ctx.message.delete()
        quote = get_quote()
        await ctx.channel.send(quote)
    @commands.command(aliases=['8ball'], brief="gives you a random yes - no response")
    async def _8ball(self, ctx, *, question):
        responses = [
                    "It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
        

def setup(bot):
    bot.add_cog(Basic(bot))
