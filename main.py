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
# Despite it's stupid name, this is the best bot you'll ever use. Moderation, Utilities.. We've got it all.
# Self-host your own at https://github.com/xNoerPlaysCodes/mbgtk-python
# main.py

# Importing Packages
import discord, sys, requests, random, os, json, asyncio, subprocess, datetime
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
#############
#uptime
start_time = datetime.datetime.now()
#############
##################### VARIABLES
version = "Release 1.0.1"

helpMenu = f"""
# ```Main```
`{PREFIX}ping` - Returns Client Latency.
`{PREFIX}help` - This!
`{PREFIX}random` <first num> <second num> - Returns a random number with two arguments that you gave.
# ```Giphy Integration```
`{PREFIX}meme` - Returns a gif from giphy (Is meme enabled -> {meme_enabled})
`{PREFIX}settag` <tag> - Sets tag to the message you put in <tag>
# ```Utility```
`{PREFIX}ticket-add` - Creates a ticket
`{PREFIX}ticket-rm` - Removes your ticket if you have one
`{PREFIX}userinfo @user` - Returns user information of user, no ping of user will return userinfo about message author.
`{PREFIX}serverinfo` - Returns guild information.
`{PREFIX}uptime` - Returns since when the bot is up.
# ```Fun```
`{PREFIX}say <msg>` - Says that message!
[ OWNER-ONLY COMMAND ]\* `{PREFIX}osay <msg>` Says that message without who said it.
[ OWNER-ONLY COMMAND]\* `{PREFIX}run <bash command>` - Runs bash command on the PC or hosting platform that is hosting it. Only works on Linux and less than macOS catalina.

# ```Moderation```
`{PREFIX}kick @user` - Kicks that user.
`{PREFIX}ban @user` - Bans that user.
`{PREFIX}slowmode <seconds>` or `{PREFIX}sm <seconds>` - Sets the slowmode for that current channel.
`{PREFIX}purge <number of messages to purge>` - Mass-deletes messages.
`{PREFIX}log_start <channel id>` - Starts the message logging in specified channel id.
`{PREFIX}log_stop` - Stops message logging if enabled.

\*Owner of this **BOT** is {owner}
            """
aboutCommandMenu = f"""
Hi, I'm MBGTK! I am an open-source discord bot that does what the most popular bots do but is designed to reduce the bots in your server while not having "Fun" commands that clog up your server.

[Github Page](https://github.com/xNoerPlaysCodes/mbgtk-python/)
[Official Website](https://xnoerplayscodes.github.io/index.html)
[Documentation](https://xnoerplayscodes.github.io/docs/docs.html)

Credits:
xNoerPlays (<@1044817642143371364>) - Developer
Techbox (<@906810276081442816>) - Ideas and the sole idea for this bot was his.
Xavier (<@1087527750539165747>) - Emotional Support XD / Tester of Bot
sam/sammy (<@1051430553469071380>) - Logo maker 😍😍😍😍😍😍😍

❤️❤️❤️❤️❤️❤️❤️ This took a long time, so consider DMing me (or any of the members above) to give them a happy thankyou <3

Other information:
Global Bot Prefix: `{PREFIX}`
Based on MBGTK.py version {version}
Hosting Python Version: ||{sys.version}||
"""
if meme_enabled == 'true':
    settings = f"""
Prefix - {PREFIX}
Intents used - discord.Intents.default()
Has intents.message_content? - True
Footer Text - {footer}
Owner - {owner}
Playing Game - {PlayingGame}

/\* Confidential information such as your discord bot token and your Giphy API key are not shown for security purposes.
    """
elif meme_enabled == 'false':
    settings = f"""
Prefix - {PREFIX}
Intents used - discord.Intents.default()
Footer Text - {footer}
Owner - {owner}
Playing Game - {PlayingGame}
Giphy API Key - API_KEY_NOT_GIVEN

/\* Confidential information such as your discord bot token are not shown for security purposes.
    """
##########################
# DEFINTIONS
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

def stopBot(exit_code):
    sys.exit(exit_code)

def isBot(user):
    return user.bot

def isStr(value):
    return isinstance(value, str)
#########################
tag = "random funny" # The tag gets reset to this value everytime bot is restarted

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
        print(f"🚀 Successful login as {client.user} with prefix {PREFIX} and no Giphy API KEY.")
    else:
        print(f"🚀 Successful login as {client.user} with prefix {PREFIX}\nand Giphy API KEY {api_key}")
    await client.change_presence(activity=discord.Game(name=PlayingGame))
