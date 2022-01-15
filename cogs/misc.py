import discord
from discord.ext import commands
import asyncio
import random
from PIL import Image
import util

def hexToRGB(hex):
    hex=hex.lstrip('#')
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

class Miscallenous(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(aliases=["av", "pfp"])
    async def avatar(self, ctx, member: discord.Member=None):
        if member != None:
            em = discord.Embed(title=f"{member.name}'s Avatar", url=member.avatar_url, color=discord.Color.blue())
            em.set_image(url=member.avatar_url)
        else:
            em = discord.Embed(title=f"Here's Your Avatar", url=ctx.author.avatar_url, color=discord.Color.blue())
            em.set_image(url=ctx.author.avatar_url)
        await ctx.send(embed=em)

    @commands.command(aliases=[])
    async def hcolor(self, ctx, hexcode):
        try:
            im = Image.new("RGB", (500,500), hexcode)
            im.save( "color.png")
            with open('color.png', 'rb') as f:
                picture = discord.File(f)
                em = discord.Embed(title=f"Here You Go!", color=discord.Color.blue())
                em.set_image(url="attachment://color.png")
                await ctx.send(file=picture, embed=em)
        except Exception:
            em = discord.Embed(title="Operation Failed", description="Make sure you have entered a valid HEX Code. \n\nFormat: #HEXCODE\n\nTry Again", color=discord.Color.red())
            await ctx.send(embed=em)
    
    @commands.command(aliases=[])
    async def randomcolor(self, ctx):
        r = lambda: random.randint(0,255)
        hexcode = '#%02X%02X%02X' % (r(),r(),r())
        im = Image.new("RGB", (500,500), hexcode)
        im.save( "color.png")
        with open('color.png', 'rb') as f:
            picture = discord.File(f)
            em = discord.Embed(title=f"Here You Go!", description=f"HEX: {hexcode}\nRGB: {hexToRGB(hexcode)}", color=discord.Color.blue())
            em.set_image(url="attachment://color.png")
            await ctx.send(file=picture, embed=em)
    
    @commands.command(aliases=["uid"])
    async def getuid(self, ctx, member:discord.Member=None):
        if member!=None:
            em = discord.Embed(title=f"{member.name} 's ID", description=member.id, color=discord.Color.green())
        else:
            em = discord.Embed(title=f"Your ID", description=ctx.author.id, color=discord.Color.green())
        await ctx.send(embed=em)
    
    @commands.command(aliases=["sts"])
    async def status(self, ctx, url):
        import requests
        status = requests.get(url)
        em = discord.Embed(title=status.status_code, description=f"Status Code: **{status.status_code}**\nOk? {status.ok}\n{url}", color=discord.Color.blue())
        await ctx.send(embed=em)
    
    @commands.command(aliases=["mc"])
    async def membercount(self, ctx):
        em = discord.Embed(description=f"The Server has Exactly **{ctx.guild.member_count} members.**", color=discord.Color.blue())
        await ctx.send(embed=em)
    
    @commands.command(aliases=[])
    async def members(self, ctx):
        memberlist=[]
        for member in ctx.guild.members:
            memberlist.append(member.name+"#"+member.discriminator)
        desc = ''
        for memberinfo in memberlist: 
            desc += memberinfo+'\n'  
        em = discord.Embed(description=f"**Member List**\n\n{desc}", color=discord.Color.blue())
        await ctx.send(embed=em)
    
    @commands.command(aliases=["uinfo", "whois"])
    async def userinfo(self,ctx, *, user: discord.Member = None): # b'\xfc'
        if user is None:
            user = ctx.author      
        date_format = "%a, %d %b %Y %I:%M %p"
        embed = discord.Embed(color=discord.Color.blue(), description=user.mention)
        embed.set_author(name=str(user), icon_url=user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        embed.add_field(name="Join position", value=str(members.index(user)+1))
        embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        embed.add_field(name="Guild permissions", value=perm_string, inline=False)
        embed.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=embed)
    
    format = "%a, %d %b %Y | %H:%M:%S %ZGMT"

    @commands.command()
    async def serverinfo(self, ctx):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)

        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)

        icon = str(ctx.guild.icon_url)
        
        embed = discord.Embed(
            title=name + " Server Information",
            description=description,
            color=discord.Color.blue()
            )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=id, inline=True)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)

        await ctx.send(embed=embed)
    
    @commands.command()
    async def uwuify(self, ctx, *, text):
        uwu = util.generateUwU(text)
        await ctx.send(f"**UwU Text**:\n\n{uwu}")
