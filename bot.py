import discord
from discord.ext import commands

TOKEN = 'MTQ0MjIwNjIzOTI2MTIwMDU2NQ.Gy-XN-.8_ATuBSlQbmJ9P-h9z4T5PixEf7WmAhnWHHCro'  # replace with your bot token

intents = discord.Intents.default()
intents.message_content = True  # needed to read messages

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

bot.run(TOKEN)
