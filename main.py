import asyncio as asyncio
from discord import Game, Embed
import discord
import json
import os.path
from discord.ext import commands


import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select


minutes = 0
hour = 0
days = 0

from commands import test,test1, STATICS, SECRETS, game , cmd_ping,cmd_autorole, cmd_clear,anime,Tischtennis,lol_user,shutdown,search,info,pw,miesmuschel,tell
testmsgid = None
testmsguser = None
client = discord.Client()
commands = {
    "tell": tell,
    "tes": test,"test": test1,
    "ping": cmd_ping,"Ping!": cmd_ping,
    "info": info,
    "game": game,"g":game,
    "autorole": cmd_autorole,
    "clear": cmd_clear,"c":cmd_clear,"C":cmd_clear,"Clear":cmd_clear,
    "anime": anime,"Anime": anime,
    "search": search,
    "shutdown": shutdown,
    "lol": lol_user,
    "T":Tischtennis,"Tischtennis":Tischtennis,"tischtennis":Tischtennis,
    "pw":pw,
    "muschel": miesmuschel

}

@client.event
@asyncio.coroutine
def on_ready():
    print("Bot is logged in successfully. Running on servers:\n")
    for s in client.servers:
        print("  - %s (%s)" % (s.name, s.id))
    yield from client.change_presence(game=Game(name="Version: "+STATICS.description))

@client.event
@asyncio.coroutine
def on_message(message):
    if message.content.startswith(STATICS.PREFIX):
        invoke = message.content[len(STATICS.PREFIX):].split(" ")[0]
        args = message.content.split(" ")[1:]
        if commands.__contains__(invoke):
            yield from commands.get(invoke).ex(args, message, client, invoke)
        else:
            yield from client.send_message(message.channel, embed=Embed(color=discord.Color.red(), description=(
                    "The command `%s` is not valid!" % invoke)))
    if message.content.startswith('?user'):
      try:
          user = message.mentions[0]
          userjoinedat = str(user.joined_at).split('.', 1)[0]
          usercreatedat = str(user.created_at).split('.', 1)[0]
          userembed = discord.Embed(
              title="Username:",
              description=user.name,
              color=0xe67e22
          )
          userembed.set_author(
              name="User Info"
          )
          userembed.add_field(
              name="Joined the server at:",
              value=userjoinedat
          )
          userembed.add_field(
              name="User Created at:",
              value=usercreatedat
          )
          userembed.add_field(
              name="Discriminator:",
              value=user.discriminator
          )
          userembed.add_field(
              name="User ID:",
              value=user.id
          )
          yield from client.send_message(message.channel, embed=userembed)
      except IndexError:
          yield from client.send_message(message.channel, "Ich konnte den User nicht finden.")
      except:
          yield from client.send_message(message.channel, "Sorry Error")
      finally:
          pass
    if message.content.startswith('?uptime'):
        yield from client.send_message(message.channel,
                                       "Ich bin schon {0} Tage {1} stunde/n und {2} minuten online auf {3}.".format(days, hour,minutes,message.server))
    if message.content.lower().startswith("?test"):
        botmsg = yield from client.send_message(message.channel, "👍 oder 👎")

        yield from client.add_reaction(botmsg, "👍")
        yield from client.add_reaction(botmsg, "👎")

        global testmsgid
        testmsgid = botmsg.id

        global testmsguser
        testmsguser = message.author
    if message.content.lower().startswith("?Teams"):
        embed = discord.Embed(
            title="Command",
            color=600,  # blue
            description="**@Brainhelfer maketeams** [anzahl der spieler] [anzahl der Teams]\n""Dann nach geh in den waiting room und gib join ein\n""am ende wenn alle pätze voll sind werden alle gemoved\n""oder mit **closeteams** gemoved wenn nicht alle pätze voll sind"
        )
        embed.set_author(
            name="Command list",
            icon_url="http://img1.wikia.nocookie.net/__cb20070302203617/beamer/images/7/71/Zahnrad.png",
            url="https://discordapp.com/developers/applications "
        )
        embed.set_footer(
            text="Ein bot von Brainkackwitz"
        )
        embed.set_thumbnail(
            url="http://img1.wikia.nocookie.net/__cb20070302203617/beamer/images/7/71/Zahnrad.png"
        )
        yield from client.send_message(message.channel, embed=embed)
    if message.content.lower().startswith("?teams"):
            embed = discord.Embed(
                title="Command",
                color=600,  # blue
                description="**@Brainhelfer maketeams** [anzahl der spieler] [anzahl der Teams]\n""Dann nach geh in den waiting room und gib join ein\n""am ende wenn alle pätze voll sind werden alle gemoved\n""oder mit **closeteams** gemoved wenn nicht alle pätze voll sind"
            )
            embed.set_author(
                name="Command list",
                icon_url="http://img1.wikia.nocookie.net/__cb20070302203617/beamer/images/7/71/Zahnrad.png",
                url="https://discordapp.com/developers/applications "
            )
            embed.set_footer(
                text="Ein bot von Brainkackwitz"
            )
            embed.set_thumbnail(
                url="http://img1.wikia.nocookie.net/__cb20070302203617/beamer/images/7/71/Zahnrad.png"
            )
            yield from client.send_message(message.channel, embed=embed)
    if message.content.lower().startswith("?Team"):
                embed = discord.Embed(
                    title="Command",
                    color=600,  # blue
                    description="**@Brainhelfer maketeams** [anzahl der spieler] [anzahl der Teams]\n""Dann nach geh in den waiting room und gib join ein\n""am ende wenn alle pätze voll sind werden alle gemoved\n""oder mit **closeteams** gemoved wenn nicht alle pätze voll sind"
                )
                embed.set_author(
                    name="Command list",
                    icon_url="http://img1.wikia.nocookie.net/__cb20070302203617/beamer/images/7/71/Zahnrad.png",
                    url="https://discordapp.com/developers/applications "
                )
                embed.set_footer(
                    text="Ein bot von Brainkackwitz"
                )
                embed.set_thumbnail(
                    url="http://img1.wikia.nocookie.net/__cb20070302203617/beamer/images/7/71/Zahnrad.png"
                )
                yield from client.send_message(message.channel, embed=embed)
    if message.content.lower().startswith("?team"):
                    embed = discord.Embed(
                        title="Command",
                        color=600,  # blue
                        description="**@Brainhelfer maketeams** [anzahl der spieler] [anzahl der Teams]\n""Dann nach geh in den waiting room und gib join ein\n""am ende wenn alle pätze voll sind werden alle gemoved\n""oder mit **closeteams** gemoved wenn nicht alle pätze voll sind"
                    )
                    embed.set_author(
                        name="Command list",
                        icon_url="http://img1.wikia.nocookie.net/__cb20070302203617/beamer/images/7/71/Zahnrad.png",
                        url="https://discordapp.com/developers/applications "
                    )
                    embed.set_footer(
                        text="Ein bot von Brainkackwitz"
                    )
                    embed.set_thumbnail(
                        url="http://img1.wikia.nocookie.net/__cb20070302203617/beamer/images/7/71/Zahnrad.png"
                    )
                    yield from client.send_message(message.channel, embed=embed)
    if message.content.lower().startswith("?lol"):

        search = message.content[5:]
        driver = webdriver.Firefox()
        url = "https://euw.op.gg/summoner/userName="
        driver.get(url)
        inputElement = driver.find_element_by_name("userName")
        inputElement.send_keys(search)
        inputElement.submit()
        try:
            time.sleep(5)
            elo = str(driver.find_element_by_class_name("TierRank").text)
            lp = str(driver.find_element_by_class_name("LeaguePoints").text)
            winr = str(driver.find_element_by_class_name("winratio").text)
            yield from client.send_message(message.channel, "Player "+search+"\n"+elo+"\n"+lp+"\n"+winr)


            #driver.find_element_by_xpath('//h3[@class="LC20lb" and not(contains(text(), "org")) and not(contains(text(), "wikipedia"))]').click()


        except:
            serverchannel = discord.Object(STATICS.channelname_Bot_channel)
            yield from client.send_message(message.channel, "Es gibt einen fehler!")




