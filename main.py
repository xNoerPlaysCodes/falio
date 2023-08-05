import discord
from var import tokenBot as TOKEN
from var import PREFIX
from commands import get_commands

# Create a Discord client (bot)
intents = discord.Intents.default()
intents.message_content = True  # Allows the bot to receive message events
client = discord.Client(intents=intents)

# Event: When the bot is ready and connected to Discord
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

# Event: When a message is received in a server the bot is a part of
@client.event
async def on_message(message):
    # Ignore messages from the bot itself to avoid an infinite loop
    if message.author == client.user:
        return

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
