import os
import discord
from discord.ext import commands
import TenGiphPy

tokens = {
          'tenor': os.environ['TENOR']
          }
t = TenGiphPy.Tenor(token=tokens['tenor'])

class RolePlay(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  async def createReaction(self, ctx, target, alt=None):
    getgifurl = await t.arandom('anime '+ctx.invoked_with)
    emb = discord.Embed(description = f'{ctx.author.mention} {alt or ctx.invoked_with + "s" } {target or ""}')
    emb.set_image(url = getgifurl)
    await ctx.channel.send(embed=emb)
  #commands  
  

  @commands.command()
  async def bite(self, ctx, *, target=None):
    await self.createReaction(ctx, target)

  @commands.command()
  async def blast(self, ctx, *,target=None):
      await self.createReaction(ctx, target)
      
  @commands.command()
  async def clap(self, ctx, *,target=None):
      await self.createReaction(ctx, target)

  @commands.command()
  async def cry(self, ctx, *,target=None):
      await self.createReaction(ctx, target, 'cries')

  @commands.command()
  async def cuddle(self, ctx, *,target=None):
      await self.createReaction(ctx, target)
  @commands.command()
  async def dance(self, ctx, *,target=None):
      await self.createReaction(ctx, target)

  @commands.command()
  async def facepalm(self, ctx, *,target=None):
      await self.createReaction(ctx, target)
  
  @commands.command()
  async def glare(self, ctx, *,target=None):
      await self.createReaction(ctx, target)

  @commands.command()
  async def greet(self, ctx, *,target=None):
      await self.createReaction(ctx, target)
  
  @commands.command()
  async def highfive(self, ctx, *,target=None):
      await self.createReaction(ctx, target)

  @commands.command()
  async def hug(self, ctx, *,target=None):
      await self.createReaction(ctx, target)

  @commands.command()
  async def kiss(self, ctx, *,target=None):
      await self.createReaction(ctx, target, 'kisses')

  @commands.command()
  async def laugh(self, ctx, *,target=None):
      await self.createReaction(ctx, target)
  
  @commands.command()
  async def lick(self, ctx, *,target=None):
      await self.createReaction(ctx, target)
  
  @commands.command(aliases = ['headpat'])
  async def pat(self, ctx, *,target=None):
      await self.createReaction(ctx, target)
  
  @commands.command()
  async def poke(self, ctx, *,target=None):
      await self.createReaction(ctx, target)

  @commands.command(aliases = ['sprint'])
  async def run(self, ctx, *,target=None):
      await self.createReaction(ctx, target)

  @commands.command()
  async def sad(self, ctx, *,target=None):
      await self.createReaction(ctx, target)

  @commands.command()
  async def shoot(self, ctx, *,target=None):
      await self.createReaction(ctx, target)

  @commands.command()
  async def shrug(self, ctx, *,target=None):
      await self.createReaction(ctx, target)

  @commands.command()
  async def shy(self, ctx, *,target=None):
      await self.createReaction(ctx, target, 'is shy')

  @commands.command()
  async def slap(self, ctx, *,target=None):
      await self.createReaction(ctx, target)

  @commands.command()
  async def smile(self, ctx, *,target=None):
      await self.createReaction(ctx, target)

  @commands.command()
  async def stare(self, ctx, *,target=None):
      await self.createReaction(ctx, target)

  @commands.command()
  async def stomp(self, ctx, *,target=None):
      await self.createReaction(ctx, target)

  @commands.command()
  async def die(self, ctx, *,target=None):
      await self.createReaction(ctx, target)

  @commands.command()
  async def wiggle(self, ctx, *,target=None):
      await self.createReaction(ctx, target)

  @commands.command()
  async def wag(self, ctx, *,target=None):
      await self.createReaction(ctx, target)

def setup(client):
  client.add_cog(RolePlay(client))
