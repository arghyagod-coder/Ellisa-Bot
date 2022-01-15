import discord
from discord.ext import commands
import random, requests

class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.command()
    async def wallpaper(self,ctx,res="1920x1080",*,search="nature"):
        query = search.replace(" ", "+")
        resp = requests.get(f"https://source.unsplash.com/{res}?{query}")
        file = open("wallpaper.png", "wb")
        file.write(resp.content)
        file.close()
        with open("wallpaper.png","rb") as f:
            file = discord.File(f)
            em = discord.Embed(title="Ah! Beauty")
            em.set_image(url="attachment://wallpaper.png")
            em.set_footer(text="Good Choice ngl")
            await ctx.send(file=file, embed=em)
    
    @commands.command(aliases=["phonebg"])
    async def mobilebg(self,ctx,*,search="nature"):
        query = search.replace(" ", "+")
        resp = requests.get(f"https://source.unsplash.com/720x1280?{query}")
        file = open("wallpaper.png", "wb")
        file.write(resp.content)
        file.close()
        with open("wallpaper.png","rb") as f:
            file = discord.File(f)
            em = discord.Embed(title="Ah! Beauty")
            em.set_image(url="attachment://wallpaper.png")
            em.set_footer(text="Good Choice ngl")
            await ctx.send(file=file, embed=em)
    
    @commands.command()
    async def dualbg(self,ctx,*,search="nature"):
        query = search.replace(" ", "+")
        resp = requests.get(f"https://source.unsplash.com/3840x1080?{query}")
        file = open("wallpaper.png", "wb")
        file.write(resp.content)
        file.close()
        with open("wallpaper.png","rb") as f:
            file = discord.File(f)
            em = discord.Embed(title="Ah! Beauty")
            em.set_image(url="attachment://wallpaper.png")
            em.set_footer(text="Good Choice ngl")
            await ctx.send(file=file, embed=em)
