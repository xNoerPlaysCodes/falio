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

# Importing Packages
import discord
import sys
import requests
import random
import os
import json
# Importing variables from var.py
from var import tokenBot as TOKEN
from var import PREFIX
from var import owner
from var import api_key
from var import footer_text as footer
from var import PlayingGame

blank = ""

if api_key == "API_KEY_HERE":
    meme_enabled = "false"
else:
    meme_enabled = "true"

helpMenu = f"""
`{PREFIX}hello` - Hello!
`{PREFIX}ping` - Returns Client Latency.
`{PREFIX}help` - This!
`{PREFIX}random` - Returns a random number 100-1000
```GIF RELATED```
`{PREFIX}meme` - Returns a gif from giphy (Is meme enabled -> {meme_enabled})
`{PREFIX}settag` <tag> - Sets tag to the message you put in <tag>
```UTILITY RELATED```
`{PREFIX}ticket-add` - Creates a ticket
`{PREFIX}ticket-rm` - Removes your ticket if you have one
```FUN RELATED```
`{PREFIX}say <msg>` - Says that message!
            """

# DEFINTIONS OF CUST_FUNC
def loadHasTicket():
    filename = "user_tickets.json"
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"users_with_tickets": {}}
def saveHasTicket(data):
    filename = "user_tickets.json"
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def stopBot(message):
    sys.exit(0)

def isBot(user):
    return user.bot
#########################
tag = "random funny"

# Create a Discord client (bot)
intents = discord.Intents.default()
intents.message_content = True  # Allows the bot to receive message events
client = discord.Client(intents=intents)

#############################################################################################################
# GIF FETCH THINGY                                                                                          #
async def fetch_gif_with_tag(tag):                                                                          #
    url = f'https://api.giphy.com/v1/gifs/random?api_key={api_key}&tag={tag}'                               #
    try:                                                                                                    #
        response = requests.get(url)                                                                        #
        response.raise_for_status()  # Raise an exception for HTTP errors                                   #
        data = response.json()                                                                              #
        if 'data' in data and 'images' in data['data'] and 'original' in data['data']['images']:            #
            gif_url = data['data']['images']['original']['url']                                             #
            return gif_url                                                                                  #
        else:                                                                                               #
            print("Error parsing API response: 'image_original_url' key not found.")                        #
            return None                                                                                     #
    except requests.exceptions.RequestException as e:                                                       #
        print("Error while fetching GIF from Giphy API:", e)                                                #
        return None                                                                                         #
    except KeyError as e:                                                                                   #
        print("Error parsing API response:", e)                                                             #
        return None##########################################################################################
# Event: When the bot is ready and connected to Discord
@client.event
async def on_ready():
    if api_key == "API_KEY_HERE":
        print(f"Successful login as {client.user} with prefix {PREFIX} and no Giphy API KEY.")
    else:
        print(f"Successful login as {client.user} with prefix {PREFIX}\nand Giphy API KEY {api_key}")
    await client.change_presence(activity=discord.Game(name=PlayingGame))

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
        if meme_enabled == "true":
            await message.channel.send(f"Tag is {tag}")
            gif_url = await fetch_gif_with_tag(tag)
            if gif_url:
                await message.channel.send(gif_url)
            else:
                await message.channel.send("Oops, something went wrong while fetching the GIF.")
        elif meme_enabled == "false":
            await message.channel.send("Meme functionality is not configured in var.py, please change that.")
    elif message.content == f"{PREFIX}help":
        embed = discord.Embed(
            title="Help Menu",
            description=helpMenu,
            color=discord.Color(int("AF27E4", 16)),
        )
        embed.set_footer(text=footer),
        await message.channel.send(embed=embed)
    elif message.content == f"{PREFIX}hello":
        await message.channel.send(f"Hello there, I'm {client.user}!")
    elif message.content == f"{PREFIX}ping":
        await message.channel.send(f"Pong! {round(client.latency * 1000)}ms")
    elif message.content == f"{PREFIX}random":
        embed = discord.Embed(
            title="Random Number",
            description=f"Your random number is..... {round(random.random() * 1000)}",
        color=discord.Color(int("AF27E4", 16)),
    )
        embed.set_footer(text=footer),
        await message.channel.send(embed=embed)

    elif message.content == f"{PREFIX}ticket-add":
        author_name = message.author.name
        user_data = loadHasTicket()

        if user_data["users_with_tickets"].get(author_name):
            await message.channel.send("You already have a ticket.")
            await message.delete()
        else:
            user_data["users_with_tickets"][author_name] = True
            saveHasTicket(user_data)
            await message.channel.send("Ticket created.")
            guild = message.guild
            await guild.create_text_channel(f"ticket-{message.author.name}")
            await message.delete()
    elif message.content == f"{PREFIX}ticket-rm":
        author_name = message.author.name
        user_data = loadHasTicket()

        if user_data["users_with_tickets"].get(author_name):
            user_data["users_with_tickets"].pop(author_name)
            saveHasTicket(user_data)

            # Find the channel associated with the user's ticket
            for channel in message.guild.channels:
                if channel.name.startswith(f"ticket-{author_name}"):
                    await channel.delete()
                    await message.channel.send("Ticket removed.")
                    await message.delete()
                    return

            await message.channel.send("Ticket channel not found.")
        else:
            await message.channel.send("You don't have a ticket to remove.")
    elif message.content.startswith(f"{PREFIX}say "):
        sayMsg = message.content[len(f"{PREFIX}say "):]
        if sayMsg == blank:
            await message.channel.send(f"You did not add anything after {PREFIX}say")
            await message.delete()
        else:
            embed = discord.Embed(
                title=f"{message.author.name} said....",
                description=sayMsg,
            color=discord.Color(int("AF27E4", 16)),
            )
            embed.set_footer(text=footer),
            await message.channel.send(embed=embed)
            await message.delete()
    elif message.content.startswith(f"{PREFIX}sayOwner "):
        if message.author.name == f"{owner}":
            sayMsg = message.content[len(f"{PREFIX}sayOwner "):]
            await message.channel.send(sayMsg)
            await message.delete()
        else:
            return

# Run the bot with the provided token
client.run(TOKEN)
