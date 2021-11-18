import discord
import requests
import anime_images_api
from anime_images_api import Anime_Images
from discord.ext import commands
class AnimeGif(commands.Cog):

  def __init__(self, client):
    self.client = client
  #commands  
  @commands.command()
  async def hug(self, ctx):
    anime = Anime_Images()
    rst = anime.get_sfw('hug')
    emb = discord.Embed(title='hug')
    emb.set_image(url = rst)

    await ctx.channel.send(embed=emb)
  @commands.command()
  async def kiss(self, ctx, target):
    anime = Anime_Images()
    dsc = f'{ctx.author.mention} kisses {target}'
    rst = anime.get_sfw('kiss')
    emb = discord.Embed(description=dsc)
    emb.set_image(url = rst)

    await ctx.channel.send(embed=emb)

  @commands.command()
  async def slap(self, ctx):
    anime = Anime_Images()
    rst = anime.get_sfw('slap')
    emb = discord.Embed(title='slap')
    emb.set_image(url = rst)

    await ctx.channel.send(embed=emb)

  @commands.command()
  async def wink(self, ctx):
    anime = Anime_Images()
    rst = anime.get_sfw('wink')
    emb = discord.Embed(title='wink')
    emb.set_image(url = rst)

    await ctx.channel.send(embed=emb)

  @commands.command()
  async def pat(self, ctx):
    anime = Anime_Images()
    rst = anime.get_sfw('pat')
    emb = discord.Embed(title='pat')
    emb.set_image(url = rst)

    await ctx.channel.send(embed=emb)

  @commands.command()
  async def kill(self, ctx):
    anime = Anime_Images()
    rst = anime.get_sfw('kill')
    emb = discord.Embed(title='kill')
    emb.set_image(url = rst)

    await ctx.channel.send(embed=emb)

  @commands.command()
  async def cuddle(self, ctx):
    anime = Anime_Images()
    rst = anime.get_sfw('cuddle')
    emb = discord.Embed(title='cuddle')
    emb.set_image(url = rst)

    await ctx.channel.send(embed=emb)

  

def setup(client):
  client.add_cog(AnimeGif(client))