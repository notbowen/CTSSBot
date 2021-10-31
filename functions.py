# functions.py
# A place to store all the "important" functions for the bot lol
# Author: wHo#6933

async def get_admins():
    # Returns a list of admin IDs, stored in STRINGs
    with open("admins.txt")as f:
        admins = f.readlines()
        f.close()

    return admins
