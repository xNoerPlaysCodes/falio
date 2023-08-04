import discord
# enter bot token here:
tokenBot = "Bot Token Here"
intents = discord.Intents.default()
intents.message_content = True  # Allows the bot to receive message events
PREFIX = ";"
ENABLE_SLASH_COMMANDS = True # SLASH COMMANDS. Set to False capital F to turn off.
# ^^^^^^^^^^^^^^^ DOESNT WORK
