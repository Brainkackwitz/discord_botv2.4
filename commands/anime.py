perm = 1
import discord
List = "blue exorcist \n""shaman king\n""on game no life\n""btoooom\n""high school dxd\n""high school of the dead\n""Naruto\n""Yugi oh\n""Pokemon\n""Digimon\n""Holy Knight\n""Sword of the Stranger\n""King of Thorn\n""Fate Stay Night\n""Inuyasha\n""Noragami\n""sword art online\n""Toradora\n""Clannad\n""Blood Lad\n""Danganronpa\n""Danmachi\n""The Irregular at Magic High School\n""Aesthetica of a Rogue Hero\n"+"Seraph of the End\n""Terror in Tokyo\n""Detektiv Conan\n""Death note\n""Erased\n""Attack on Titan\n""Gate\n""Tokyo Ghoul\n""Ajin: Demi-Human\n""Charlotte\n""Shimoneta\n""Guilty Crown\n""Psycho-Pass\n""Anohana\n""Death Parade\n""Steins;Gate?\n""A Silent Voice\n""Prison School\n""Kämpfer\n""Akuma no Riddle\n""Akame Ga Kill\n""K Project\n""parasyte\n""Black Lagoon\n""Kill La Kill\n""Yamada-kun to 7-nin no Majo\n"+"Gurren Lagann\n""coppelion\n""Re: Zero Kara Hajimeru Isekai Seikatsu\n""Love Hina\n""Rokka no Yuusha\n""B: The Beginning\n""undefeated bahamut\n""Fuuka\n""Hai to Gensou no Grimgar\n""USAGI DROP\n""blood blockade battlefront\n""Sword Gai: The Animation\n""Romeo × Juliet\n""brynhildr in the darkness\n""Ookami Shoujo to Kuro Ouji\n""trinity seven\n""Summer wars\n""patema inverted\n""5 Centimeters Per Second\n"""




def ex(args, message, client, invoke):
    args = message.content.split
    if args(" ")[1:]:
         if args("List")[1:]:
            embed = discord.Embed(
                title="List",
                color=0xe67e22,
                description=List
            )
            embed.set_author(
                name="Anime list",
                icon_url="https://rocketdock.com/images/screenshots/21.png",
                url="https://discordapp.com/developers/applications "
            )
            embed.set_footer(
                text="Ein bot von Brainkackwitz"
            )
            embed.set_thumbnail(
                url="http://images6.fanpop.com/image/photos/35100000/Asuna-Yuuki-asuna-yuuki-35129718-844-886.jpg"
            )
            yield from client.send_message(message.channel, embed=embed)
            return
         if args("list")[1:]:
            embed = discord.Embed(
                title="List",
                color=0xe67e22,
                description=List
            )
            embed.set_author(
                name="Anime list",
                icon_url="https://rocketdock.com/images/screenshots/21.png",
                url="https://discordapp.com/developers/applications "
            )
            embed.set_footer(
                text="Ein bot von Brainkackwitz"
            )
            embed.set_thumbnail(
                url="http://images6.fanpop.com/image/photos/35100000/Asuna-Yuuki-asuna-yuuki-35129718-844-886.jpg"
            )
            yield from client.send_message(message.channel, embed=embed)
            return
            # error
         if args("Wallpaper")[1:]:
            embed = discord.Embed(
                title="List",
                color=0xe67e22,
                description="https://wall.alphacoders.com/by_category.php?id=3&name=Anime+Wallpapers&lang=German&page=4"
            )
            embed.set_author(
                name="Wallpaper-list",
                url="https://discordapp.com/developers/applications "
            )
            embed.set_footer(
                text="Ein bot von Brainkackwitz"
            )
            embed.set_thumbnail(
                url="http://img.talkandroid.com/uploads/2016/10/google_wallpapers_app_icon.png"
            )
            yield from client.send_message(message.channel, embed=embed)
            return
            # error
         if args("wallpaper")[1:]:
           embed = discord.Embed(
               title="List",
               color=0xe67e22,
               description="https://wall.alphacoders.com/by_category.php?id=3&name=Anime+Wallpapers&lang=German&page=4"
           )
           embed.set_author(
               name="Wallpaper-list",
               url="https://discordapp.com/developers/applications "
           )
           embed.set_footer(
               text="Ein bot von Brainkackwitz"
           )
           embed.set_thumbnail(
               url="http://img.talkandroid.com/uploads/2016/10/google_wallpapers_app_icon.png"
           )
           yield from client.send_message(message.channel, embed=embed)
           return
           # error
         if args("W")[1:]:
            embed = discord.Embed(
                title="List",
                color=0xe67e22,
                description="https://wall.alphacoders.com/by_category.php?id=3&name=Anime+Wallpapers&lang=German&page=4"
            )
            embed.set_author(
                name="Wallpaper-list",
                url="https://discordapp.com/developers/applications "
            )
            embed.set_footer(
                text="Ein bot von Brainkackwitz"
            )
            embed.set_thumbnail(
                url="http://img.talkandroid.com/uploads/2016/10/google_wallpapers_app_icon.png"
            )
            yield from client.send_message(message.channel, embed=embed)
            return
            # error
         if args("w")[1:]:
           embed = discord.Embed(
               title="List",
               color=0xe67e22,
               description="https://wall.alphacoders.com/by_category.php?id=3&name=Anime+Wallpapers&lang=German&page=4"
           )
           embed.set_author(
               name="Wallpaper-list",
               url="https://discordapp.com/developers/applications "
           )
           embed.set_footer(
               text="Ein bot von Brainkackwitz"
           )
           embed.set_thumbnail(
               url="http://img.talkandroid.com/uploads/2016/10/google_wallpapers_app_icon.png"
           )
           yield from client.send_message(message.channel, embed=embed)
           return
           # error
         #error
         else:
             embed = discord.Embed(
                 title="error",
                 icon_url="http://img1.wikia.nocookie.net/__cb20070302203617/beamer/images/7/71/Zahnrad.png",
                 description="this command not exist",
                 color=0xe40000,  # red
             )
             embed.set_footer(
                 text="Ein bot von Brainkackwitz"
             )
             embed.set_thumbnail(
                 url="http://img1.wikia.nocookie.net/__cb20070302203617/beamer/images/7/71/Zahnrad.png"
             )
             yield from client.send_message(message.channel, embed=embed)
             return
         # commands
    else:
        embed = discord.Embed(
            title="Commands",
            color=600,  # blue
            description="~anime list\n""~anime wallpaper"
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
