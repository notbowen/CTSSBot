# Official CTSS Bot
# Author: wHo#6933

# Libraries
import discord
from discord.ext import commands
from discord_components.client import DiscordComponents

import os
import termcolor

from keep_alive import keep_alive

# Bot class setup
bot = commands.Bot(
    command_prefix=["c ", "C ", "c", "C"],
    case_insensitive=True
    )
bot.remove_command("help")

@bot.event
async def on_ready():
    DiscordComponents(bot)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="chelp"))
    print(termcolor.colored("Bot initialised :D", "green"))

# Start the "server"
keep_alive()

# Load cogs recursively
# File Structure should follow the form of: ./cogs/folder/code.py
# Where folder is the category of the script
print(termcolor.colored("Loading cogs...", "yellow"))
for f in os.listdir('./cogs'):
    if f.endswith(".py"):
        bot.load_extension(f'cogs.{f[:-3]}')
        print(termcolor.colored("Loaded cog: " + f[:-3], "yellow"))
    else:
        for x in os.listdir(f"./cogs/{f}"):
            if x.endswith(".py"):
                bot.load_extension(f'cogs.{f}.{x[:-3]}')
                print(termcolor.colored("Loaded cog: " + x[:-3], "yellow"))
print(termcolor.colored("Cogs loaded :D", "yellow"))

# Run the bot
token = os.getenv("CTSS Bot Token")
bot.run(token)