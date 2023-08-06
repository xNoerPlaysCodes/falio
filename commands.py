import discord
import random
import sys
from var import footer_text as footer
from var import PREFIX
# ^^^^^^^^^^^^^^^^^^^ This is the Bot by noerlol thingy, you can edit if you want.

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
            description=";hello\n;ping\n;embedlol\n;help (This!)\n;random",
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
    }
    # Set the footer using the set_footer method
    commands["embedlol"].set_footer(text="ma foot")
    commands["help"].set_footer(text=footer)
    commands["about"].set_footer(text=footer)
    return commands
