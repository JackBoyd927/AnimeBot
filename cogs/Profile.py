import discord
from io import BytesIO
from discord.ext import commands
from PIL import Image, ImageChops, ImageDraw, ImageFont

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
    base = Image.open('./Assets/main.png').convert("RGBA")
    data = BytesIO(await pfp.read())
    pfp = Image.open(data).convert("RGBA")
    name = f"{name[:16]}..." if len(name)>16 else name
    draw = ImageDraw.Draw(base)
    pfp = circle(pfp, size=(500,500))
    font = ImageFont.truetype("./Assets/OpenSans.ttf", 75)
    subFont = ImageFont.truetype("./Assets/OpenSans.ttf", 45)
    draw.text((288,540), name, fill = "black", font= font)

    draw.text((288,740), userId, fill = "black", font= subFont)
    draw.text((288,840), status, fill = "black", font= subFont)
    draw.text((288,940), joined, fill = "black", font= subFont)
    base.paste(pfp,(0,0),pfp)

    with BytesIO() as a:
      base.save(a, "PNG")
      a.seek(0)
      await ctx.send(file=discord.File(a,"profile.png"))








def setup(client):
  client.add_cog(Profile(client))

    