#join and left the server tell in the chat
@client.event
@asyncio.coroutine
def on_member_remove(member):
    serverchannel = discord.Object(STATICS.channelname_Bot_channel)
    yield from client.send_message(serverchannel, "Bye Bye {0}".format(member.name))

@client.event
@asyncio.coroutine
def on_member_join(member):
    serverchannel = discord.Object(STATICS.channelname_Bot_channelforall)
    msg = "Willkommen ⭐{0}⭐ auf **{1}**".format(member.mention, member.server.name)
    yield from client.send_message(serverchannel, msg)
    yield from client.send_message(member, "**Hey!** %s \n\nWelcome on the official %s Discord-Server from %s\n\nNow have a nice day!" % (member.name,member.server.name, member.server.owner.mention))
    role = cmd_autorole.get(member.server)
    if not role == None:
        yield from client.add_roles(member, role)
        yield from client.send_message(member, "You got automatically assigned the role **" + role.name + "**!\nA moderator will register you")


@client.event
@asyncio.coroutine
async def tutorial_uptime():
    await client.wait_until_ready()
    global minutes
    minutes = 0
    global hour
    hour = 0
    global days
    days = 0

    while not client.is_closed:
        await asyncio.sleep(60)
        minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1
        if hour == 24:
            hour = 0
            days += 1
client.loop.create_task(tutorial_uptime())
@client.event
@asyncio.coroutine
def on_reaction_add(reaction, user):
        msg = reaction.message

        if reaction.emoji == "👍" and msg.id == testmsgid and user == testmsguser:
            role = discord.utils.find(lambda r: r.name == "ROLE", msg.server.roles)
            yield from client.add_roles(user, role)

        if reaction.emoji == "👎" and msg.id == testmsgid and user == testmsguser:
            role = discord.utils.find(lambda r: r.name == "ROLE", msg.server.roles)
            yield from client.remove_roles(user, role)



client.run(SECRETS.TOKEN)
