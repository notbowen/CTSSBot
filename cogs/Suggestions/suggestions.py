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

from typing import List
import discord
from discord import embeds
from discord.ext import commands
from discord_components import ActionRow, Button, ButtonStyle, component

import random
import asyncio

from discord.ext.commands.core import command
from discord_components.interaction import InteractionEventType

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

        index = 0
        data = await readSuggestions()
        idList = [] # List of suggestion IDs to be displayed

        # Populate list
        tmp = []
        for i in data.keys():
            tmp.append(i)
            if i % int(resultsPerPage) == 0 and i != 0 or i == list(data.keys())[-1]: # checks if: it is the max number of result per page, or it is the last suggestion
                idList.append(tmp)
                tmp = []

        # buttons
        options = [ActionRow(
            Button(label="|<", style=ButtonStyle.gray, custom_id="btn_start"),
            Button(label="<", style=ButtonStyle.gray, custom_id="btn_left"),
            Button(label=">", style=ButtonStyle.gray, custom_id="btn_right"),
            Button(label=">|", style=ButtonStyle.gray, custom_id="btn_end")
        )]

        disabledOptions = [ActionRow(
            Button(label="|<", style=ButtonStyle.gray, custom_id="btn_start", disabled=True),
            Button(label="<", style=ButtonStyle.gray, custom_id="btn_left", disabled=True),
            Button(label=">", style=ButtonStyle.gray, custom_id="btn_right", disabled=True),
            Button(label=">|", style=ButtonStyle.gray, custom_id="btn_end", disabled=True)
        )]

        # Display data
        embed = await self.generateSuggestions(ctx, idList, data, 0)
        msg = await ctx.send(embed=embed, components=options)

        # handle button clicks
        while True:
            try:
                res = await self.bot.wait_for("button_click", timeout=60)
                if res.channel == ctx.channel and res.user == ctx.author:
                    if res.component.custom_id == "btn_start":
                        await res.respond(type=6, content="\u2800")
                        await msg.edit(embed=await self.generateSuggestions(ctx, idList, data, 0), components=options)
                        index = 0
                    if res.component.custom_id == "btn_left" and index != 0:
                        await res.respond(type=6, content="\u2800")
                        await msg.edit(embed=await self.generateSuggestions(ctx, idList, data, index-1), components=options)
                        index -= 1
                    elif res.component.custom_id == "btn_left" and index == 0:
                        await res.respond(type=6, content="\u2800")
                        await msg.edit(embed=await self.generateSuggestions(ctx, idList, data, index), components=options)
                    if res.component.custom_id == "btn_right" and index != (len(idList) - 1):
                        await res.respond(type=6, content="\u2800")
                        await msg.edit(embed=await self.generateSuggestions(ctx, idList, data, index+1), components=options)
                        index += 1
                    elif res.component.custom_id == "btn_right" and index == (len(idList) - 1):
                        await res.respond(type=6, content="\u2800")
                        await msg.edit(embed=await self.generateSuggestions(ctx, idList, data, index), components=options)
                    if res.component.custom_id == "btn_end":
                        await res.respond(type=6, content="\u2800")
                        await msg.edit(embed=await self.generateSuggestions(ctx, idList, data, (len(idList) - 1)), components=options)
                        index = len(idList) - 1
                else:
                    await self.respond(res, "Lmao this isn't your button :>")
            except asyncio.TimeoutError:
                await msg.edit(embed=embed, components=disabledOptions)
                break

    async def generateSuggestions(self, ctx, idList, data, index : int):
        color = await generateRandomColor()
        embed = discord.Embed(title=f"Suggestions, Page {index + 1}", color=color)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/903696474951520397/904335874483965962/logo.png") # CTSS Logo
        embed.set_footer(text=f"Page {index + 1}", icon_url=f"{ctx.message.author.avatar_url}")

        for i in idList[index]:
            embed.add_field(name=f"Suggestion #{i} by {ctx.author.name}#{ctx.author.discriminator}",
                            value=f"Suggestion: {data[i]['suggestion']}",
                            inline=False)

        return embed

    async def respond(self, res, content):
        await res.respond(content=content)

# Link cog to main bot
def setup(bot):
    bot.add_cog(suggestionsCommand(bot))