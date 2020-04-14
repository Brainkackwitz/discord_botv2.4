import discord
import asyncio
client = discord.Client()
from commands import STATICS


@asyncio.coroutine
def ex(args, message, client, invoke):
      embed = discord.Embed(
          title=STATICS.BOTNAME,
          color=0xe67e22,
          description="version: "+STATICS.description
      )
      embed.set_author(
          name=STATICS.authorname,
          icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Crown_of_Savoy.svg/1280px-Crown_of_Savoy.svg.png",
          url="https://discordapp.com/developers/applications "
      )
      embed.add_field(
          name="ID",
          value="327779958250405889",
      )
      embed.add_field(
          name="Help",
          value="?help",
          inline=False
      )
      embed.set_footer(
          text="Ein bot von Brainkackwitz"
      )
      embed.set_thumbnail(
          url="https://www.welt.de/img/kultur/mobile160730744/9152508057-ci102l-w1024/Die-Wunderbare-Reise-Des-Kleinen-Nils-Holgersson.jpg"
      )
      yield from client.send_message(message.channel, embed=embed)
