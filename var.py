#       ii           iii    BBBBBBBBBBB     GGGGGGGGGGGGGG      TTTTTTTTTTTTTTTTT       K      K
#       iii         iiii    B         B     G                           T               K    K
#       iiiii      iiiii    B         B     G                           T               K  K
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
import os
import time

fileSystemStruct = ["main.py", "var.py", "banned_users.py", "user_tickets.json", "log_channel.json"]
folder_path = os.path.dirname(os.path.abspath(__file__))

for filename in fileSystemStruct:
    file_path = os.path.join(folder_path, filename)
    if not os.path.isfile(file_path):
        print(f"File '{filename}' is missing in the folder.")

print("All required files are present, continuing start-up")
time.sleep(1)

def hardPrefixMaxCharCount():
    print(f"PREFIX is higher than 5. '{PREFIX}' is not valid. Exception Occurred.")
    sys.exit(0)

def ThrowIllegalExeception(x):
    print(x)
    sys.exit(0)

# MBGTK and regular bot stuff here:
# enter bot token here:

tokenBot = "BOT_TOKEN_HERE"
intents = discord.Intents.default()
intents.message_content = True  # Allows the bot to receive message events
if tokenBot == "BOT_TOKEN_HERE":
    ThrowIllegalExeception('Illegal Exception in Line 16 of var.py, "TOKEN" variable, "BOT_TOKEN_HERE" is not a valid Discord Bot Token and should be changed to a valid Discord Bot Token.')
PREFIX = "!" # Bot prefix
prcount = len(PREFIX)
if prcount > 6:
    hardPrefixMaxCharCount()
ENABLE_SLASH_COMMANDS = True # SLASH COMMANDS. Set to False capital F to turn off.
# ^^^^^^^^^^^^^^^ DOESNT WORK
footer_text = "Bot by noerlol#0000"
owner = "noerlol"
color = 'AF27E4'
# The bot owner username if they have no tag at the end of name do only the name no #0000 for example not noerlol#0000 but noerlol or anything and if they have a tag do this UserName#1234 and replace with correct

#           To get current prefix enter {PREFIX} in PlayingGame
PlayingGame = f"I'm in testing mode."

# added functionality of meme (Gifs using Giphy) thing using meme command (giphy)
api_key = "API_KEY_HERE"
# Your Giphy API Key!