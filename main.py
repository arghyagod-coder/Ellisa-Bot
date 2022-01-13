import discord
from discord.ext import commands
import os
import argparse
import random
import util
from cogs.mod import Moderator
from cogs.help import Help


TOKEN = os.getenv("TOKEN")
client = commands.Bot(command_prefix = '=')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command() # Syntax to define a command
async def hi(ctx): # ctx stands for context object. It has to be passed in almost every command. It has many objects
    await ctx.send(f"Hello {ctx.author.mention}")


client.add_cog(Moderator(client))
client.remove_command("help")
client.add_cog(Help(client))

# @client.command() # Syntax to define a command
# async def kick(ctx, *msg):
# 	parser = argparse.ArgumentParser()
# 	parser.add_argument('--target', type=int, required=True)
# 	parser.add_argument('--reason', type=str, required=False)
# 	args = parser.parse_args(msg)
# 	replies = ["Seems justified.", "Damn one player down!", "Funeral time ;-;", "Will he return back?"]
# 	user = await client.fetch_user(args.target)
# 	args.target = user.name
# 	if args.reason != None:
# 		msg = f"**{args.target}** will be kicked for **{args.reason}**. {random.choice(replies)}"
# 	else:
# 		msg = f"**{args.target}** was kicked! Ah how bad would the guy have beem?"
# 	em = discord.Embed(description=msg, color=discord.Color.blue())
# 	await ctx.send(embed=em)


client.run(TOKEN)