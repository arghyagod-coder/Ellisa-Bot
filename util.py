import discord

def cembed(title=None, url=None, description=None, thumbnail=None, image=None, color=discord.Color.blue()):
	em = discord.Embed(title=title, description=description, color=color)
	if image != None:
		em.set_image(url=image)
	if thumbnail != None:
		em.set_thumbnail(
            url=thumbnail
        )
	return em