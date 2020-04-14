import discord
from discord.ext import commands

client = discord.Client()
import time
import csv
def ex(args, message, client, invoke):
    dateuhandler = open("/home/pi/Desktop/bots/discord_botv2.4/commands/pw.csv")

    inhalt = dateuhandler.read()


    tabelle = []

    zeilen = inhalt.split('\n')
    for i in range(len(zeilen)):
        spalten = zeilen[i].split(',')
        tabelle.append(spalten)

    if args in tabelle:
        yield from client.send_message(message.channel, "link")



    else:
        yield from client.send_message(message.channel, "Worng")
