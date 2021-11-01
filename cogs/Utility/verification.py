# verification.py
# Verification part of the bot, verifies users ;-;
# Author: wHo#6933

import discord
from discord.ext import commands
from discord_components.component import ActionRow, Button, ButtonStyle

import random
import asyncio

class verificationCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.roles = {  # dict containing all roles & ids
            "sec1": 903673312452956181,
            "sec2": 903673384926330921,
            "sec3": 903673456778952734,
            "sec4": 903673461614973009,
            "sec5": 903673461614973009,

            "oak": 903679230959837196,
            "saga": 903679273750122546,
            "maple": 903679314040598529,
            "willow": 903678800817164348
        }

    @commands.command()
    async def verify(self, ctx):
        admin = discord.utils.get(ctx.guild.roles, id=903654645707186236) # get admin role to bypass checks

        if len(ctx.author.roles) > 1 and admin not in ctx.author.roles:                        # check if user has a role other than @everyone
            await ctx.send(":x: You are already verified!")  # if yes > user is verified
            return

        options = [] # List to store all the options user chose

        randomColor = lambda: random.randint(0,255)
        color = int("0x%02X%02X%02X" % (randomColor(),randomColor(),randomColor()), 16) # Generates a random color then converts str to hex

        # 1. Level (sec 1, 2, 3, 4, 5)
        levelEmbed = discord.Embed(title="What is your level?", color=color)

        levelButtons = [ActionRow(
            Button(label="Secondary 1", style=ButtonStyle.blue, custom_id="btn_sec1"),
            Button(label="Secondary 2", style=ButtonStyle.red, custom_id="btn_sec2"),
            Button(label="Secondary 3", style=ButtonStyle.red, custom_id="btn_sec3"),
            Button(label="Secondary 4", style=ButtonStyle.gray, custom_id="btn_sec4"),
            Button(label="Secondary 5", style=ButtonStyle.gray, custom_id="btn_sec5"),
        )]

        disabledLevelButtons = [ActionRow(
            Button(label="Secondary 1", style=ButtonStyle.blue, custom_id="btn_sec1", disabled=True),
            Button(label="Secondary 2", style=ButtonStyle.red, custom_id="btn_sec2", disabled=True),
            Button(label="Secondary 3", style=ButtonStyle.red, custom_id="btn_sec3", disabled=True),
            Button(label="Secondary 4", style=ButtonStyle.gray, custom_id="btn_sec4", disabled=True),
            Button(label="Secondary 5", style=ButtonStyle.gray, custom_id="btn_sec5", disabled=True),
        )]

        levelMsg = await ctx.send(embed=levelEmbed, components=levelButtons)

        while True:  # while loop to wait for input till user responds
            try:
                res = await self.bot.wait_for("button_click", timeout=60) # A timeout of 60 secs
                if res.channel == ctx.channel and res.user == ctx.author:
                    if res.component.custom_id == "btn_sec1":
                        await self.respond(res, "Secondary 1 was chosen!")
                        await levelMsg.edit(embed=levelEmbed, components=disabledLevelButtons)
                        options.append("sec1")
                    if res.component.custom_id == "btn_sec2":
                        await self.respond(res, "Secondary 2 was chosen!")
                        await levelMsg.edit(embed=levelEmbed, components=disabledLevelButtons)
                        options.append("sec2")
                    if res.component.custom_id == "btn_sec3":
                        await self.respond(res, "Secondary 3 was chosen!")
                        await levelMsg.edit(embed=levelEmbed, components=disabledLevelButtons)
                        options.append("sec3")
                    if res.component.custom_id == "btn_sec4":
                        await self.respond(res, "Secondary 4 was chosen!")
                        await levelMsg.edit(embed=levelEmbed, components=disabledLevelButtons)
                        options.append("sec4")
                    if res.component.custom_id == "btn_sec5":
                        await self.respond(res, "Secondary 5 was chosen!")
                        await levelMsg.edit(embed=levelEmbed, components=disabledLevelButtons)
                        options.append("sec5")
                    break
                else:
                    await self.respond(res, "Lmao this isn't your button :>")
            except asyncio.TimeoutError:
                await ctx.reply(":x: You took too long to respond :<")
                await levelMsg.edit(embed=levelEmbed, components=disabledLevelButtons)
                return
        
        # 2. House
        color = int("0x%02X%02X%02X" % (randomColor(),randomColor(),randomColor()), 16) # regenerate color again

        houseEmbed = discord.Embed(title="What is your house?", color=color)

        houseButtons = [ActionRow(
            Button(label="Oak", style=ButtonStyle.green, custom_id="btn_oak"),
            Button(label="Saga", style=ButtonStyle.green, custom_id="btn_saga"),
            Button(label="Maple", style=ButtonStyle.green, custom_id="btn_maple"),
            Button(label="Willow", style=ButtonStyle.green, custom_id="btn_willow"),
        )]

        disabledHouseButtons = [ActionRow(
            Button(label="Oak", style=ButtonStyle.green, custom_id="btn_oak", disabled=True),
            Button(label="Saga", style=ButtonStyle.green, custom_id="btn_saga", disabled=True),
            Button(label="Maple", style=ButtonStyle.green, custom_id="btn_maple", disabled=True),
            Button(label="Willow", style=ButtonStyle.green, custom_id="btn_willow", disabled=True),
        )]

        houseMsg = await ctx.send(embed=houseEmbed, components=houseButtons)

        while True:  # while loop to wait for input till user responds
            try:
                res = await self.bot.wait_for("button_click", timeout=60) # A timeout of 60 secs
                if res.channel == ctx.channel and res.user == ctx.author:
                    if res.component.custom_id == "btn_oak":
                        await self.respond(res, "Oak was chosen!")
                        await houseMsg.edit(embed=houseEmbed, components=disabledHouseButtons)
                        options.append("oak")
                    if res.component.custom_id == "btn_saga":
                        await self.respond(res, "Saga was chosen!")
                        await houseMsg.edit(embed=houseEmbed, components=disabledHouseButtons)
                        options.append("saga")
                    if res.component.custom_id == "btn_maple":
                        await self.respond(res, "Maple was chosen!")
                        await houseMsg.edit(embed=houseEmbed, components=disabledHouseButtons)
                        options.append("maple")
                    if res.component.custom_id == "btn_willow":
                        await self.respond(res, "Willow was chosen!")
                        await houseMsg.edit(embed=houseEmbed, components=disabledHouseButtons)
                        options.append("willow")
                    break
                else:
                    await self.respond(res, "Lmao this isn't your button :>")
            except asyncio.TimeoutError:
                await ctx.reply(":x: You took too long to respond :<")
                await houseMsg.edit(embed=houseEmbed, components=disabledHouseButtons)
                return
                
        # Give respective roles to user
        for i in options:
            try:
                role = ctx.guild.get_role(self.roles[i]) # refer to the dic and get role id
                await ctx.author.add_roles(role)
            except Exception as e:
                await ctx.send(f":x: There was an error, pls report :|\nLog:\n```{e}```")
                return

        await ctx.reply(":white_check_mark: Roles added!")

    async def respond(self, res, content):
        await res.respond(content=content)

# Link cog to main bot
def setup(bot):
    bot.add_cog(verificationCommand(bot))