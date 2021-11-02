# suggestions.py
# Code to handle submitting and reviewing suggestions.
# Author: wHo#6933

# Plans:
# 1. Submit suggestion command
# 2. List pending suggestions command
# 3. Accept/Decline suggestions command

# Json format:
# {
#    "id" (int): {
#       "user": userId (int),
#       "suggestion": suggestion (str)
#       "status": "accepted", "pending", "declined" (str, either 3)
#       }
# }

import discord
from discord.ext import commands

import random

from discord.ext.commands.core import command

from functions import readSuggestions, writeSuggestions, check_admin

class suggestionsCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Submit suggestion
    @commands.command()
    async def suggest(self, ctx, *, suggestion=""):
        # check if suggestion is empty
        if suggestion == "":
            await ctx.send(":x: Empty suggestion >:(")
            return

        data = await readSuggestions()

        data[max(data.keys()) + 1] = {  # get highest id, +1, and add content to it
            "user": int(ctx.author.id),
            "suggestion": suggestion,
            "status": "pending"
        }

        await writeSuggestions(data)
        await ctx.reply(random.choice([":white_check_mark: Your suggestion has been sent for review :D", ":white_check_mark: Your suggestion has been sent for review :>"]))

    # List pending commands
    # Admin only ;-;
    """WORK IN PROGRESS"""
    @commands.command()
    async def listSuggestions(self, ctx):
        if await check_admin(str(ctx.author.id)) == False:
            await ctx.reply(":x: This command is only for admins :<")
            return

        data = await readSuggestions()

# Link cog to main bot
def setup(bot):
    bot.add_cog(suggestionsCommand(bot))