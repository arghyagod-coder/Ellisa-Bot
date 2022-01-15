import discord
import asyncio

def cembed(title=None, url=None, description=None, thumbnail=None, image=None, color=discord.Color.blue()):
	em = discord.Embed(title=title, description=description, color=color)
	if image != None:
		em.set_image(url=image)
	if thumbnail != None:
		em.set_thumbnail(
            url=thumbnail
        )
	return em

# Function to convert into UwU text
def generateUwU(input_text):
     
    # the length of the input text
    length = len(input_text)
     
    # variable declaration for the output text
    output_text = ''
     
    # check the cases for every individual character
    for i in range(length):
         
        # initialize the variables
        current_char = input_text[i]
        previous_char = '&# 092;&# 048;'
         
        # assign the value of previous_char
        if i > 0:
            previous_char = input_text[i - 1]
         
        # change 'L' and 'R' to 'W'
        if current_char == 'L' or current_char == 'R':
            output_text += 'W'
         
        # change 'l' and 'r' to 'w'
        elif current_char == 'l' or current_char == 'r':
            output_text += 'w'
         
        # if the current character is 'o' or 'O'
        # also check the previous character
        elif current_char == 'O' or current_char == 'o':
            if previous_char == 'N' or previous_char == 'n' or previous_char == 'M' or previous_char == 'm':
                output_text += "yo"
            else:
                output_text += current_char
         
        # if no case match, write it as it is
        else:
            output_text += current_char
 
    return output_text

def errembed(error:str):
    em = discord.Embed(title="Permission Denied", description=error, color=discord.Color.red())
    em.set_image(url="https://c.tenor.com/8eoRXRw-xE4AAAAC/richard-stallman-triggered.gif")
    em.set_footer(text="Retry with Root Priveleges...")
    return em

def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele+'\n'  
    
    # return string  
    return str1 

class Pages:
    def __init__(self, client):
        self.client = client
    async def pa1(self, embeds, ctx, start_from=0):
        message = await ctx.send(embed=embeds[start_from])
        pag = start_from
        await message.add_reaction("◀️")
        await message.add_reaction("▶️")

        def check(reaction, user):
            return (
                user != self.client.user
                and str(reaction.emoji) in ["◀️", "▶️"]
                and reaction.message.id == message.id
            )

        while True:
            try:
                reaction, user = await self.client.wait_for(
                    "reaction_add", timeout=360, check=check
                )            
                if str(reaction.emoji) == "▶️" and pag + 1 != len(embeds):
                    pag += 1
                    await message.edit(embed=embeds[pag])
                elif str(reaction.emoji) == "◀️" and pag != 0:
                    pag -= 1
                    await message.edit(embed=embeds[pag])
                await message.remove_reaction(reaction, user)
            except asyncio.TimeoutError:
                break