import discord
import random
from discord.ext import commands
import util
from discord.utils import get

ownerid= "794984520712847390"

class Sysadmin(commands.Cog):
    """Basic Administration and Management-related Commands"""

    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def ls(self,ctx,arg):
        '''```
ls - List specific iterables
        
SYNOPSIS:
ls <DIRECTORY>

USECASES:
ls servers
    List all servers Ellisa is a member of
ls members
    List all members of the current server
ls bots
    List all the bot users in the current server```'''
        try:
            if arg=="servers":
                guilds = self.bot.guilds
                glist = ""
                for guild in guilds:
                    glist+=guild.name+"\n"
                em = discord.Embed(title=f"Currently in {len(guilds)} Servers", description=glist, author=True)
                await ctx.send(embed=em)
            elif arg=="members":
                memberlist=[]
                for member in ctx.guild.members:
                    memberlist.append(member.name+"#"+member.discriminator)
                desc = ''
                for memberinfo in memberlist: 
                    desc += memberinfo+'\n'  
                em = discord.Embed(description=f"**Member List**\n\n**Count: {ctx.guild.member_count}**\n\n{desc}", color=discord.Color.blue())
                await ctx.send(embed=em)
            elif arg=="bots":
                memberlist=[]
                for member in ctx.guild.members:
                    if member.bot==True:
                        memberlist.append(member.name+"#"+member.discriminator)
                desc = ''
                for memberinfo in memberlist: 
                    desc += memberinfo+'\n'  
                em = discord.Embed(description=f"**Bot List**\n\n**Count: {len(memberlist)}**\n\n{desc}", color=discord.Color.blue())
                await ctx.send(embed=em)
        except:
            pass

    @commands.command()
    async def rm(self,ctx,flag,member:discord.Member,*,reason=None):
        if ctx.author.guild_permissions.ban_members and ctx.author.guild_permissions.kick_members: 
            if reason != None:
                reason = reason.replace("--reason ", "")     
            if flag=="-r":
                await ctx.guild.kick(member)
                replies = ["Seems justified.", "Damn one player down!", "Funeral time ;-;", "Will he return back?"]
                if reason != None:
                    msg = f"**{member.name}** was kicked for **{reason}**. {random.choice(replies)}"
                else:
                    msg = f"**{member.name}** was kicked! Ah how bad would the guy have beem?"
                em = discord.Embed(description=msg, color=discord.Color.red(), author=True)
                em.set_thumbnail(url=member.avatar_url)
                em.set_image(url="https://c.tenor.com/_OJw-eCkMYAAAAAC/anime-naruto.gif")
                await ctx.send(embed=em)
            elif flag=="-rf":
                await member.ban(reason=reason)
                replies = ["Begone!", "Cry Cry Cry More :O", "Never see you again!", "You pay for your sins!"]
                if reason != None:
                    msg = f"**{member.name}** was banned for **{reason}**. {random.choice(replies)}"
                else:
                    msg = f"**{member.name}** was banned!"
                em = discord.Embed(description=msg, color=discord.Color.red(), author=True)
                em.set_image(url="https://c.tenor.com/SglvezQEKnAAAAAC/discord-ban.gif")
                em.set_thumbnail(url=member.avatar_url)
                await ctx.send(embed=em)
            else:
                em = discord.Embed(title="Invalid Flags", description="**Invalid Flags used:**\n\nAvailable Options are:\n\nrm -rf <user>      Ban a Member\nrm -r <user>     Kick a Member\n\nUse the correct options. If this was not what you intended, use `$help` to check other Commands under **Sysadmin** Category", color=discord.Color.red())
                em.set_image(url="https://4kwallpapers.com/images/walls/thumbs_2t/926.png")
                ctx.send(embed=em)
        else:
            await ctx.send(embed=util.errembed(f"Permission Denied: Cannot remove /{ctx.guild.name}/{member.name}"))
    
    @commands.command()
    async def mkdir(self, ctx,*,category_name):
        if ctx.author.guild_permissions.manage_guild:
            await ctx.guild.create_category(category_name)
            await ctx.send(
                embed=discord.Embed(
                    title="Process Completed",
                    description=f"Created a new category **./{category_name}**",
                    color=discord.Color.blue(),
                    thumbnail=self.bot.user.avatar_url_as(format="png")
                    )
                
                )
        else:
            await ctx.send(embed=util.errembed(f"Permission Denied: Cannot create category ./{category_name}"))
    
    @commands.command()
    async def rmdir(self, ctx,*,category_name):
        if ctx.author.guild_permissions.manage_guild:
            category = get(ctx.guild.categories, name = category_name)
            await category.delete()
            await ctx.send(
                embed=discord.Embed(
                    title="Execution Completed",
                    description=f"Removed category **./{category_name}**",
                    color=discord.Color.blue(),
                    thumbnail=self.bot.user.avatar_url_as(format="png")
                    )
                
                )
        else:
            await ctx.send(embed=util.errembed(f"Permission Denied: Cannot remove category ./{category_name}"))
    
    @commands.command()
    async def touch(self, ctx,channel,*, category=None):
        if ctx.author.guild_permissions.manage_channels:
            try:
                if category == None:
                    await ctx.guild.create_text_channel(channel)
                elif category.isnumeric()==True:
                    category = discord.utils.get(ctx.guild.categories, id=category)
                    await ctx.guild.create_text_channel(channel, category = category)
                else:
                    category = get(ctx.guild.categories, name = category)
                    await ctx.guild.create_text_channel(channel, category = category)
            except:
                await ctx.send(
                    embed=discord.Embed(
                        title="Execution Failed.",
                        description="Use a Proper Channel Name or Category Name\n\n**Possible Usecases:**\n\n$touch <channel_name>\n$touch <channel_name> <category_name>**",
                        color=discord.Color.blue()
                    )
                    )
        else:
            if category==None:
                await ctx.send(embed=util.errembed(f"Permission Denied: Cannot create chanel ./{channel}"))
            else:
                await ctx.send(embed=util.errembed(f"Permission Denied: Cannot create channel ./{category}/{channel}"))

    
    @commands.command()
    async def fd(self, ctx, channel:discord.TextChannel, *, text):
        msglist = []
        embeds = []
        i = 1
        messages = await channel.history(limit=500).flatten()
        for message in messages:
            #print(message.author.name + ': ' + message.content)
            if str(message.clean_content).lower().find(str(text).lower())>=0:
                msglist.append(f"**Found Result {i}:**\n\n{message.clean_content}")
                i+=1
        for i in range(len(msglist)//10):
            e = util.listToString(msglist[i*10:(i+1)*10])
            embed = discord.Embed(
                title=f"Found {len(msglist)} Results",
                description=f"Here are the results:\n\n{e}",
                color=discord.Color.blue(),             
            )
            embeds.append(embed)                

        if len(embeds)==0:            
            e = util.listToString(msglist)
            print(e)
            embed = discord.Embed(
                title=f"Found {len(msglist)} Results",
                description=f"Here are the results:\n\n{e}",
                color=discord.Color.blue(),             
            )
            await ctx.send(embed=embed)  
            return      
        await util.Pages(self.bot).pa1(embeds,ctx)

    @commands.command()
    async def history(self, ctx, channel:discord.TextChannel, limit:int):
        msglist = ""
        messages = await channel.history(limit=limit).flatten()
        for message in messages:
            msglist += f"**{str(message.author)}**: {message.clean_content}\n"
        em = discord.Embed(title="Message History", description=f"The last {limit} Messages in **{ctx.guild.name}**:\n\n{msglist}", author=True)
        await ctx.author.send(embed=em)
        await ctx.reply("**Message History** sent in your DMs")
    
    @commands.command()
    async def chown(self,ctx,member:discord.Member,*,role):
        if ctx.author.guild_permissions.manage_roles:
            try:
                role = get(ctx.guild.roles, name=role)
                await member.add_roles(role)
                await ctx.send(
                    embed=discord.Embed(
                        title="Execution Success.",
                        description=f"Role **{role.name}** was added to **{member.name}**",
                        color=discord.Color.blue()
                    )
                    )

            except Exception as e:
                print(e)
                await ctx.send(
                    embed=discord.Embed(
                        title="Execution Failed.",
                        description="Use a Proper Role Name. Note not to mention the role but just write it's name.\n\n**Possible Usecases:**\n\n$chown <user_mention> <role_name>\n$touch <channel_name> <category_name>**",
                        color=discord.Color.blue()
                    )
                    )

    @commands.command()
    async def report(self,ctx,*,bug):
        msg = f"\n\nNew Bug Reported by {ctx.author.name}#{ctx.author.discriminator} of {ctx.guild.name}:\n\n{bug}"
        with open("bugreport.txt", "a") as f:
            f.write(msg)
            f.close()
        await ctx.send(
            embed=discord.Embed(
                title="Bug Reported Successfully",
                description="Do not worry, the developers will soon look into your report",
                color=discord.Color.blue()
            )
        )
        