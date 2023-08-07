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
# main.py

import discord
import sys
import requests
from var import tokenBot as TOKEN
from var import PREFIX
from commands import get_commands
from var import owner
from var import api_key
#define stopBot(message)
def stopBot(message):
    sys.exit(0)

def isBot(user):
    return user.bot

tag = "random funny"

# Create a Discord client (bot)
intents = discord.Intents.default()
intents.message_content = True  # Allows the bot to receive message events
client = discord.Client(intents=intents)

# GIF FETCH THINGY
async def fetch_gif_with_tag(tag):
    url = f'https://api.giphy.com/v1/gifs/random?api_key={api_key}&tag={tag}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        if 'data' in data and 'images' in data['data'] and 'original' in data['data']['images']:
            gif_url = data['data']['images']['original']['url']
            return gif_url
        else:
            print("Error parsing API response: 'image_original_url' key not found.")
            return None
    except requests.exceptions.RequestException as e:
        print("Error while fetching GIF from Giphy API:", e)
        return None
    except KeyError as e:
        print("Error parsing API response:", e)
        return None
# Event: When the bot is ready and connected to Discord
@client.event
async def on_ready():
    if api_key == "API_KEY_HERE":
        print(f"Successful login as {client.user} with prefix {PREFIX} and no Giphy API KEY.")
    else:
        print(f"Successful login as {client.user} with prefix {PREFIX}\nand Giphy API KEY {api_key}")
    await client.change_presence(activity=discord.Game(name=f'{PREFIX}help'))

# Event: When a message is received in a server the bot is a part of
@client.event
async def on_message(message):
    # Ignore messages from the bot itself to avoid an infinite loop
    if message.author == client.user:
        return
    # Ignore messages from other bots too
    if isBot(message.author):
        return

    if message.content == f"{PREFIX}stopthebotrightnow":
        if message.author.name == owner:
            stopBot(message)
            print(f"{message.author} directed the stopping of the bot.")
        else:
            print("A user tried to stop the bot while not being owner.")
            await message.channel.send(f"Sorry, you're not the owner of the bot, if you think this is a mistake edit the var.py file and replace the blank with username. You are {message.author} and from var.py is {owner}")

    global tag  # Declare the global tag variable to change it if needed

    if message.content.startswith(f"{PREFIX}settag "):
        tag = message.content[len(f"{PREFIX}settag "):]
        await message.channel.send(f"Tag set to `{tag}`.")
    elif message.content == f"{PREFIX}meme":
        await message.channel.send(f"Tag is {tag}")
        gif_url = await fetch_gif_with_tag(tag)
        if gif_url:
            await message.channel.send(gif_url)
        else:
            await message.channel.send("Oops, something went wrong while fetching the GIF.")


#            COMMMANDS.PY PART
             # Split the message into the command and arguments
    parts = message.content.split(" ", 1)
    command = parts[0].lower()
    arguments = parts[1] if len(parts) > 1 else ""

    # Get the commands dictionary using the get_commands function from commands.py
    commands = get_commands(client)

    # Check if the command is recognized
    if command.startswith(PREFIX) and command[len(PREFIX):] in commands:
        # Get the response from the commands dictionary
        response = commands[command[len(PREFIX):]]
        # If it's an embed, send it as an embed
        if isinstance(response, discord.Embed):
            await message.channel.send(embed=response)
        else:
            # Otherwise, send it as a normal message
            await message.channel.send(response)

# Run the bot with the provided token
client.run(TOKEN)
