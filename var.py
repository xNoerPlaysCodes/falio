import discord
with open("config.txt") as config:
    for line in config:
        if line.startswith("token"):
            token = line.strip().split('=', 1)
            tokenBot = line.strip().strip("'")
            break
intents = discord.Intents.default()
intents.message_content = True  # Allows the bot to receive message events
PREFIX = ";"
ENABLE_SLASH_COMMANDS = True # SLASH COMMANDS. Set to False capital F to turn off.
# ^^^^^^^^^^^^^^^ DOESNT WORK
