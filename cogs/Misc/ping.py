# ping.py
# Ping command
# Author: wHo#6933

import discord
from discord.ext import commands

class pingCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"Pong!\nLatency: **{str(round(self.bot.latency, 2))}**ms")

# Link cog to main bot
def setup(bot):
    bot.add_cog(pingCommand(bot))