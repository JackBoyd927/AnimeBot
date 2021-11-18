import os
import random
import requests
import discord
from discord.ext import commands
import anime_images_api
from anime_images_api import Anime_Images
import giphy_client
from giphy_client.rest import ApiException


TOKEN = os.environ['TOKEN']

client = commands.Bot(command_prefix='^')



@client.event
async def on_ready():
  print('Bot is logged in as {0.user}'
  .format(client))

@client.command()
async def hello(ctx):
  await ctx.channel.send(f"Hello! {ctx.author.mention}")

@client.command()
async def hug(ctx):
  anime = Anime_Images()
  rst = anime.get_sfw('hug')
  emb = discord.Embed(title=hug)
  emb.set_image(url = rst)

  await ctx.channel.send(embed=emb)

@client.command()
async def kiss(ctx):
  anime = Anime_Images()
  rst = anime.get_sfw('kiss')
  emb = discord.Embed(title=kiss)
  emb.set_image(url = rst)

  await ctx.channel.send(embed=emb)

@client.command()
async def slap(ctx):
  anime = Anime_Images()
  rst = anime.get_sfw('slap')
  emb = discord.Embed(title=slap)
  emb.set_image(url = rst)

  await ctx.channel.send(embed=emb)

@client.command()
async def wink(ctx):
  anime = Anime_Images()
  rst = anime.get_sfw('wink')
  emb = discord.Embed(title=wink)
  emb.set_image(url = rst)

  await ctx.channel.send(embed=emb)

@client.command()
async def pat(ctx):
  anime = Anime_Images()
  rst = anime.get_sfw('pat')
  emb = discord.Embed(title=pat)
  emb.set_image(url = rst)

  await ctx.channel.send(embed=emb)

@client.command()
async def kill(ctx):
  anime = Anime_Images()
  rst = anime.get_sfw('kill')
  emb = discord.Embed(title=kill)
  emb.set_image(url = rst)

  await ctx.channel.send(embed=emb)

@client.command()
async def cuddle(ctx):
  anime = Anime_Images()
  rst = anime.get_sfw('cuddle')
  emb = discord.Embed(title=cuddle)
  emb.set_image(url = rst)

  await ctx.channel.send(embed=emb)








client.run(TOKEN)