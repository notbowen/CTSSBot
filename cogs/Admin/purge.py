# purge.py
# Purges/clears messages in chat
# Author: wHo#6933

import discord
from discord.ext import commands
from discord.ext.commands.core import has_permissions

from functions import check_admin

class purgeCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["clear"])
    async def purge(ctx, amount=1):
        if await check_admin(str(ctx.author.id)) == False:
            await ctx.send(":x: You are not an admin >:(")
            return

        await ctx.channel.purge(limit=amount+1)

# Link cog to main bot
def setup(bot):
    bot.add_cog(purgeCommand(bot))