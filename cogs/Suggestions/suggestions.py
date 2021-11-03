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
from discord import embeds
from discord.ext import commands
from discord_components import ActionRow, Button, ButtonStyle

import random
import asyncio

from discord.ext.commands.core import command

from functions import readSuggestions, writeSuggestions, check_admin, generateRandomColor

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
    """BUGGED"""
    @commands.command()
    async def listSuggestions(self, ctx, resultsPerPage="5"):
        await ctx.reply("WARNING: This part of the code is still WIP, there would be like 69 bugs :<")

        if await check_admin(str(ctx.author.id)) == False:
            await ctx.reply(":x: This command is only for admins :<")
            return

        if not resultsPerPage.isdigit():
            await ctx.send(":x: Invalid results per page value :<")
            return

        data = await readSuggestions()
        idList = [] # List of suggestion IDs to be displayed

        # Populate list
        tmp = []
        for i in data.keys():
            tmp.append(i)
            if i % int(resultsPerPage) == 0 and i != 0 or i == list(data.keys())[-1]: # checks if: it is the max number of result per page, or it is the last suggestion
                idList.append(tmp)
                tmp = []

        # Display data
        color = await generateRandomColor()
        embed = discord.Embed(title="Suggestions", color=color)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/903696474951520397/904335874483965962/logo.png") # CTSS Logo
        embed.set_footer(text=f"Requested by: {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")

        index = 0

        for i in idList[index]:
            embed.add_field(name=f"Suggestion #{i} by {ctx.author.name}#{ctx.author.discriminator}",
                            value=f"Suggestion: {data[i]['suggestion']}",
                            inline=False)

        await ctx.send(embed=embed)

# Link cog to main bot
def setup(bot):
    bot.add_cog(suggestionsCommand(bot))