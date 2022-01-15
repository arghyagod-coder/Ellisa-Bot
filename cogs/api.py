import discord
from discord.ext import commands
import random
import dog
import requests
from urllib import *
from datetime import date
import os
import json
from dotenv import load_dotenv
import pyqrcode
import png
from pyqrcode import QRCode
import re

load_dotenv()
class API(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.command(aliases=["gen","g"])
    async def generate(self,ctx,*,text):
        r = requests.post(
            "https://api.deepai.org/api/text-generator",
            data={
                'text': text,
            },
            headers={'api-key': os.getenv("DEEPAI_KEY")}
        )
        generated = r.json()['output']
        em = discord.Embed(title="Generated Text", description=generated, footer="Ain't I smart?", author=True, thumbnail=ctx.author.avatar_url)
        await ctx.send(embed=em)

    @commands.command(aliases=["yt"])
    async def youtube(self, ctx, *, search):
        query_string = parse.urlencode({'search_query': search})
        html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
        search_content= html_content.read().decode()
        search_results = re.findall(r'\/watch\?v=\w+', search_content)
        #print(search_results)
        await ctx.send('https://www.youtube.com' + search_results[0])
    
    @commands.command()
    async def age(self,ctx,*args):
        res = requests.get("https://api.agify.io/?name="+args[0])
        age= res.json()["age"]
        await ctx.reply(f"Your name says you are {age}")
    
    @commands.command()
    async def covid(self,ctx,*,country):
        if country.lower()=="global":
            res = requests.get('https://api.covid19api.com/summary')
            data = res.json()
            gd = data["Global"]
            info={
                "country":"Global",
                "totalconfirmed":gd["TotalConfirmed"],
                "newcases":gd["NewConfirmed"],
                "newdeaths":gd["NewDeaths"],
                "totaldeaths":gd["TotalDeaths"]
            }
            em = discord.Embed(title=f"Covid 19 Global Statistics", color=discord.Color.red())
            em.add_field(name="New Confirmed Cases", value=gd["NewConfirmed"])
            em.add_field(name="Total Confirmed Cases", value=gd["TotalConfirmed"])
            em.add_field(name="New Deaths", value=gd["NewDeaths"])
            em.add_field(name="Total Deaths", value=gd["TotalDeaths"])
            em.set_thumbnail(url="https://mlo1gfdw4hud.i.optimole.com/7AeXmgQ-r-JaQYaO/w:auto/h:auto/q:79/https://dndi.org/wp-content/uploads/2020/03/COVID19_icon.svg")

        else:
            country = country.lower()
            country = country.replace(" ", "-")
            res = requests.get('https://api.covid19api.com/country/'+country)
            data = res.json()
            today_data = data[-1]
            em = discord.Embed(title=f"Covid 19 Statistics in {country}", color=discord.Color.red())
            em.add_field(name="Date", value=date.today())
            em.add_field(name="Confirmed Cases", value=today_data["Confirmed"])
            em.add_field(name="Deaths", value=today_data["Deaths"])
            em.add_field(name="Active Cases", value=today_data["Active"])
            em.set_thumbnail(url="https://mlo1gfdw4hud.i.optimole.com/7AeXmgQ-r-JaQYaO/w:auto/h:auto/q:79/https://dndi.org/wp-content/uploads/2020/03/COVID19_icon.svg")
        
        await ctx.send(embed=em)
    
    @commands.command()
    async def bored(self,ctx):
        res = requests.get("https://www.boredapi.com/api/activity")
        act = res.json()["activity"]
        em = discord.Embed(title=f"Bored?", description=act, color=discord.Color.red())
        await ctx.send(embed=em)
    
    @commands.command()
    async def ideate(self,ctx):
        res = requests.get("http://itsthisforthat.com/api.php?json")
        this = res.json()["this"]
        that = res.json()["that"]
        em = discord.Embed(title=f"New Idea", description=f"Create a {this} for {that}", color=discord.Color.blue())
        await ctx.send(embed=em)
    
    @commands.command()
    async def shakespeare(self,ctx,*,text):
        text = parse.quote(text)
        res = requests.get("https://api.funtranslations.com/translate/shakespeare.json?text="+text)
        shakesphere = res.json()["contents"]["translated"]
        await ctx.reply(shakesphere)

    @commands.command()
    async def qr(self,ctx,url):
        url = pyqrcode.create(url)
        url.png("color.png", scale=6)
        with open("color.png","rb") as f:
            file = discord.File(f)
            em = discord.Embed(title="Here you Go!", color=discord.Color.blue())
            em.set_image(url="attachment://color.png")
            em.set_footer(text="Use a scanner to get access to the Link")
            await ctx.send(file=file, embed=em)
    
    @commands.command()
    async def snap(self,ctx,url):
        key = os.getenv("SSAPI")
        res = requests.get(f"https://shot.screenshotapi.net/screenshot?token={key}&url={url}")
        em = discord.Embed(title="Nice Webpage", color=discord.Color.blue())
        em.set_image(url=res.json()["screenshot"])
        em.set_footer(text="Site looks cool tho!")
        await ctx.send(embed=em)
    
    @commands.command()
    async def btc(self,ctx,currency="USD"):
        res = requests.get(f"https://api.coinbase.com/v2/prices/spot?currency={currency}")
        cvc = float(res.json()["data"]["amount"])
        await ctx.send(
            embed=discord.Embed(
                title=round(cvc,2), description=f"**1 BitCoin** equals {round(cvc, 2)} {currency} in {date.today()}", color=discord.Color.green(),
                thumbnail="https://static.news.bitcoin.com/wp-content/uploads/2019/09/bitcoin-breakout.jpg"
            )
        )
    


