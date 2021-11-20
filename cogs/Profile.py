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
    joined = target.joined_at.strftime("%a %b %B %Y")

    pfp = target.avatar_url_as(size=256)
    base = Image.open('./Assets/profileBase.png').convert("RGBA")
    data = BytesIO(await pfp.read())
    pfp = Image.open(data).convert("RGBA")
    name = f"{name[:16]}..." if len(name)>16 else name
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
  async def ship(self, ctx, *,  target : discord.Member=None):
      if not target:
        target = ctx.author
      authName = str(ctx.author.display_name)
      targName = str(target.display_name)
      amount = randrange(100)
      amount = f"{amount}%"

      authPfp = ctx.author.avatar_url_as(size=256)
      targPfp = target.avatar_url_as(size=256)
      base = Image.open('./Assets/loveBase.png').convert("RGBA")
      data = BytesIO(await authPfp.read())
      authPfp = Image.open(data).convert("RGBA")
      data = BytesIO(await targPfp.read())
      targPfp = Image.open(data).convert("RGBA")
      authName = f"{authName[:16]}..." if len(authName)>16 else authName
      targName = f"{targName[:16]}..." if len(targName)>16 else targName
      draw = ImageDraw.Draw(base)
      authPfp = circle(authPfp, size=(150,150))
      targPfp = circle(targPfp, size=(150,150))
      W = 375
      H = 550
      w, h = draw.textsize(authName)
      w2, h2 = draw.textsize(targName)
      w3, h3 = draw.textsize(amount)
      font = ImageFont.truetype("./Assets/openSans.ttf", 25)
      draw.text(((W-w)/2,(H-h)/2-75), authName, fill="black", font=font)
      draw.text(((W-w2)/2,(H-h2)/2+75), targName, fill="black", font=font)
      draw.text(((W-w3)/2,(H-h3)/2), amount, fill="black", font=font)
      base.paste(authPfp,(137,15),authPfp)
      base.paste(targPfp,(137,400),targPfp)

      with BytesIO() as a:
        base.save(a, "PNG")
        a.seek(0)
        await ctx.send(file=discord.File(a,"ship.png"))






def setup(client):
  client.add_cog(Profile(client))

    