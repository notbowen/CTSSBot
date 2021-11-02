# functions.py
# A place to store all the "important" functions for the bot lol
# Author: wHo#6933

# Libraries
import json

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
async def readSuggestions():
    with open("./Suggestions/suggestions.json", "r")as f:
        data = json.load(f)
        f.close()

    return data

async def writeSuggestions(dic : dict):
    with open("./Suggestions/suggestions.json", "w")as f:
        data = json.dump(dic, f, indent=4) # indent for formatting
        f.close()