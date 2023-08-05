import discord
# enter bot token here:
tokenBot = "BOT_TOKEN_HERE"
intents = discord.Intents.default()
intents.message_content = True  # Allows the bot to receive message events
PREFIX = ";"
ENABLE_SLASH_COMMANDS = True # SLASH COMMANDS. Set to False capital F to turn off.
# ^^^^^^^^^^^^^^^ DOESNT WORK
footer_text = "Bot by noerlol#0000"
# Anywhere in commands.py with commands["COMMAND_NAME_HERE"].set_footer(text=footer) the text=footer will use this.
