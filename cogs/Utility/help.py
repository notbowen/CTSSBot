# help.py
# Help command for CTSS bot
# Author: wHo#6933

import discord
from discord.ext import commands

from functions import check_admin, generateRandomColor

class helpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Help", color=0x66cdaa)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/903696474951520397/904335874483965962/logo.png") # CTSS Logo
        embed.set_footer(text=f"Requested by: {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")

        # Adds fields to the embed
        # TODO: Add more commands to be displayed
        embed.add_field(name="verify:",
                        value="Verifies the user.",
                        inline=False)
        embed.add_field(name="sourceCode:",
                        value="Sends the link of the source code.",
                        inline=False)
        embed.add_field(name="ping:",
                        value="Displays the latency of the bot.",
                        inline=False)

        # Sends the embed
        await ctx.send(embed=embed)

    @commands.command()
    async def adminHelp(self, ctx):
        # Check if user is an admin
        if await check_admin(str(ctx.author.id)) == False:
            await ctx.send(":x: Only admins can access this command lmao :/")
            return

        # Embed
        embed = discord.Embed(title="Help", color=await generateRandomColor())
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/903696474951520397/904335874483965962/logo.png") # CTSS Logo
        embed.set_footer(text=f"Requested by: {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")

        # Adds fields to the embed
        # TODO: Add more commands to be displayed
        embed.add_field(name="purge(amount):",
                        value="Deletes a specified amount of messages, defaults to 1 if the amount is not specified.",
                        inline=False)

        # Sends the embed
        await ctx.send(embed=embed)

# Link cog to main bot
def setup(bot):
    bot.add_cog(helpCommand(bot))