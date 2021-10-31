# sourceCode.py
# Code that returns the source code of the bot
# Author: wHo#6933

import discord
from discord.ext import commands

class sourceCodeCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sourceCode(self, ctx):
        await ctx.send("Source Code: https://github.com/wHo69/CTSSBot")

# Link cog to main bot
def setup(bot):
    bot.add_cog(sourceCodeCommand(bot))