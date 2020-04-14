import discord
import asyncio
client = discord.Client()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

@asyncio.coroutine
def ex(args, message, client, invoke):
    if message.content[5:]:
        search = message.content[5:]
        driver = webdriver.Firefox()
        url = "https://euw.op.gg/summoner/userName="
        driver.get(url)
        inputElement = driver.find_element_by_name("userName")
        inputElement.send_keys(search)
        inputElement.submit()
        print(search)
        time.sleep(5)
        try:
            print("1")

        except Exception:
                #not exist
            embed = discord.Embed(
                    color=712,#
                    description="Player not exist"
                    )
            embed.set_author(
                name="League of Legends",
                icon_url="http://www.macupdate.com/images/icons256/47210.png",
                url="https://euw.leagueoflegends.com/de/"
                )
            embed.set_footer(
                text="Ein bot von Brainkackwitz"
                )

            yield from client.send_message(message.channel, embed=embed)
        else:
            ico = driver.find_element_by_xpath("//img[@class='ProfileImage']").get_attribute("src")


        try:
            #normal
            ico = driver.find_element_by_xpath("//img[@class='ProfileImage']").get_attribute("src")
            #lvl = driver.find_element_by_xpath("//span[@class='Level tip tpd-delegation-uid-1']").text
            elo = str(driver.find_element_by_class_name("TierRank").text)
            lp = str(driver.find_element_by_class_name("LeaguePoints").text)
            winr = str(driver.find_element_by_class_name("winratio").text)
            embed = discord.Embed(
                    color=712,
                    description="Player "+search+"\n"+elo+"\n"+lp+"\n"+winr
                    )
            embed.set_author(
                name="League of Legends",
                icon_url="http://www.macupdate.com/images/icons256/47210.png",
                url="https://euw.leagueoflegends.com/de/"
                )
            embed.set_footer(
                text="Ein bot von Brainkackwitz"
                )
            embed.set_thumbnail(
                url=ico
                )
            yield from client.send_message(message.channel, embed=embed)

        except:
            ico = driver.find_element_by_xpath("//img[@class='ProfileImage']").get_attribute("src")
                #lvl = driver.find_element_by_xpath("//span[@class='Level tip tpd-delegation-uid-1']").text
                #Unranked

            embed = discord.Embed(
                    color=712,#
                    description="Player "+search+"\nUnranked"
                    )
            embed.set_author(
                name="League of Legends",
                icon_url="http://www.macupdate.com/images/icons256/47210.png",
                url="https://euw.leagueoflegends.com/de/"
                )
            embed.set_footer(
                text="Ein bot von Brainkackwitz"
                )
            embed.set_thumbnail(
                url=ico
                )
            yield from client.send_message(message.channel, embed=embed)


        finally:

            driver.close()






#driver.find_element_by_xpath('//h3[@class="LC20lb" and not(contains(text(), "org")) and not(contains(text(), "wikipedia"))]').click()


        #except:
        #    yield from client.send_message(message.channel, "Es gibt einen fehler!")
        #    time.sleep(5)
        #    driver.close()









    else:
        embed = discord.Embed(
            title="Commands",
            color=600,#blue
            description="name (nur für euw)"
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
        time.sleep(5)
        webdriver.Firefox().close()
