#       ii           iii    BBBBBBBBBBB     GGGGGGGGGGGGGG      TTTTTTTTTTTTTTTTT       K   K
#       iii         iiii    B         B     G                           T               K  K
#       iiiii      iiiii    B         B     G                           T               K K
#       iiiiiii   iiiiii    B         B     G                           T               KKK
#       iiiiiiiiiiiiiiii    BBBBBBBBBB      G                           T               K  K
#       i              i    B         B     GGGGGGGGGGGGG               T               K   K
#       i              i    B         B     G           G               T               K     K
#       i              i    B         B     G           G               T               K      K
#       i              i    BBBBBBBBBBB     GGGGGGGGGGGGG               T               K       K
#                                                                                                   .py
#
# CONFIG / VARIABLES and OTHER STUFF
#
# var.py
import sys
import discord

def hardPrefixMaxCharCount():
    print(f"PREFIX is higher than 5. '{PREFIX}' is not valid. Exception Occurred.")
    sys.exit(0)

def ThrowIllegalExeception():
    print('Illegal Exception in Line 16 of var.py, "TOKEN" variable, "BOT_TOKEN_HERE" is not a valid Discord Bot Token and should be changed to a valid Discord Bot Token.')
    sys.exit(0)

# MBGTK and regular bot stuff here:
# enter bot token here:

tokenBot = "BOT_TOKEN_HERE"
intents = discord.Intents.default()
intents.message_content = True  # Allows the bot to receive message events
if tokenBot == "BOT_TOKEN_HERE":
    ThrowIllegalExeception()
PREFIX = ";" # should not contain spaces after so 'owo! ' invalid while 'owo!' is vaid
prcount = len(PREFIX)
if prcount > 5:
    hardPrefixMaxCharCount()
ENABLE_SLASH_COMMANDS = True # SLASH COMMANDS. Set to False capital F to turn off.
# ^^^^^^^^^^^^^^^ DOESNT WORK
footer_text = "Bot by noerlol#0000"
owner = "noerlol"
# The bot owner username if they have no tag at the end of name do only the name no #0000 for example not noerlol#0000 but noerlol or anything and if they have a tag do this UserName#1234 and replace with correct

#           To get current prefix enter {PREFIX} in PlayingGame
PlayingGame = f"{PREFIX}help"

# added functionality of meme (Gifs using Giphy) thing using meme command (giphy)
api_key = "API_KEY_HERE"
# Your Giphy API Key!
