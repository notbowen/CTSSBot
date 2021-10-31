# Official CTSS Bot
# Author: wHo#6933

import discord
from discord.ext import commands

import os

# Bot class setup
bot = commands.Bot(
    command_prefix=["c ", "C ", "c", "C"],
    case_insensitive=True
    )
bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="chelp"))
    print("Bot initialised :D")

# Load cogs recursively
# File Structure should follow the form of: ./cogs/folder/code.py
# Where folder is the category of the script
for f in os.listdir('./cogs'):
    if f.endswith(".py"):
        bot.load_extension(f'cogs.{f[:-3]}')
        print("Loaded cog: " + f[:-3])
    else:
        for x in os.listdir(f"./cogs/{f}"):
            if x.endswith(".py"):
                bot.load_extension(f'cogs.{f}.{x[:-3]}')
                print("Loaded cog: " + f[:-3])

# Run the bot
token = os.getenv("CTSS Bot Token")
bot.run(token)