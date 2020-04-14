import discord
import asyncio
client = discord.Client()
from commands import STATICS

@asyncio.coroutine
def ex(args, message, client, invoke):



        if len(args) > 0:
          if message.author.id == STATICS.authorid:
             print(args)
             game = message.content[6:]
             yield from client.change_presence(game=discord.Game(name=game))
             yield from client.send_message(message.channel, "Ich habe meinen Status zu " + game + " geändert")