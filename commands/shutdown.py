import discord
import sys
from commands import STATICS


def ex(args, message, client, invoke):



        if len(args) == 0:
          if message.author.id == STATICS.authorid:
             yield from client.send_message(message.channel, "Ich fahre mich runter")
             sys.exit(0)
          else:
             yield from client.send_message(message.channel, "You are not my Master!")
