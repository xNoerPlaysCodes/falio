import discord
# enter bot token here:
tokenBot = "BOT_TOKEN_HERE"
intents = discord.Intents.default()
intents.message_content = True  # Allows the bot to receive message events
PREFIX = ";"
ENABLE_SLASH_COMMANDS = True # SLASH COMMANDS. Set to False capital F to turn off.
# ^^^^^^^^^^^^^^^ DOESNT WORK
footer_text = "Bot by noerlol#0000" # Credits, if you want you can change, changes the footer in most commands.
owner = "noerlol"
# The bot owner username if they have no tag at the end of name do only the name no #0000 for example not noerlol#0000 but noerlol or anything and if they have a tag do this UserName#1234 and replace with correct
