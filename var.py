import discord
# enter bot token here:
tokenBot = "bot token here"
intents = discord.Intents.default()
intents.message_content = True  # Allows the bot to receive message (Message updates, message send, delete etc (required to function))
PREFIX = ";" # The bot will respond to for example if you have prefix ; then it will respond to ;embedlol or ;help etc
