import discord
from discord.ext import commands
import random
import dog
import requests

async def get(session: object, url: object) -> object:
    async with session.get(url) as response:
        return await response.text()

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def cat(self, ctx):
        response = requests.get('https://aws.random.cat/meow')
        data = response.json()
        embed = discord.Embed(
            title = 'Meow!',
            description = 'Cats :star_struck:',
            colour = discord.Colour.purple()
            )
        embed.set_image(url=data['file'])            
        embed.set_footer(text="")
        await ctx.send(embed=embed)
    
    @commands.command()
    async def dadjoke(self, ctx):
        from dadjokes import Dadjoke
        dadjoke = Dadjoke()
        await ctx.send(dadjoke.joke)
            
    