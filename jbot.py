import os, discord
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True

load_dotenv()

BANNED_WORDS = [
    "nigger",
    "nigga",
    "retard",
    "bastard",
    "test"
]

PIRACY = [
    "sp",
    "simplaza",
    "rutracker",
    "suprbay",
    "pirates-forum"
]

TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client(command_prefix='-', intents=intents)

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    if message.author == client.user:
        return
    
    if channel == "chat":
        if user_message.lower() == "hello there":
            await message.channel.send("General Kenobi!")
            return
        
    if username != "kubab511":
        for word in BANNED_WORDS:
            if word in user_message.lower():
                try: 
                    await message.delete()
                    await message.channel.send(f"{username} watch your language!")
                    break
                except discord.errors.Forbidden:
                    print(f"Could not delete message from {username} due to lack of permissions")

        for word in PIRACY:
            if word in user_message.lower():
                try:
                    await message.delete()
                    await message.channel.send(f"{username} rule 7.")
                    break
                except discord.errors.Forbidden:
                    print(f"Could not delete message from {username} due to lack of permissions")

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="Member")

    if role:
        await member.add_roles(role)
        return
    
client.run(TOKEN)