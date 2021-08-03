from discord.ext import commands, tasks
import pymongo
import discord
import asyncio
import random

bot = discord.Client(intents=discord.Intents.all())

mongo_url = "mongodb+srv://Tei:yeet123LMAO@shizukudb.rt4ys.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
cluster = pymongo.MongoClient(mongo_url)
db = cluster["ShizukuDB"]
collection = db['new']
intents = discord.Intents.default()

async def get_user(member):
    stats = collection.find({'_id':member})
    if stats == None:
        post = {"_id": member,
                "Wallet": 0,
                "Bank_Space": 50,
                'Bank': 0
                    }
        collection.insert_one(post)
        await bot.send("Account successfully created")

"""async def check_money(ctx, user, amount):
    stats = collection.find({'_id':user.id})
    amount = int(amount)
    if stats == None:
        await get_user
    for x in stats:
        money = x['Wallet']
    if money < amount:
        await ctx.send(f"{ctx.user.mention} You don't have that much points in your wallet bruh")
        return
    if amount < 5:
        await ctx.send(f"{ctx.user.mention} You can't bet less that 5 points")
        return
    if amount < 0:
        await ctx.send(f"{ctx.user.mention} You can't bet negative points bruh")
        return"""

class Points(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases = ['open', 's'])
    async def start(self, ctx, member: discord.Member = None):
        if member == None:
            stat = collection.find_one({'_id':ctx.author.id})
            if stat == None:
                post = {
                        "_id": ctx.author.id,
                        "Wallet": 0,
                        "Bank_Space": 50,
                        'Bank': 0
                    }
                collection.insert_one(post)
                await ctx.send("Account successfully created")
            else:
                await ctx.send("You already have an account")
        else:
            stat = collection.find_one({'_id':member.id})
            if stat == None:
                post = {
                            "_id": member.id,
                            "Wallet": 0,
                            "Bank_Space": 50,
                            'Bank': 0
                        }
                collection.insert_one(post)
                await ctx.send("Account successfully created")
            else:
                await ctx.send("That user already has an account")


    @commands.command(aliases = ['rps'])
    async def rockpaperscissors(self, ctx):
        await get_user(ctx.author.id)
        rpsGame = ['rock', 'paper', 'scissors']
        collection.update_one({'_id':ctx.author.id}, {'$inc':{'Bank_Space':1}}, upsert=True) 
        await ctx.send(f"Rock, paper, or scissors? Choose wisely...")
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rpsGame
        user_choice = (await self.bot.wait_for('message', check=check)).content
        comp_choice = random.choice(rpsGame)
        if user_choice == 'rock':
            if comp_choice == 'rock':
                embed1 = discord.Embed(title = "Intense game of rock paper scissors...", color = ctx.author.color)
                embed1.set_image(url = 'https://i.pinimg.com/originals/f6/99/14/f69914b03a9e05de63293ec786f53b4d.gif')
                msg = await ctx.send(embed=embed1)
                await asyncio.sleep(2.2)
                embed2 = discord.Embed(title = 'Well, we tied. How lame.', color = ctx.author.color)
                embed2.set_image(url = 'https://media.tenor.com/images/eea071a04e23ff4e109087a18d78a1f8/tenor.gif')
                embed2.add_field(name = '**Your Choice:\n**', value = f"{user_choice}")
                embed2.add_field(name = '**My Choice:\n**', value = f"{comp_choice}")
                await msg.edit(embed=embed2)
            elif comp_choice == 'paper':
                embed1 = discord.Embed(title = "Intense game of rock paper scissors...", color = ctx.author.color)
                embed1.set_image(url = 'https://i.pinimg.com/originals/f6/99/14/f69914b03a9e05de63293ec786f53b4d.gif')
                msg = await ctx.send(embed=embed1)
                await asyncio.sleep(2.2)
                embed2 = discord.Embed(title = 'Nice try but I won that time >;)', color = ctx.author.color)
                embed2.set_image(url = 'https://64.media.tumblr.com/dd0a4f60fab86914035631d3319ef7be/tumblr_p8kmwbo20d1xs22ito1_500.gif')
                embed2.add_field(name = '**Your Choice:\n**', value = f"{user_choice}")
                embed2.add_field(name = '**My Choice:\n**', value = f"{comp_choice}")
                embed2.set_footer(text="heh no points for u")
                await msg.edit(embed=embed2)
            elif comp_choice == 'scissors':
                embed1 = discord.Embed(title = "Intense game of rock paper scissors...", color = ctx.author.color)
                embed1.set_image(url = 'https://i.pinimg.com/originals/f6/99/14/f69914b03a9e05de63293ec786f53b4d.gif')
                msg = await ctx.send(embed=embed1)
                await asyncio.sleep(2.2)
                embed2 = discord.Embed(title = 'Ah shit, you beat me.', color = ctx.author.color, description = "I guess I'll give you 5 points... <:petpigsniff:856645464895520788>")
                embed2.set_image(url = 'https://media1.tenor.com/images/e56e1ae197ea11668756e6e82407e5c5/tenor.gif')
                embed2.add_field(name = '**Your Choice:\n**', value = f"{user_choice}")
                embed2.add_field(name = '**My Choice:\n**', value = f"{comp_choice}")
                embed2.set_footer(text="i went easy this time smh")
                await msg.edit(embed=embed2)
                collection.update_one({'_id': ctx.author.id}, {'$inc':{'Wallet':5}}, upsert=True)
                collection.update_one({'_id':ctx.author.id}, {'$inc':{'Bank_Space':1}}, upsert=True)
        elif user_choice == 'paper':
            if comp_choice == 'rock':
                embed1 = discord.Embed(title = "Intense game of rock paper scissors...", color = ctx.author.color)
                embed1.set_image(url = 'https://i.pinimg.com/originals/f6/99/14/f69914b03a9e05de63293ec786f53b4d.gif')
                msg = await ctx.send(embed=embed1)
                await asyncio.sleep(2.2)
                embed2 = discord.Embed(title = 'crap- ill let you win this time around-', color = ctx.author.color, description = "I guess I'll give you 5 points... <:petpigsniff:856645464895520788>")
                embed2.set_image(url = 'https://i.imgur.com/UILjVng.gif')
                embed2.add_field(name = '**Your Choice:\n**', value = f"{user_choice}")
                embed2.add_field(name = '**My Choice:\n**', value = f"{comp_choice}")
                embed2.set_footer(text="i went too easy on you this time smh")
                await msg.edit(embed=embed2)
                collection.update_one({'_id': ctx.author.id}, {'$inc':{'Wallet':5}}, upsert=True)
                collection.update_one({'_id':ctx.author.id}, {'$inc':{'Bank_Space':1}}, upsert=True)
            elif comp_choice == 'paper':
                embed1 = discord.Embed(title = "Intense game of rock paper scissors...", color = ctx.author.color)
                embed1.set_image(url = 'https://i.pinimg.com/originals/f6/99/14/f69914b03a9e05de63293ec786f53b4d.gif')
                msg = await ctx.send(embed=embed1)
                await asyncio.sleep(2.2)
                embed2 = discord.Embed(title = 'bruhhhh another tie?', color = ctx.author.color)
                embed2.set_image(url = 'https://media4.giphy.com/media/U7GRtzqJMyVEs/200.gif')
                embed2.add_field(name = '**Your Choice:\n**', value = f"{user_choice}")
                embed2.add_field(name = '**My Choice:\n**', value = f"{comp_choice}")
                embed2.set_footer(text='rematch me rn ill smoke u')
                await msg.edit(embed=embed2)
            elif comp_choice == 'scissors':
                embed1 = discord.Embed(title = "Intense game of rock paper scissors...", color = ctx.author.color)
                embed1.set_image(url = 'https://i.pinimg.com/originals/f6/99/14/f69914b03a9e05de63293ec786f53b4d.gif')
                msg = await ctx.send(embed=embed1)
                await asyncio.sleep(2.2)
                embed2 = discord.Embed(title = 'hippity hoppity my points are not your property >:)', color = ctx.author.color)
                embed2.set_image(url = 'https://www.icegif.com/wp-content/uploads/evil-laugh-icegif-23.gif')
                embed2.add_field(name = '**Your Choice:\n**', value = f"{user_choice}")
                embed2.add_field(name = '**My Choice:\n**', value = f"{comp_choice}")
                embed2.set_footer(text="heh no points for u luzer")
                await msg.edit(embed=embed2)
        elif user_choice == 'scissors':
            if comp_choice == 'rock':
                embed1 = discord.Embed(title = "Intense game of rock paper scissors...", color = ctx.author.color)
                embed1.set_image(url = 'https://i.pinimg.com/originals/f6/99/14/f69914b03a9e05de63293ec786f53b4d.gif')
                msg = await ctx.send(embed=embed1)
                await asyncio.sleep(3)
                embed2 = discord.Embed(title = 'LMAO IMAGINE LOSING TO A BOT IN RPS', color = ctx.author.color)
                embed2.set_image(url = 'https://i.imgur.com/zORK5gV.gif')
                embed2.add_field(name = '**Your Choice:\n**', value = f"{user_choice}")
                embed2.add_field(name = '**My Choice:\n**', value = f"{comp_choice}")
                embed2.set_footer(text="heh no points for u luzer")
                await msg.edit(embed=embed2)
            elif comp_choice == 'paper':
                embed1 = discord.Embed(title = "Intense game of rock paper scissors...", color = ctx.author.color)
                embed1.set_image(url = 'https://i.pinimg.com/originals/f6/99/14/f69914b03a9e05de63293ec786f53b4d.gif')
                msg = await ctx.send(embed=embed1)
                await asyncio.sleep(3)
                embed2 = discord.Embed(title = 'Bruh stop winning. ur keep stealing my points.', color = ctx.author.color, description = "I guess I'll give you 5 points... <:petpigsniff:856645464895520788>")
                embed2.set_image(url = 'https://i.pinimg.com/originals/a5/c0/62/a5c062b945367ba3419f52cbef6be867.gif')
                embed2.add_field(name = '**Your Choice:\n **', value = f"{user_choice}")
                embed2.add_field(name = '**My Choice:\n **', value = f"{comp_choice}")
                embed2.set_footer(text="im going broke")
                await msg.edit(embed=embed2)
                collection.update_one({'_id': ctx.author.id}, {'$inc':{'Wallet':5}}, upsert=True)
                collection.update_one({'_id':ctx.author.id}, {'$inc':{'Bank_Space':1}}, upsert=True)
            elif comp_choice == 'scissors':
                embed1 = discord.Embed(title = "Intense game of rock paper scissors...", color = ctx.author.color)
                embed1.set_image(url = 'https://media.tenor.com/images/ed2058bd089729e3a719d20bde731cd0/tenor.gif')
                msg = await ctx.send(embed=embed1)
                await asyncio.sleep(3)
                embed2 = discord.Embed(title = 'welp. we tied.', color = ctx.author.color)
                embed2.set_image(url = '')
                embed2.add_field(name = '**Your Choice:\n**', value = f"{user_choice}")
                embed2.add_field(name = '**My Choice:\n**', value = f"{comp_choice}")
                embed2.set_footer(text='rematch me rn ill smoke ur pack')
                await msg.edit(embed=embed2)

    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def beg(self, ctx):
        collection.update_one({'_id':ctx.author.id}, {'$inc':{'Bank_Space':2}}, upsert=True) 
        amount = random.randint(1,10)
        collection.update({'_id':ctx.author.id}, {'$inc':{'Wallet':amount}}, upsert=True)
        message = "Tei has spared you ", "The owner has dropped points. You picked up ", "wha- some points fell out of the sky. You picked up ", "u shoved ur hand into your rusty musty bag, and picked up ", "The tooth fairy has left you ", "donkeh the elephant gave you"
        await ctx.channel.send(f"{random.choice(message)}{str(amount)} points")
    @beg.error
    async def beg_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention} You can beg people for points again in {round(error.retry_after, 1)} seconds")
    @commands.command()
    @commands.cooldown(1,86400,commands.BucketType.user)
    async def daily(self, ctx):
        await get_user(ctx.author.id)
        collection.update_one({'_id':ctx.author.id}, {'$inc':{'Bank_Space':10}}, upsert=True)
        collection.update({'_id':ctx.author.id}, {'$inc':{'Wallet':50}}, upsert=True)
        await ctx.send(f"{ctx.author.mention} you have claimed your daily 50 points")

    @daily.error
    async def daily_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention} You can claim daily again in {int(round(error.retry_after, 1))} seconds")
            
    @commands.command(aliases = ['cf','flipcoin'])
    async def coinflip(self, ctx):
        collection.update_one({'_id':ctx.author.id}, {'$inc':{'Bank_Space':1}}, upsert=True) 
        await ctx.send('You have flipped a coin. heads or tails?')
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
        headtail = (await self.bot.wait_for('message', check=check)).content
        coins = ['heads', 'tails']
        comp_flip_result = random.choice(coins)
        if headtail == 'heads':
            if comp_flip_result == 'heads':
                await ctx.send('darn you managed to guess correctly. Heres your well earned 5 points')
                collection.update_one({'_id': ctx.author.id}, {'$inc':{'Wallet':5}}, upsert=True)
                collection.update_one({'_id':ctx.author.id}, {'$inc':{'Bank_Space':1}}, upsert=True)
            elif comp_flip_result == 'tails':
                await ctx.send(f"{ctx.author.mention} looks like you didn't guess correctly this time around ;D")
        elif headtail == 'tails':
            if comp_flip_result == 'tails':
                await ctx.send('darn you managed to guess correctly. Heres your well earned 5 points')
                collection.update_one({'_id': ctx.author.id}, {'$inc':{'Wallet':5}}, upsert=True)
                collection.update_one({'_id':ctx.author.id}, {'$inc':{'Bank_Space':1}}, upsert=True)
            elif comp_flip_result == 'heads':
                await ctx.send(f"{ctx.author.mention} looks like you didn't guess correctly this time around ;D")

    @commands.command(aliases = ['rob'])
    async def steal(self, ctx, *, member: discord.Member = None):
        await get_user(ctx.author.id)
        if member == None:
            await ctx.send(f"{ctx.author.mention} bruh mention someone to steal from")
            return
        s = collection.find({'_id':member.id})
        for x in s:
            wallet = x['Wallet']
        if wallet <= 5:
            await ctx.send(f"{ctx.author.mention} bro that person doesn't even have 5 points in their wallet...")
            return
        collection.update_one({'_id':ctx.author.id}, {'$inc':{'Bank_Space':1}}, upsert=True) 
        results = ['steal', 'keep', 'lose','lose','keep']
        result = random.choice(results)
        if result == 'steal':
            steal_amount = random.randint(1,15)
            collection.update_one({'_id': ctx.author.id}, {'$inc':{'Wallet':steal_amount}}, upsert=True)
            collection.update_one({'_id':ctx.author.id}, {'$inc':{'Bank_Space':1}}, upsert=True)
            collection.update_one({'_id': member.id}, {'$inc':{'Wallet':-1*steal_amount}}, upsert=True)
            collection.update_one({'_id':member.id}, {'$inc':{'Bank_Space':1}}, upsert=True)
            await ctx.send(f"{ctx.author.mention} just stole {steal_amount} points from {member.mention} LMAO <a:gottago:842208779440881665>")
        elif result == 'keep':
            await ctx.send(f"{ctx.author.mention} bruh ur actually so bad at stealing <a:mindblown:855492678665371648> that you stepped on your on foot while attempting to steal from {member.mention} <:catL:844940795395047515>")
        elif result == 'lose':
            lose_amount = random.randint(1, 5)
            collection.update_one({'_id': ctx.author.id}, {'$inc':{'Wallet':-1*lose_amount}}, upsert=True)
            collection.update_one({'_id':ctx.author.id}, {'$inc':{'Bank_Space':1}}, upsert=True)
            await ctx.send(f"how disappointing. {ctx.author.mention} tried stealing from {member.mention} but walked into a pole and lost {lose_amount} points from hospital fees. :person_facepalming:")
    
    @commands.command(aliases = ['bal', 'wallet'])
    async def mypoints(self, ctx, member: discord.Member = None):
        await get_user(ctx.author.id)
        if member == None:
            results = collection.find({'_id':ctx.author.id})
            for result in results:
                amount = result["Wallet"]
                banks = result["Bank_Space"]
                bank = result["Bank"]
                embed = discord.Embed(title = f"{ctx.author.display_name} Balance", color = ctx.author.color)
                embed.add_field(name = "**Wallet**", value = f"\n\nAmount: {amount} points", inline = False)
                percent = bank/banks*100
                embed.add_field(name = "**Bank**", value = f" \n\nAmount: {bank}\nAvailable Space: {banks}\n`Bank is {int(percent)}% full`")
                embed.set_thumbnail(url = ctx.author.avatar_url)
                space = banks - bank
                embed.set_footer(text=f"You have {int(space)} available space")
                await ctx.send(embed=embed)
        else:
            await get_user(member.id)
            results = collection.find({'_id':member.id})
            for result in results:
                amount = result["Wallet"]
                banks = result['Bank_Space']
                bank = result["Bank"]
                embed = discord.Embed(title = f"{member.display_name} Balance", color = member.color)
                embed.add_field(name = "**Wallet**", value = f"\n\nAmount: {amount} points", inline = False)
                percent = bank/banks*100
                embed.add_field(name = "**Bank**", value = f" \n\nAmount: {bank}\nAvailable Space: {banks}\n`Bank is {int(percent)}% full`")
                embed.set_thumbnail(url = member.avatar_url)
                space = banks - bank
                embed.set_footer(text=f"{member.name} has {space} available space")
                await ctx.send(embed=embed)

    @commands.command(aliases = ['dep'])
    async def deposit(self, ctx, amount):
        await get_user(ctx.author.id)
        if amount  == "all":
            bank = collection.find({'_id': ctx.author.id})
            for m in bank:
                money = m['Wallet']
            collection.update_one({'_id': ctx.author.id}, {'$inc':{'Wallet':-1*money}}, upsert=True)
            collection.update_one({'_id': ctx.author.id}, {'$inc':{'Bank':money}}, upsert=True)
            await ctx.send(f"Successfully withdrew {money} points from your bank")
        else:
            amount = int(amount)
            if amount < 0:
                await ctx.send("You can't deposit negative values")
                return
            elif amount == 0 or None:
                await ctx.send("You didn't enter a amount to deposit")
                return
            wallet = collection.find({'_id': ctx.author.id})
            for m in wallet:
                money = m['Wallet']
                banks = m['Bank_Space']
                bank = m['Bank']
                if money < amount:
                    await ctx.send("You don't have that much money to deposit")
                    return
                banks = banks - bank
                if banks < amount:
                    await ctx.send(f"You don't have enough space to deposit. Available amount: {banks}")
                    return
            collection.update_one({'_id': ctx.author.id}, {'$inc':{'Bank':amount}}, upsert=True)
            dep_amt = -1*amount
            collection.update_one({'_id': ctx.author.id}, {'$inc':{'Wallet':dep_amt}}, upsert=True)
            await ctx.send(f"Successfully deposited {amount} points")


    @commands.command(aliases=['with'])
    async def withdraw(self, ctx, amount):
        await get_user(ctx.author.id)
        if amount == "all":
            bank = collection.find({'_id': ctx.author.id})
            for m in bank:
                money = m['Bank']
            collection.update_one({'_id': ctx.author.id}, {'$inc':{'Wallet':money}}, upsert=True)
            collection.update_one({'_id': ctx.author.id}, {'$inc':{'Bank':-1*money}}, upsert=True)
            await ctx.send(f"Successfully withdrew {money} points from your bank")
        else: 
            amount = int(amount)
            if amount < 0:
                await ctx.send("You can't withdraw negative values")
                return
            elif amount == 0 or None:
                await ctx.send("You didn't enter a amount to withdraw")
                return
            bank = collection.find({'_id': ctx.author.id})
            for m in bank:
                money = m['Bank']
                if money < amount:
                    await ctx.send("You don't have that much points to withdraw")
                    return
            collection.update_one({'_id': ctx.author.id}, {'$inc':{'Wallet':amount}}, upsert=True)
            dep_amt = -1*amount
            collection.update_one({'_id': ctx.author.id}, {'$inc':{'Bank':dep_amt}}, upsert=True)
            await ctx.send(f'Successfully withdrew {amount} points')

   

    @commands.command()
    @commands.is_owner()
    async def award(self, ctx, member: discord.Member = None, amount = None):
        await get_user(member.id)
        amount = int(amount)
        collection.update_one({'_id': member.id}, {'$inc':{'Wallet':amount}}, upsert=True)
        await ctx.send(f'{ctx.author.mention} Successfully awarded {amount} points to {member.mention}')

    @commands.command()
    async def give(self, ctx, member: discord.Member = None, amount = None):
        await get_user(ctx.author.id)
        await get_user(member.id)
        if member == None:
            await ctx.send(f"{ctx.author.mention} Mention someone to give points to")
        else:
            results = collection.find({'_id':ctx.author.id})
            for result in results:
                bal = result['Wallet']
            amount = int(amount)
        if amount>bal:
            await ctx.send(f"{ctx.author.mention} You dont have that much to send bruh")
            return
        if amount<0:
            await ctx.send(f"{ctx.author.mention} You can't send someone negative coins")
            return
        if amount == None:
            await ctx.send(f'{ctx.author.mention} enter an amount to give')
            return
        collection.update_one({'_id': ctx.author.id}, {'$inc':{'Wallet':-1*amount}}, upsert=True)
        collection.update_one({'_id': member.id}, {'$inc':{'Wallet':amount}}, upsert=True)
        await ctx.send(f'{ctx.author.mention} Successfully sent {amount} points to {member.mention}')

    @commands.command(aliases = ['bet'])
    async def gamble(self, ctx, amount):
        await get_user(ctx.author.id)
        collection.update_one({'_id':ctx.author.id}, {'$inc':{'Bank_Space':3}}, upsert=True) 
        amount = int(amount)
        if amount == None:
            await ctx.send(f"{ctx.author.mention} bruh enter how much u want to gamble")
            return
        if amount < 5:
            await ctx.send(f"{ctx.author.mention} you can't bet less than 5 points")
            return
        bank = collection.find({'_id': ctx.author.id})
        for m in bank:
            money = m['Wallet']
            if money < amount:
                await ctx.send("You don't have that much points in your wallet to gamble with")
                return
        else:
            comp_outcomess1 = ['1','2','3','4','5','6','7','8','9','10']
            c_outcome1 = random.choice(comp_outcomess1)
            c_outcome2 = random.choice(comp_outcomess1)
            p_outcome1 = random.choice(comp_outcomess1)
            p_outcome2 = random.choice(comp_outcomess1)
            ct_outcome = int(c_outcome1) + int(c_outcome2)
            pt_outcome = int(p_outcome1) + int(p_outcome2)
            if ct_outcome > pt_outcome:
                em = discord.Embed(description = f"You lost {amount} points. Im actually too good at gambling", colour = discord.Colour(0xec0909))
                em.set_author(name = f"{ctx.author.display_name}'s losing bet")
                em.add_field(name = f"{ctx.author.display_name}'s roll:", value = f"`{p_outcome1}` + `{p_outcome2}` = **{pt_outcome}**")
                em.add_field(name = "Shizuku's roll:".format(bot.user), value = f"`{c_outcome1}` + `{c_outcome2}` = **{ct_outcome}**")
                em.set_footer(text = "lol sucks to suck")
                collection.update_one({'_id': ctx.author.id}, {'$inc':{'Wallet':-1*amount}}, upsert=True)
                collection.update_one({'_id':ctx.author.id}, {'$inc':{'Bank_Space':1}}, upsert=True) 
                await ctx.send(embed=em)
            elif ct_outcome < pt_outcome:
                percets = [1, 2, 0.3, 0.4, 0.5, 0.6, 0.8, 0.9, 0.2, 0.25, 0.45]
                percents = random.choice(percets)
                percentss = percents*100
                amount = int(percents*amount)
                em = discord.Embed(description = f"You won {amount} points ({percentss}% of your original bet)", colour = discord.Colour(0x8ff57d))
                em.set_author(name = f"{ctx.author.display_name}'s winning bet")
                em.add_field(name = f"{ctx.author.display_name}'s roll:", value = f"`{p_outcome1}` + `{p_outcome2}` = **{pt_outcome}**")
                em.add_field(name = "Shizuku's roll:".format(bot.user), value = f"`{c_outcome1}` + `{c_outcome2}` = **{ct_outcome}**")
                em.set_footer(text = "gawd dammint i swear u cheated")
                collection.update_one({'_id': ctx.author.id}, {'$inc':{'Wallet':amount}}, upsert=True)
                collection.update_one({'_id':ctx.author.id}, {'$inc':{'Bank_Space':1}}, upsert=True) 
                await ctx.send(embed=em)
            elif ct_outcome == pt_outcome:
                em = discord.Embed(description = f"Bruh how did we tie- this shit rigged", colour = discord.Colour(0x8ff57d))
                em.set_author(name = f"how lame...")
                em.add_field(name = f"{ctx.author.display_name} roll:", value = f"`{p_outcome1}` + `{p_outcome2}` = **{pt_outcome}**")
                em.add_field(name = "Shizuku's roll:".format(bot.user), value = f"`{c_outcome1}` + `{c_outcome2}` = **{ct_outcome}**")
                em.set_footer(text = "gawd dammint i swear u cheated")
                collection.update_one({'_id':ctx.author.id}, {'$inc':{'Bank_Space':1}}, upsert=True) 
                await ctx.send(embed=em)

    @commands.command(aliases = ['lb'])
    async def leaderboard(self, ctx, x = 1):
        await ctx.message.delete()
        guild = ctx.author.guild
        total = []
        ids = {}
        item = collection.find({})
        for i in item:
            wallet = i['Wallet']
            bank = i['Bank']
            id_ = i['_id']
            totals = int(wallet)+int(bank)
            total.append(totals)
            ids[totals] = int(id_)


        total = sorted(total, reverse=True)

        await ctx.send(f"__**Top 10 Richest People in {guild.name}**__")
        index=1
        for amt in total:
            ids_ = ids[amt]
            member = self.bot.get_user(ids_)
            name = member.display_name
            await ctx.send(f"#{index}. **{name}**: `{amt} points`")
            if index == x+9:
                break
            else:
                index += 1


    @commands.command(aliases=['adv'])
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def adventure(self, ctx):
        collection.update_one({'_id':ctx.author.id}, {'$inc':{'Bank_Space':1}}, upsert=True) 
        await ctx.send(f"{ctx.author.mention} you might lose points when you go on a adventure..are you sure? yes or no?")
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
        msg = (await self.bot.wait_for('message', check=check)).content
        if msg == 'yes':
            poss = ['m','m','m','d','d','d','d']
            possi = random.choice(poss)
            if possi == 'm':
                collection.update_one({'_id':ctx.author.id}, {'$inc':{'Bank_Space':10}}, upsert=True) 
                places = ["mars","france","Great Wall of China"]
                placesf = ['camino', 'beverly hills', "grandma's house", "forest"]
                placest = ['burger king', 'sketchy basement']
                place1 = random.choice(places)
                place2 = random.choice(placesf)
                place3 = random.choice(placest)
                placess = place1, place2, place3
                await ctx.send(f"{ctx.author.mention} Where would you like to go today? `{place1}`, `{place2}`, `{place3}`")
                def check(g):
                    return g.author == ctx.author and g.channel == ctx.channel
                msg = (await self.bot.wait_for('message', check=check)).content
                if any(word in msg for word in placess):
                    times = random.randint(5, 15)
                    await ctx.send(f"{ctx.author.mention} You went on a hunt for points at {msg}! You will be back in `{times} seconds`")
                    await asyncio.sleep(times)
                    points = random.randint(5,15)
                    await ctx.send(f"{ctx.author.mention} You have arrived back from {msg} with **{points} points**")
                    collection.update({'_id':ctx.author.id}, {'$inc':{'Wallet':points}}, upsert=True)
                else:
                    await ctx.send(f"{ctx.author.mention} bruh thats not a correct place")
                    collection.update({'_id':ctx.author.id}, {'$inc':{'Wallet':10}}, upsert=True)
            elif possi == 'd':
                collection.update_one({'_id':ctx.author.id}, {'$inc':{'Bank_Space':10}}, upsert=True) 
                places = ["mars","france","Great Wall of China"]
                placesf = ['camino', 'beverly hills', "grandma's house", "forest"]
                placest = ['burger king', 'sketchy basement']
                place1 = random.choice(places)
                place2 = random.choice(placesf)
                place3 = random.choice(placest)
                placess = place1, place2, place3
                await ctx.send(f"{ctx.author.mention} Where would you like to go today? `{place1}`, `{place2}`, `{place3}`")
                def check(msg):
                    return msg.author == ctx.author and msg.channel == ctx.channel
                msg = (await self.bot.wait_for('message', check=check)).content
                if any(word in msg for word in placess):
                    times = random.randint(15, 20)
                    await ctx.send(f"{ctx.author.mention} You went on a hunt for points at {msg}! You will be back in `{times} seconds`")
                    await asyncio.sleep(times)
                    points = random.randint(1,30)
                    sta = ['oh god pls save me','i have the power of god and anime on my side','time to flee','i will initiate hate crime if you rob me','pft imagine robbing someone as innocent as me']
                    state = random.choice(sta)
                    ppl = ['monkeys','owls','clowns','bandits','chicken','mermaids','dweebs']
                    people = random.choice(ppl)
                    mes = await ctx.send(f"{ctx.author.mention} oh gawd looks like you were beaten up by a bunch of {people} at {msg}...")
                    await asyncio.sleep(1.5)
                    await mes.edit(content=f"Hurry! you have 25 seconds to type `{state}` to save yourself!")
                    def check(msg):
                        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in sta
                    try:
                        msg = (await self.bot.wait_for('message', timeout=5.0, check=check)).content
                        if any(word in msg for word in state): 
                            pay = random.randint(1,50)
                            mesg = await ctx.send(f"{ctx.author.mention} darn that was close- you were almost robbed by a hoard of **{people}**...")
                            await asyncio.sleep(1.5)
                            await mesg.edit(content=f"but instead you pulled a uno reverse and robbed **{pay} points** from them instead <a:poggu:44060014053425203>")
                            collection.update({'_id':ctx.author.id},{'$inc':{'Wallet':pay}}, upsert=True)
                            collection.update_one({'_id':ctx.author.id}, {'$inc':{'Bank_Space':2}}, upsert=True) 
                        else:
                            pay = random.randint(1,12)
                            mesgs = await ctx.send(f"{ctx.author.mention} gawd you didnt type the phrase correctly and was robbed and beaten up by a hurdle of **{people}**...")
                            await asyncio.sleep(1.5)
                            await mesgs.edit(content=f"as a result, you lost **{pay} points** <:um:861703464823816192>")
                            collection.update({'_id':ctx.author.id}, {'$inc':{'Wallet':-1*pay}}, upsert=True)
                            collection.update_one({'_id':ctx.author.id}, {'$inc':{'Bank_Space':2}}, upsert=True) 
                    except asyncio.exceptions.TimeoutError:
                        coins = random.choice(1,12)
                        msgt = await ctx.send(f"{ctx.author.mention} gawd you didnt type the phrase fast enough and was robbed and beaten up by a hurdle of **{people}**...")
                        await asyncio.sleep(1.5)
                        await msgt.edit(content=f"as a result, you lost **{coins} points** <:um:861703464823816192>")
                        collection.update({'_id':ctx.author.id}, {'$inc':{'Wallet':-1*coins}}, upsert=True)
                        collection.update_one({'_id':ctx.author.id}, {'$inc':{'Bank_Space':2}}, upsert=True) 
                else:
                    collection.update_one({'_id':ctx.author.id}, {'$inc':{'Bank_Space':1}}, upsert=True) 
                    await ctx.send(f"{ctx.author.mention} bruh thats not a correct place")
                    collection.update({'_id':ctx.author.id}, {'$inc':{'Wallet':10}}, upsert=True)
        elif msg == 'no':
            await ctx.send("alr bet i guess we're not going on a very exciting adventure..")
    @adventure.error
    async def adventure_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention} You can go on a adventure again in {round(error.retry_after, 1)} seconds")
    
    @commands.command(aliases=["slots"])
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def slot(self, ctx, amount):
        stats = collection.find({'_id':ctx.author.id})
        amount = int(amount)
        if stats == None:
            await get_user
        for x in stats:
            money = x['Wallet']
        if money < amount:
            await ctx.send(f"{ctx.author.mention} You don't have that much points in your wallet bruh")
            return
        if amount < 5:
            await ctx.send(f"{ctx.author.mention} You can't bet less that 5 points")
            return
        if amount < 0:
            await ctx.send(f"{ctx.author.mention} You can't bet negative points bruh")
            return
        """ Roll the slot machine """
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)
        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
        embed1=discord.Embed(title = f"{ctx.author.name}'s Slot Machine!", 
        color=discord.Color.random(),
        description=f"{a} {b} {c}")
        msg = await ctx.send(embed=embed1)
        await asyncio.sleep(0.5)
        embed2=discord.Embed(title = f"{ctx.author.name}'s Slot Machine!", 
        color=discord.Color.random(),
        description=f"{b} {a} {c}")
        await msg.edit(embed=embed2)
        await asyncio.sleep(0.7)
        embed3=discord.Embed(title = f"{ctx.author.name}'s Slot Machine!", 
        color=discord.Color.random(),
        description=f"{a} {b} {c}")
        await msg.edit(embed=embed3)
        await asyncio.sleep(0.5)
        embed4=discord.Embed(title = f"{ctx.author.name}'s Slot Machine!", 
        color=discord.Color.random(),
        description=f"{b} {a} {c}")
        await msg.edit(embed=embed4)
        await asyncio.sleep(0.6)
        embed5=discord.Embed(title = f"{ctx.author.name}'s Slot Machine!", 
        color=discord.Color.random(),
        description=f"{a} {c} {b}")
        await msg.edit(embed=embed5)
        await asyncio.sleep(0.6)

        if (a == b == c):
            embed9=discord.Embed(title = f"{ctx.author.name}'s Slot Machine!", color = discord.Color.green(),
            description=f"{slotmachine} All matching, you won **50 Points!** 🎉")
            await msg.edit(embed=embed9)
            collection.update({'_id':ctx.author.id}, {'$inc':{'Wallet':50}}, upsert=True)
        elif (a == b) or (a == c) or (b == c):
            embed90=discord.Embed(title = f"{ctx.author.name}'s Slot Machine!", color = discord.Color.green(),
            description=f"{slotmachine} All matching, you won **10 Points!** 🎉")
            await msg.edit(embed=embed90)
            collection.update({'_id':ctx.author.id}, {'$inc':{'Wallet':10}}, upsert=True)
        else:
            embed92=discord.Embed(title = f"{ctx.author.name}'s Slot Machine!", color = discord.Color.red(),
            description=f"{slotmachine} No match, you lost lmaoo 🎉")
            await msg.edit(embed=embed92)

def setup(bot):
    bot.add_cog(Points(bot))
