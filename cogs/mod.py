import discord
from discord.ext import commands
import argparse
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
        parser = argparse.ArgumentParser()
        parser.add_argument('--target', type=int, required=True)
        parser.add_argument('--reason', type=str, nargs="+", required=False)
        args = parser.parse_args(msg)
        replies = ["Seems justified.", "Damn one player down!", "Funeral time ;-;", "Will he return back?"]
        user = await self.bot.fetch_user(args.target)
        args.target = user.name
        args.reason = listToString(args.reason)
        await ctx.guild.ban(user, reason=args.reason)
        if args.reason != None:
            msg = f"**{args.target}** will be kicked for **{args.reason}**. {random.choice(replies)}"
        else:
            msg = f"**{args.target}** was kicked! Ah how bad would the guy have beem?"
        em = discord.Embed(description=msg, color=discord.Color.blue())
        await ctx.send(embed=em)


    @commands.command()
    async def unban(self, ctx, *msg):
        """Unban a member"""
        parser = argparse.ArgumentParser()
        parser.add_argument('--target', type=int, required=True)
        parser.add_argument('--reason', type=str, nargs="+", required=False)
        args = parser.parse_args(msg)
        replies = ["Seems justified.", "Damn one player down!", "Funeral time ;-;", "Will he return back?"]
        user = await self.bot.fetch_user(args.target)
        args.target = user.name
        args.reason = listToString(args.reason)
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = user.name, user.discriminator

        for ban_entry in banned_users:
            user = ban_entry.user
        
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
        
        if args.reason != None:
            msg = f"**{args.target}** will be kicked for **{args.reason}**. {random.choice(replies)}"
        else:
            msg = f"**{args.target}** was kicked! Ah how bad would the guy have beem?"
        em = discord.Embed(description=msg, color=discord.Color.blue())
        await ctx.send(embed=em)

    @commands.command()
    async def kick(self, ctx, *msg):
        """Kick a member outta stage"""
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