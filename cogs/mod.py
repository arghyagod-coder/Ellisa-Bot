import discord
from discord.ext import commands
import argparse
import asyncio
import random

def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele+' '  
    
    # return string  
    return str1 

class Moderator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def ban(self, ctx, *msg):
        """Ban a member permanently so that he/she can not join the server again"""
        if ctx.author.guild_permissions.ban_members:
            parser = argparse.ArgumentParser()
            parser.add_argument('--target', type=int, required=True)
            parser.add_argument('--reason', type=str, nargs="+", required=False)
            args = parser.parse_args(msg)
            replies = ["Begone!", "Cry Cry Cry More :O", "Never see you again!", "You pay for your sins!"]
            user = await ctx.guild.fetch_member(args.target)
            args.target = user.name
            args.reason = listToString(args.reason)
            await ctx.guild.ban(user, reason=args.reason)
            if args.reason != None:
                msg = f"**{args.target}** was banned for **{args.reason}**. {random.choice(replies)}"
            else:
                msg = f"**{args.target}** was banned!!"
            em = discord.Embed(description=msg, color=discord.Color.blue())
            em.set_image(url="https://c.tenor.com/SglvezQEKnAAAAAC/discord-ban.gif")

            await ctx.send(embed=em)
        else:
            await ctx.send(
                embed=discord.Embed(
                    title="Hey Sudo man",
                    description="No you cant do that",
                    color=discord.Color.blue()
                )
            )

    @commands.command()
    async def kick(self, ctx, *msg):
        """Kick a member outta stage"""
        if ctx.author.guild_permissions.kick_members:
            parser = argparse.ArgumentParser()
            parser.add_argument('--target', type=int, required=True)
            parser.add_argument('--reason', type=str, nargs="+", required=False)
            args = parser.parse_args(msg)
            replies = ["Seems justified.", "Damn one player down!", "Funeral time ;-;", "Will he return back?"]
            user = await self.bot.fetch_user(args.target)
            args.target = user.name
            args.reason = listToString(args.reason)
            await ctx.guild.kick(user)
            if args.reason != None:
                msg = f"**{args.target}** will be kicked for **{args.reason}**. {random.choice(replies)}"
            else:
                msg = f"**{args.target}** was kicked! Ah how bad would the guy have beem?"
            em = discord.Embed(description=msg, color=discord.Color.blue())
            await ctx.send(embed=em)
        else:
            await ctx.send(
                embed=discord.Embed(
                    title="Hey Sudo man",
                    description="No you cant do that",
                    color=discord.Color.blue()
                )
            )

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(ctx, member: discord.Member, mute_time):
        guild = ctx.guild
        for role in ctx.guild.roles:
            if role.name == "Muted":
                role = discord.utils.get(member.server.roles, name='Muted')

                await member.add_roles(role)
                await ctx.send("{} has has been muted!" .format(member.mention))
                await asyncio.sleep(mute_time)
                await member.remove_roles(role)
                await ctx.send("{} has been unmuted!" .format(member.mention))