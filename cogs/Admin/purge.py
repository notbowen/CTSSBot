# purge.py
# Purges/clears messages in chat
# Author: wHo#6933

import discord
from discord.ext import commands
from discord.ext.commands.core import has_permissions

from functions import get_admins

class purgeCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["clear"])
    async def purge(ctx, amount=1):
        admins = await get_admins()

        if str(ctx.author.id) not in admins:
            await ctx.send(":x: You are not an admin >:(")
            return

        await ctx.channel.purge(limit=amount+1)

# Link cog to main bot
def setup(bot):
    bot.add_cog(purgeCommand(bot))