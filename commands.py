import discord
import random

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
            description="Hey, I'm just a work in progress so don't expect me to work!",
            color=discord.Color(int("AF27E4", 16))
        ),
        "random": discord.Embed(
            title="Random",
            description=f"Your random number is.... {random.random()}",
            color=discord.Color(int("AF27E4", 16))
        ),
    }
    # Set the footer using the set_footer method
    commands["embedlol"].set_footer(text="ma foot")
    commands["help"].set_footer(text="Bot by noerlol#0000")
    return commands
