import discord
import asyncio
client = discord.Client()




@client.event
async def on_message(message):
        embed = discord.Embed(
            title="Hallo World",
            color=0xe67e22,
            description="guten tag welt adjkhfg iadsfgjkadsh gjkahdfbg adfg\n"
                        "yhuasdghasd\n"
                        "guten\n"
                        "tag"
        )
        embed.set_author(
            name="Bobo",
            icon_url="https://cdn.pixabay.com/photo/2017/05/16/21/24/gorilla-2318998_960_720.jpg",
            url="http://grewoss.com/"
        )
        embed.add_field(
            name="Title 2",
            value="Description 2\n"
                  "fgasdfujhkasfdgk adfg da\n"
                  "asdgufhadsfjgkhads\n"
                  "afsdgadifghahdioufg\n",
            inline=False
        )
        embed.add_field(
            name="haladfgad",
            value="asdgasdfg",
            inline=False
        )
        embed.add_field(
            name="asdggasdfgadfhg",
            value="adfiohgjadfi giuhadf gadjkfhg2222",
            inline=False
        )
        embed.set_footer(
            text="Ein bot von mir",
            icon_url="https://cdn.pixabay.com/photo/2017/05/16/21/24/gorilla-2318998_960_720.jpg"
        )
        embed.set_thumbnail(
            url="https://cdn.pixabay.com/photo/2017/05/16/21/24/gorilla-2318998_960_720.jpg"
        )

        await client.send_message(message.channel, embed=embed)
