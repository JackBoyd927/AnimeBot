import os
import random
import discord
from discord.ext import commands
from keep_alive import keep_alive

TOKEN = os.environ['TOKEN']

client = commands.Bot(command_prefix='%') 

@client.command()
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')
  client.load_extension(f'cogs.{extension}')


@client.event
async def on_ready():
  print(f'Bot is logged in as {client.user}')

@client.command()
async def hello(ctx):
  await ctx.channel.send(f"Hello! {ctx.author.mention}")

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')
keep_alive()
client.run(TOKEN)