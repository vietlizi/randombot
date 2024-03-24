import discord
from discord.ext import commands
TOKEN = 'your_token_here'
WELCOME_CHANNEL_NAME = 'new_member'

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_member_join(member):
    # Find the channel by name
    for channel in member.guild.channels:
        if channel.name == WELCOME_CHANNEL_NAME:
            # Replace 'anhemdoả' with your server's name or any text you want
            await channel.send(f'Welcome {member.mention}, to anhemdoả. We hope you have a great time here!')
            break

bot.run(TOKEN)