############################################# LOGGING MESSAGES
@client.event
async def on_message_delete(message):
    # print("Message deleted")
    if message.author == client.user:
        return

    try:
        with open("log_channel.json", "r") as f:
            server_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        server_data = []

    server_id = str(message.guild.id)
    server_entry = next((data for data in server_data if data['server_id'] == server_id), None)

    if server_entry and server_entry["log_enabled"]:
        log_channel_id = server_entry.get("log_channel")
        if log_channel_id:
            log_channel = message.guild.get_channel(log_channel_id)
            if log_channel:
                time_now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
                embed = discord.Embed(
                    title=f"{message.author.name}'s message was deleted",
                    description=message.content,
                    color=discord.Color(int("FFFFFF", 16)),
                )
                embed.set_footer(text=f"Deleted at {time_now}")
                await log_channel.send(embed=embed)

### EDITED MSGS

@client.event
async def on_message_edit(before, after):
    # print("Message edited")
    if before.author == client.user:
        return
    if isBot(before.author):
        return

    try:
        with open("log_channel.json", "r") as f:
            server_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        server_data = []

    server_id = str(before.guild.id)
    server_entry = next((data for data in server_data if data['server_id'] == server_id), None)

    if server_entry and server_entry["log_enabled"]:
        log_channel_id = server_entry.get("log_channel")
        if log_channel_id:
            log_channel = before.guild.get_channel(log_channel_id)
            if log_channel:
                time_now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
                embed = discord.Embed(
                    title=f"{before.author.name} edited",
                    description=f"```Original Message:```\n{before.content}\n```New Message:```\n{after.content}",
                    color=discord.Color(int("FFFFFF", 16)),
                )
                embed.set_footer(text=f"Edited at {time_now}")
                await log_channel.send(embed=embed)
##############################################################
# Load the list of server data from log_channel.json if the file exists
try:
    with open("log_channel.json", "r") as f:
        server_data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    server_data = []
