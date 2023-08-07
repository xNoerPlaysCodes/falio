# commands.py

import discord
import random
import sys
from var import footer_text as footer
from var import PREFIX
from var import api_key
# ^^^^^^^^^^^^^^^^^^^ This is the Bot by noerlol thingy, you can edit if you want.
if api_key == "API_KEY_HERE":
    meme_enabled = "false"
else:
    meme_enabled = "true"

def stopBot():
    sys.exit(0)

def get_commands(client):
    commands = {
        "hello": f"Hello there, I'm {client.user}",
        "ping": f"Pong! {round(client.latency * 1000)}ms",
        "embedlol": discord.Embed(
            title="A discord embed.",
            description="A discord description by noerlol",
            color=discord.Color(int("AF27E4", 16)),
        ),
        "help": discord.Embed(
            title="Help Menu",
            description=f"""
            {PREFIX}hello
            {PREFIX}ping
            {PREFIX}embedlol
            {PREFIX}help (This!)
            {PREFIX}random
            {PREFIX}meme (Is meme enabled? -> {meme_enabled})
            {PREFIX}settag (Tag)
            ^^^^^^^^^^^^^^^^^^^^ Sets Gifs what will be about to (Tag)
            """,
            color=discord.Color(int("AF27E4", 16))
        ),
        "random": discord.Embed(
            title="Random",
            description=f"Your random number is.... {random.random()}",
            color=discord.Color(int("AF27E4", 16))
        ),
        "about": discord.Embed(
        title="MBGTK.py",
        description=f"Hey! I'm a open source discord bot designed for general purposes developed by xNoerPlays. You can find me on https://github.com/xNoerPlaysCodes/mbgtk-python/ This specific one's prefix is {PREFIX}.",
        color=discord.Color(int("AF27E4", 16)),
        ),
#       "stopthebotrightnow": This is defined in main.py Line 28
#       "meme": Meme command defined in main.py
#       "settag": Defined in main.py
    }
    # Set the footer using the set_footer method
    commands["embedlol"].set_footer(text="ma foot")
    commands["help"].set_footer(text=footer)
    commands["about"].set_footer(text=footer)
    return commands
