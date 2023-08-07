# var.py
import sys
import discord

def hardPrefixMaxCharCount():
    print(f"PREFIX is higher than 5. '{PREFIX}' is not valid. Exception Occurred.")
    sys.exit(0)

# MBGTK and regular bot stuff here:
# enter bot token here:
tokenBot = "BOT_TOKEN_HERE"
intents = discord.Intents.default()
intents.message_content = True  # Allows the bot to receive message events
PREFIX = ";" # should not contain spaces after so 'owo! ' invalid while 'owo!' is vaid
prcount = len(PREFIX)
if prcount > 5:
    hardPrefixMaxCharCount()
ENABLE_SLASH_COMMANDS = True # SLASH COMMANDS. Set to False capital F to turn off.
# ^^^^^^^^^^^^^^^ DOESNT WORK
footer_text = "Bot by noerlol#0000"
owner = "noerlol"
# The bot owner username if they have no tag at the end of name do only the name no #0000 for example not noerlol#0000 but noerlol or anything and if they have a tag do this UserName#1234 and replace with correct

# added functionality of meme (Gifs using Giphy) thing using meme command (giphy)
api_key = "API_KEY_HERE"
# Your Giphy API Key!
