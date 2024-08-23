import os, discord
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client(command_prefix='-', intents=intents)

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
        
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="Member")

    if role:
        await member.add_roles(role)
    else:
        pass

    print("User joined")

client.run(TOKEN)