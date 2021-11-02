# errorHandler.py
# Script to handle bot errors that may occur due to crap code :<
# Yeeted from: https://vcokltfre.dev/tutorial/12-errors/
# Author: wHo#6933

import discord
from discord.ext import commands

class errorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx : commands.Context, error : commands.CommandError):
        # Global error handler cog
        if isinstance(error, commands.CommandNotFound):
            return # no action for command not found
        elif isinstance(error, commands.CommandOnCooldown):
            message = f"This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds."
        elif isinstance(error, commands.MissingPermissions):
            message = "You are missing the required permissions to run this command!"
        elif isinstance(error, commands.UserInputError):
            message = "Something about your input was wrong, please check your input and try again!"
        else:
            message = f"Oh no! Something went wrong while running the command!\nError log: \n```diff\n- {error}```"

        await ctx.send(message)

# Link cog to main bot
def setup(bot):
    bot.add_cog(errorHandler(bot))