import discord
import random
from discord.ext import commands

class Linux(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

