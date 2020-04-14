import discord
perm = 3

def ex(args, message, client, invoke):
    args = message.content.split

    ico = "http://www.clker.com/cliparts/2/9/c/7/11949867871570711906table_tennis_omar_abo-na_01.svg.hi.png"
    if args(" ")[1:]:
        #url
        name = str(args()[2:3])[2:-2]
        punkte = str(args()[3:4])[2:-2]
        VEREIN = str(args()[4:5])[2:-2]

        if args("c")[1:]:

            try:

                f = open("/home/pi/Desktop/bots/discord_botv2.4/commands/tischtennis/"+name+".txt", "x")
                f.write(VEREIN+"\n"+name+"\n"+punkte)

            except:
                f = open("/home/pi/Desktop/bots/discord_botv2.4/commands/tischtennis/"+name+".txt", "w")
                f.write(VEREIN+"\n"+name+"\n"+punkte)

                f.close()
                print('exist')
                pass



        else:
            try:
                f = open("/home/pi/Desktop/bots/discord_botv2.4/commands/tischtennis/"+str(args()[1:2])[2:-2]+".txt", "r")



                t = discord.Embed(
                    title="VEREIN",
                    color=0xe67e29,
                    description=f.readline(),
                    url = "https://www.ttv-koenigstein.de/php/page.php?name=start"
                    )
                t.set_author(
                    name=f.readline(),
                    icon_url=ico,
                    url="https://dresden.tischtennislive.de/?L1=Ergebnisse&L2=TTStaffeln&L2P=8715&L3=Spieler&L3P=83141&Page=Vorrunde"
                    )

                t.add_field(
                    name="LivePZ",
                    value=f.readline(),

                    )
                t.set_footer(
                    text="Function by Brainkackwitz"
                    )

                yield from client.send_message(message.channel, embed=t)
                return
            except:
                embed = discord.Embed(
                    title="Commands",
                    color=600,#blue
                    description="https://dresden.tischtennislive.de/?L1=Public\n~Tischtennis c | create / name / punkte / verein\n~Tischtennis name"
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

                return
                pass





    #commands
    else:
        embed = discord.Embed(
            title="Commands",
            color=600,#blue
            description="https://dresden.tischtennislive.de/?L1=Public\n~Tischtennis c | create / name / punkte / verein\n~Tischtennis name"
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
