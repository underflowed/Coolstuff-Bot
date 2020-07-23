#Entry point for the bot
import discord
from cogs.Parser import Parser
from cogs.Challonge import ChallongeTournament


#Inheriting from discord.py module Client class
#Refer to https://discordpy.readthedocs.io/ for more info on attributes, methods, etc.
class CoolBotClient(discord.Client):

    #Important to mark new methods in this class as asynchronous
    async def on_ready(self):
        print('Logged on as {0}'.format((self.user)))

    async def on_message(self, message):
        parser = Parser()
        challonge = ChallongeTournament("7y3m8oss")
        if message.author == client.user:
            return
        if message.content.startswith('$'):
            cardname = message.content
            cardname = cardname.replace('$',"")
            cardname = cardname.replace(" ","%20")
            cardinfo, url = parser.GetCardText(cardname)
            await message.channel.send("```{0}```\n{1}".format(cardinfo, url))
        if message.content.startswith('!pairings'):
            await message.channel.send("{0}".format(challonge.GetPairings()))

client = CoolBotClient()
client.run("NzI4Nzg1OTUwMDIwMzM3Njk0.Xv_c_w.Shnpv4WH-R7hG3K7YMA2NL0rGlQ")