import random
import discord
List = ["Nein!", "Vielleicht Später", "Das weiß du nicht?", "Das stimmt wohl!", "Korekt!", "Du hast gelogen!", "Ja", "Frag wen anders"]




def ex(a ,message, client, invoke):

    embed = discord.Embed(
        title=List[random.randrange(0,8)],
        color=0xe67e22
        )
    embed.set_author(
        name="Magische Miesmuschel",
        )
    embed.set_footer(
        text="Ein bot von Brainkackwitz"
        )
    embed.set_thumbnail(
        url="https://img-android.lisisoft.com/imgmic/1/8/3781-i-com.alex.tools.magischemiesmuschelapp.jpg"
        )
    yield from client.send_message(message.channel, embed=embed)
    return
