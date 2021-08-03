from discord.ext import commands

class Init(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

def setup(bot):
    bot.add_cog(Init(bot))