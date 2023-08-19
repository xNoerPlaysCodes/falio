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
# Despite it's stupid name, this bot is the best bot you have ever seen. Moderation, Fun, Utilities... We've got it all
# Invite me today at https://bit.ly/mbgtk (OR PUT GITHUB PAGE)
# main.py

# Importing Packages
import discord, sys, requests, random, os, json, asyncio
# Importing variables from var.py
from var import tokenBot as TOKEN
from var import footer_text as footer
from var import PREFIX, owner, api_key, PlayingGame
## banned users importing
from banned_users import users_banned
################# CHECKS
if api_key == "API_KEY_HERE":
    meme_enabled = "false"
else:
    meme_enabled = "true"
########################
##################### VARIABLES
version = "PR-4"
blank = ""

helpMenu = f"""
```Main```
`{PREFIX}ping` - Returns Client Latency.
`{PREFIX}help` - This!
`{PREFIX}random` - Returns a random number 100-1000
```Giphy Integration```
`{PREFIX}meme` - Returns a gif from giphy (Is meme enabled -> {meme_enabled})
`{PREFIX}settag` <tag> - Sets tag to the message you put in <tag>
```Utility```
`{PREFIX}ticket-add` - Creates a ticket
`{PREFIX}ticket-rm` - Removes your ticket if you have one
`{PREFIX}userinfo @user` - Returns user information of user, no ping of user will return userinfo about message author.
`{PREFIX}serverinfo` - Returns guild information.
```Fun```
`{PREFIX}say <msg>` - Says that message!
[ OWNER-ONLY COMMAND ]\* `{PREFIX}osay <msg>` Says that message without who said it.

\*Owner of this bot is {owner}
            """
aboutCommandMenu = f"""
Hi, I'm MBGTK! I am an open-source discord bot designed to help you reduce the bots in your server.

[Github Page](https://github.com/xNoerPlaysCodes/mbgtk-python/)
[Official Website](https://xnoerplayscodes.github.io/index.html)

Credits:
xNoerPlays (noerlol#0) - Lead Developer
Techbox (teckbox#0) - Ideas and the sole idea for this bot was his.
Xavier (frlnamra#0) - Emotional Support XD / Tester of Bot
sam/sammy (@.zqkarl#0) - Logo maker 😍😍😍😍😍😍😍

❤️❤️❤️❤️❤️❤️❤️ This took a long time, so consider DMing me (or any of the members above) to give them a happy thankyou <3

Other information:
Global Bot Prefix: `{PREFIX}`
Based on MBGTK.py version {version}
Hosting Python Version: ||{sys.version}||
"""
##########################
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
    if message.author.name in users_banned:
        await message.channel.send("You are banned from using this bot.")
    else:
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
                await message.channel.send(embed=embed)
                await message.delete()
        elif message.content.startswith(f"{PREFIX}osay "):
            if message.author.name == f"{owner}":
                sayMsg = message.content[len(f"{PREFIX}osay "):]
                await message.channel.send(sayMsg)
                await message.delete()
            else:
                return
        elif message.content.lower().startswith("mbgtk su"):
            await message.channel.send("Nope.")
        elif message.content == f"{PREFIX}about":
            embed = discord.Embed(
                description=aboutCommandMenu,
            color=discord.Color(int("AF27E4", 16)),
            )
            embed.set_footer(text=f"Made with love in discord.py | {footer}"),
            await message.channel.send(embed=embed)
        elif message.content == f"{PREFIX}serverinfo":
            guild = message.guild
            # Gets emojis as formatted
            emojis = ", ".join([str(emoji) for emoji in guild.emojis])

            # Gets roles as formatted
            roles = ", ".join([role.mention for role in guild.roles])
            embed = discord.Embed(
                title="Server Information",
                description=f"""
```Main Info```
Guild is {guild}
Server ID - {guild.id}
Server Name - {guild.name}
Server Description - {guild.description}
```Other```
Server Member Count - {str(guild.member_count)}
Server Boost Count - {int(guild.premium_subscription_count)}
Server Boost Level - {guild.premium_tier}
Server Emojis - (Click to expose spoiler) ||{emojis}||
Server Roles - {roles}
    """,
    color=discord.Color(int("AF27E4", 16)),
        )
            embed.set_thumbnail(url=f"{guild.icon}")
            embed.set_footer(text=footer)
            await message.channel.send(embed=embed)

        elif message.content.startswith(f"{PREFIX}userinfo"):
            user_mentions = message.mentions  # Get mentioned users

            if len(user_mentions) == 0:
                user = message.author
            else:
                user = user_mentions[0]  # Consider only the first mentioned user
            is_bot = "Yes" if user.bot else "No"
            # !!!! DOSENT WORK !!!!
            # nitro_subscription_type = "Nitro Basic" if user.premium_type == discord.PremiumType.nitro_basic else ("Nitro" if user.premium_type == discord.PremiumType.nitro else "None")
            # has_2fa = "Yes" if user.mfa_enabled else "No"

            embed = discord.Embed(
                title="User Information",
                description=f"""
Is Bot?: {is_bot}
User Mention: <@{user.id}>
User Name: {user.name}#{user.discriminator}
User ID: {user.id}
Display Name: {user.display_name}
        """,
                color=discord.Color(int("AF27E4", 16)),
            )
            embed.set_footer(text=footer)
            embed.set_thumbnail(url=user.avatar)

            await message.channel.send(embed=embed)
# Run the bot with the provided token
client.run(TOKEN)