#########
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
        return
    else:
        if message.content == f"{PREFIX}halt":
            if message.author.name == owner:
                print(f"{message.author} has stopped the bot.")
                time.sleep(1)
                stopBot(0)
            else:
                print("A user tried to stop the bot while not being owner.")
                await message.channel.send(f"Sorry, you're not the owner of the bot, if you think this is a mistake edit the var.py file and replace the blank with username. You are {message.author} and from var.py is {owner}")
        global tag  # Declare the global tag variable to change it if needed

        if message.content.startswith(f"{PREFIX}settag"):
            if meme_enabled == "true":
                tag = message.content[len(f"{PREFIX}settag"):]
                await message.channel.send(f"Tag set to `{tag}`.")
            elif meme_enabled == "false":
                await message.channel.send("Meme functionality is disabled in var.py, please change that.")
        elif message.content == f"{PREFIX}meme":
            if meme_enabled == "true":
                gif_url = await fetch_gif_with_tag(tag)
                if gif_url:
                    embed = discord.Embed(
                        title=f"Tag is `{tag}`",
                    color=discord.Color(int("AF27E4", 16))
                    )
                    embed.set_footer(text=f"Powered by GIPHY®")
                    embed.set_image(url=gif_url)
                    await message.channel.send(embed=embed)
                else:
                    await message.channel.send("Oops, something went wrong while fetching the GIF.", delete_after=5)
            elif meme_enabled == "false":
                await message.channel.send("Meme functionality is disabled in var.py, please change that.")
        elif message.content == f"{PREFIX}help":
            embed = discord.Embed(
                title="Help Menu",
                description=helpMenu,
                color=discord.Color(int("AF27E4", 16)),
            )
            embed.set_footer(text=footer),
            try:
                await message.author.send(embed=embed)
                await message.channel.send("Check your DMs!")
            except discord.errors.Forbidden:
                await message.channel.send(embed=embed)

        elif message.content == f"{PREFIX}ping":
            og_msg = await message.channel.send(f"Calculating....")
            await asyncio.sleep(1)
            await og_msg.edit(content=f"Pong! {round(client.latency * 1000)}ms")
        elif message.content.startswith(f"{PREFIX}random"):
            args = message.content.split()
            if len(args) == 3:
                if args[1].isdigit() and args[2].isdigit():
                    first = int(args[1])
                    second = int(args[2])
    #
                    embed = discord.Embed(
                        title="Random Number",
                        description=f"Your random number is..... {random.randint(first, second)}",
                    color=discord.Color(int("AF27E4", 16)),
                )
                    embed.set_footer(text=footer),
                    await message.channel.send(embed=embed)
                else:
                    first = str(args[1])
                    second = str(args[2])
                    await message.channel.send(f"{first} or {second} was not an integer")
            else:
                await message.channel.send(f"Usage: {PREFIX}random <first num> <second num>")
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
        elif message.content.startswith(f"{PREFIX}say"):
            sayMsg = message.content[len(f"{PREFIX}say"):]
            if sayMsg == blank:
                await message.channel.send(f"You did not add anything after {PREFIX}say")
                await message.delete()
            else:
                embed = discord.Embed(
                    title=f"{message.author.name} said...",
                    description=sayMsg,
                color=discord.Color(int("AF27E4", 16)),
                )
                async with message.channel.typing():
                    await asyncio.sleep(0.5)  # Simulate typing for 2 seconds
                    await message.channel.send(embed=embed)
                await message.delete()
        elif message.content.startswith(f"{PREFIX}osay"):
            if message.author.name == f"{owner}":
                sayMsg = message.content[len(f"{PREFIX}osay"):]
                async with message.channel.typing():
                    await asyncio.sleep(0.5)  # Simulate typing for 2 seconds
                    await message.channel.send(sayMsg)
                await message.delete()
            else:
                return
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
Server Roles - {roles}\n(No you did not just ping everyone.)
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

        elif message.content.startswith(f"{PREFIX}run"):
            if message.author.name == owner:
                bash_command = message.content[len(f"{PREFIX}run"):]
                if bash_command != "":
                    try:
                        command_output = subprocess.check_output(bash_command, shell=True, text=True)
                        # For Python 3.5 and earlier, use: command_output = subprocess.check_output(bash_command, shell=True)
                    except subprocess.CalledProcessError as e:
                        await message.channel.send(f"`{bash_command}` is not a valid bash command!")
                        await message.delete()
                        command_output = None

                    if command_output is not None:
                        embed = discord.Embed(
                            title=f"Command was `{bash_command}`",
                            description=f"```\n{command_output}\n```",
                        color=discord.Color(int("AF27E4", 16))
                        )
                        embed.set_footer(text=f"User was {message.author.name} | {footer}")
                        await message.channel.send(embed=embed)
                        await message.delete()
                    else:
                        return
                elif bash_command == "":
                    await message.channel.send("Provide a valid bash command to run!")
                    await message.delete()

        elif message.content.startswith(f"{PREFIX}purge"):
            amount = message.content[len(f"{PREFIX}purge"):]
            if amount != "":
                if int(amount) < int(-1):
                    await message.channel.send("Provide a valid number of messages to delete")
                    return
                elif int(amount) > 500:
                    await message.channel.send(f"{amount} is greater than the limit of 500!")
                else:
                    if message.author.guild_permissions.manage_messages:
                        try:
                            amount = int(amount)
                            await message.channel.purge(limit=amount + 1)
                            await message.channel.send(f"Purged {amount} messages", delete_after=2)
                        except discord.errors.Forbidden as e:
                            await message.channel.send(f"Error has occurred and the command could not be executed.\n```\n{e}\n```")
                    else:
                        await message.channel.send("You do not have enough permissions!")
                        return
            else:
                await message.channel.send("Please give how many messages to purge!")

        elif message.content.startswith(f"{PREFIX}kick"):
            if message.author.guild_permissions.manage_messages:
                command_parts = message.content.split()
                if len(command_parts) < 2:
                    await message.channel.send(f"Usage: {PREFIX}kick <user_mention>")
                    return

                user_id = command_parts[1].strip('<@!>')
                try:
                    member = await message.guild.fetch_member(int(user_id))
                    if member:
                        try:
                            await member.kick()
                            await message.channel.send(f"<@{user_id}> ({member.display_name}) has been kicked from the server.")
                        except discord.Forbidden:
                            await message.channel.send("I don't have permission to kick members.")
                    else:
                        await message.channel.send("User not found.")
                except discord.NotFound:
                    await message.channel.send("User not found.")
            else:
                await message.channel.send("You don't have permission to kick members as you need **manage messages.**")

        elif message.content == f"{PREFIX}uptime":
            current_time = datetime.datetime.now()
            uptime = current_time - start_time

            days, seconds = uptime.days, uptime.seconds
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            seconds = seconds % 60

            uptime_str = f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

            await message.channel.send(f"Uptime: {uptime_str}")

        if message.content == f"{PREFIX}log_start":
            if message.author.guild_permissions.manage_messages:
                try:
                    with open("log_channel.json", "r") as f:
                        server_data = json.load(f)
                except (FileNotFoundError, json.JSONDecodeError):
                    server_data = []

                server_id = str(message.guild.id)
                server_entry = next((data for data in server_data if data['server_id'] == server_id), None)

                if not server_entry:
                    server_data.append({"server_id": server_id, "log_enabled": True, "log_channel": int(message.channel.id)})

                    with open("log_channel.json", "w") as f:
                        json.dump(server_data, f, indent=4)

                    await message.channel.send("Logging enabled for this server and channel.")
                else:
                    await message.channel.send("Logging is already enabled for this server and channel.")

        elif message.content == f"{PREFIX}log_stop":
            if message.author.guild_permissions.manage_messages:
                try:
                    with open("log_channel.json", "r") as f:
                        server_data = json.load(f)
                except (FileNotFoundError, json.JSONDecodeError):
                    server_data = []

                server_id = str(message.guild.id)
                server_entry = next((data for data in server_data if data['server_id'] == server_id), None)

                if server_entry:
                    server_entry["log_enabled"] = False

                    with open("log_channel.json", "w") as f:
                        json.dump(server_data, f, indent=4)

                    await message.channel.send("Logging disabled for this server.")
                else:
                    await message.channel.send(f"Server logging was not enabled using {PREFIX}log_start.")
            # Load the list of server data from log_channel.json if the file exists
            try:
                with open("log_channel.json", "r") as f:
                    server_data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                server_data = []
        elif message.content == f'{PREFIX}settings':
            if message.author.name == owner:
                embed = discord.Embed(
                    title=f"Read-only settings for {client.user}",
                    description=settings,
                color=discord.Color(int('AF27E4', 16))
                )
                embed.set_footer(text=footer)
                embed.set_thumbnail(url='https://i.imgur.com/7ggtoIk.png')
                await message.channel.send(embed=embed)
            else:
                await message.channel.send(f'Only the owner ({owner}) can use this command.')

        elif message.content.startswith(f'{PREFIX}slowmode'):
            args = message.content.split()
            if len(args) != 2:
                await message.channel.send(f"Usage: {PREFIX}slowmode <duration>")
                return
            if message.author.guild_permissions.manage_messages:
                try:
                    duration = int(args[1])
                    if duration < 0 or duration > 21600:  # Set reasonable limits for slow mode (0 to 6 hours)
                        await message.channel.send("Please provide a valid duration between 0 and 21600 seconds.")
                        return

                    await message.channel.edit(slowmode_delay=duration)
                    await message.channel.send(f"Slow mode set to {duration} seconds in this channel.")
                except ValueError:
                    await message.channel.send("Please provide a valid duration, no need to put `s`, just the number is fine.")
            else:
                await message.channel.send("You do not have enough permissions!")
                return

        elif message.content.startswith(f'{PREFIX}sm'):
            args = message.content.split()
            if len(args) != 2:
                await message.channel.send(f"Usage: {PREFIX}sm <duration>")
                return
            if message.author.guild_permissions.manage_messages:
                try:
                    duration = int(args[1])
                    if duration < 0 or duration > 21600:  # Set reasonable limits for slow mode (0 to 6 hours)
                        await message.channel.send("Please provide a valid duration between 0 and 21600 seconds.")
                        return

                    await message.channel.edit(slowmode_delay=duration)
                    await message.channel.send(f"Slowmode set to {duration} seconds in this channel.")
                except ValueError:
                    await message.channel.send("Please provide a valid duration, no need to put `s`, just the number is fine.")
            else:
                await message.channel.send("You do not have enough permissions!")
                return

        elif message.content.startswith(f"{PREFIX}ban"):
            if message.author.guild_permissions.ban_members:
                command_parts = message.content.split()
                if len(command_parts) < 2:
                    await message.channel.send(f"Usage: {PREFIX}ban <user_mention>")
                    return

                user_id = command_parts[1].strip('<@!>')
                try:
                    member = await message.guild.fetch_member(int(user_id))
                    if member:
                        try:
                            await member.ban()
                            await message.channel.send(f"<@{user_id}> ({member.display_name}) has been banned from the server.")
                        except discord.Forbidden:
                            await message.channel.send("I don't have permission to ban members.")
                    else:
                        await message.channel.send("User not found.")
                except discord.NotFound:
                    await message.channel.send("User not found.")
            else:
                await message.channel.send("You don't have permission to ban members as you need **ban members** permission.")

        elif message.content.startswith(f"{PREFIX}eval"):
            evalCMD = message.content[len(f"{PREFIX}eval"):]
            if evalCMD == '':
                await message.channel.send("Input must not be **None**")
                return
            else:
                if message.author.name == owner:
                    try:
                        result = eval(evalCMD)
                        embed = discord.Embed(
                            title=f"Code output:",
                            description=f"```\n{result}\n```",
                        color=discord.Color(int("AF27E4", 16))
                        )
                        embed.set_footer(text=footer)
                        await message.channel.send(embed=embed)
                    except SyntaxError as e:
                        await message.channel.send(f"Fatal error.\n```\nTYPE=SyntaxError\n{e}\n```")
                        return
                    except ValueError as ve:
                        await message.channel.send(f"Fatal error.\n```\nTYPE=ValueError\n{ve}\n```")
                        return
                    except Exception as x:
                        await message.channel.send(f"Fatal error.\n```\nTYPE=Exception\n{x}\n```")
                        return
                elif message.author.name != owner:
                    return

# Run the bot with the provided token
client.run(TOKEN)
