# functions.py
# A place to store all the "important" functions for the bot lol
# Author: wHo#6933

# Libraries
import json
import os
import random

async def generateRandomColor():
    randomColor = lambda: random.randint(0,255)
    color = int("0x%02X%02X%02X" % (randomColor(),randomColor(),randomColor()), 16)
    return color

# Admin matters
async def get_admins():
    # Returns a list of admin IDs, stored in STRINGs
    with open("admins.txt")as f:
        admins = f.readlines()
        f.close()

    return admins

async def check_admin(id: str):
    # Checks if an ID (STRING) is an admin
    admins = await get_admins()
    return (id in admins) # if id in admins, yes
                          # if id not in admins, no
                        
# Suggestion file handling
suggestionFilePath = os.path.join(os.path.dirname(__file__), "cogs/Suggestions/suggestions.json")

async def readSuggestions():
    with open(suggestionFilePath, "r")as f:
        data = json.load(f)
        f.close()

    # make keys into integers for ez parsing
    data = {int(key):dict(value) for key,value in data.items()}

    return data

async def writeSuggestions(dic : dict):
    with open(suggestionFilePath, "w")as f:
        data = json.dump(dic, f, indent=4) # indent for formatting
        f.close()