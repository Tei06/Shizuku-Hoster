import discord
from discord.ext import commands
from discord.ext.commands import context
bot = discord.Client()

class Custom(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg):
        brian_words = ('brian','Brian','BRIAN')
        if any(word in msg.content for word in brian_words):
            await msg.add_reaction('<petpigsniff:856645464895520788>')
            await msg.add_reaction('<a:hypechicken:863924954235928626>')
            await msg.add_reaction('<a:pandafight:855492137277587476>')
        lara_words = ('lara','Lara','LARA','lala')
        if any(word in msg.content for word in lara_words):
            await msg.add_reaction('🦷')
            await msg.add_reaction('🪥')
        tanu_words = ('tanu', 'Tanu', 'TANU', 'tanusha','TANUSHA')
        if any(word in msg.content for word in tanu_words):
            await msg.add_reaction('🫀')
        marco_words = ('marco', 'Marco','MARCO','marco he')
        if any(word in msg.content for word in marco_words):
            await msg.add_reaction('<:MonkaChrist:863920365121962004>')
            await msg.add_reaction('<:strangle:829566645835661323>')
        cait_words = ('caitlyn','cait','Cait','CAIT','CAITLYN')
        if any(word in msg.content for word in cait_words):
            await msg.add_reaction('<a:bellycat:842208740194254878>')
        ish_words = ('ishaan','Ishaan','ISHAAN')
        if any(word in msg.content for word in ish_words):
            await msg.add_reaction('<:swag:841427625478062100>')
            await msg.add_reaction('<:catheart:844942477084590080>')
def setup(bot):
    bot.add_cog(Custom(bot))