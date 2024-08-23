import os, discord
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    client.run(TOKEN)

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f"Message {user_message} by {username} in {channel}")

    if message.author == client.user:
        return
    
    if channel == "chat":
        if user_message.lower() == "hello there":
            await message.channel.send("General Kenobi!")
            return

client.run(TOKEN)