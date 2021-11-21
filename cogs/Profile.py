import discord
from io import BytesIO
from discord.ext import commands
from PIL import Image, ImageChops, ImageDraw, ImageFont
from random import randrange


def circle(pfp,size = (500,500)):
    
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp
  
class Profile(commands.Cog):
  
  def __init__(self, client):
    self.client = client

  

  @commands.command()
  async def profile(self, ctx, *,  target : discord.Member=None):
    if not target:
      target = ctx.author
    name = str(target.display_name)
    userId = str(target.id)
    status = str(target.status)
    joined = target.joined_at.strftime("%A, %B %d %Y\n@ %H:%M:%S %p")

    pfp = target.avatar_url_as(size=256)
    base = Image.open('./Assets/profileBase.png').convert("RGBA")
    data = BytesIO(await pfp.read())
    pfp = Image.open(data).convert("RGBA")
    name = f"{name[:12]}..." if len(name)>12 else name
    draw = ImageDraw.Draw(base)
    pfp = circle(pfp, size=(500,500))
    font = ImageFont.truetype("./Assets/openSans.ttf", 75)
    subFont = ImageFont.truetype("./Assets/openSans.ttf", 45)
    draw.text((288,540), name, fill = "black", font= font)

    draw.text((288,740), userId, fill = "black", font= subFont)
    draw.text((288,840), status, fill = "black", font= subFont)
    draw.text((288,940), joined, fill = "black", font= subFont)
    base.paste(pfp,(0,0),pfp)

    with BytesIO() as a:
      base.save(a, "PNG")
      a.seek(0)
      await ctx.send(file=discord.File(a,"profile.png"))
  @commands.command()
  async def ship(self, ctx,  target1 : discord.Member, target2 : discord.Member=None):
      if not target2:
        target2 = ctx.author
      targ2Name = str(target2.display_name)
      targ1Name = str(target1.display_name)
      amount = randrange(100)
      amount = f"{amount}%"

      targ2Pfp = target2.avatar_url_as(size=256)
      targ1Pfp = target1.avatar_url_as(size=256)
      base = Image.open('./Assets/loveBase.png').convert("RGBA")
      data = BytesIO(await targ2Pfp.read())
      targ2Pfp = Image.open(data).convert("RGBA")
      data = BytesIO(await targ1Pfp.read())
      targ1Pfp = Image.open(data).convert("RGBA")
      targ2Name = f"{targ2Name[:10]}..." if len(targ2Name)>10 else targ2Name
      targ1Name = f"{targ1Name[:10]}..." if len(targ1Name)>10 else targ1Name
      draw = ImageDraw.Draw(base)
      targ2Pfp = circle(targ2Pfp, size=(200,200))
      targ1Pfp = circle(targ1Pfp, size=(200,200))
      W = 500
      font = ImageFont.truetype("./Assets/openSans.ttf", 25)
      w,h = draw.textsize(targ2Name, font=font)
      draw.text(((W-w)/2-150,268), targ2Name, fill="black", font=font)
      w,h = draw.textsize(targ1Name, font=font)
      draw.text(((W-w)/2+150,268), targ1Name, fill="black", font=font)
      w,h = draw.textsize(amount, font=font)
      draw.text(((W-w)/2,268), amount, fill="black", font=font)
      base.paste(targ2Pfp,(150,24),targ2Pfp)
      base.paste(targ1Pfp,(150,352),targ1Pfp)

      with BytesIO() as a:
        base.save(a, "PNG")
        a.seek(0)
        await ctx.send(file=discord.File(a,"ship.png"))






def setup(client):
  client.add_cog(Profile(client))

    