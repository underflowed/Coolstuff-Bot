import discord
from cogs.Parser import Parser


#Inheriting from discord.py module Client class
#Refer to https://discordpy.readthedocs.io/ for more info on attributes, methods, etc.
class CoolBotClient(discord.Client):

    async def on_ready(self):
        print('Logged on as {0}'.format((self.user)))

    async def on_message(self, message):
        parser = Parser()
        if message.author == client.user:
            return

        if message.content.startswith('$'):
            cardname = message.content
            cardname = cardname.replace('$',"")
            cardinfo, url = parser.GetCardText(cardname)
            await message.channel.send("```{0}```\nget it today at {1} !".format(cardinfo, url))
            


client = CoolBotClient()
client.run("NzI4Nzg1OTUwMDIwMzM3Njk0.Xv_c_w.Shnpv4WH-R7hG3K7YMA2NL0rGlQ")