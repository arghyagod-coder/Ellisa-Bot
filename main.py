import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from cogs.misc import Miscallenous
from cogs.help import Help
from cogs.fun import Fun
from cogs.sysadmin import Sysadmin
from cogs.linux import Linux
from cogs.images import Images
from cogs.music import Music
from cogs.api import API
# from cogs.emoji import emoji

load_dotenv()

intents = discord.Intents.default()
intents.members = True
TOKEN = os.getenv("TOKEN")
client = commands.Bot(command_prefix = '$', intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command() # Syntax to define a command
async def hi(ctx): # ctx stands for context object. It has to be passed in almost every command. It has many objects
    await ctx.send(f"Hello {ctx.author.mention}")

@client.event
async def on_message(message):
    await client.process_commands(message)
    if f"<@!{client.user.id}>" in message.content:
        em = discord.Embed(
            title="Hello There! Ellisa at your service!",
            description="**Prefix:** $\nI am a general purpose bot with awesome features that are worth trying out! For checking out all my features, use `$man` or `$manual`.",
            color=discord.Color.blue(),
            author="Ellisa"
        )
        em.set_image(url="https://media.discordapp.net/attachments/822445271568351274/931163021609435206/Futuristic_HiTech_Intro_free.mp4")
        await message.reply(embed=em)

client.remove_command("help")
client.add_cog(Help(client))
client.add_cog(Miscallenous(client))
client.add_cog(Fun(client))
client.add_cog(Linux(client))
client.add_cog(Sysadmin(client))
client.add_cog(Images(client))
client.add_cog(Music(client))
client.add_cog(API(client))
# cogs = ["cogs.emoji"]
# for cog in cogs:
#     client.load_extension(cog)

client.run(TOKEN)