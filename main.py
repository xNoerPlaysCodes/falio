import discord
from var import tokenBot as token

print("Logging in....")

intents = discord.Intents.default()
intents.typing = True
intents.presences = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    print(f'Message received: {message.content}')  # Add this line to check the message content

    if message.content.startswith(';test'):
        await message.channel.send(f'Hello, {message.author.name}.')

    if message.content.startswith(';ping'):
        # Calculate the bot's ping in milliseconds.
        ping_ms = round(client.latency * 1000)
        await message.channel.send(f'Ping is {ping_ms}ms')

    if message.content.startswith('mbgtk suc'):
        await message.channel.send(f'I will send you to Jesus.')

client.run(token)
