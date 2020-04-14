import discord
import asyncio
client = discord.Client()
from commands import STATICS
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

@asyncio.coroutine
def ex(args, message, client, invoke):
    if message.content[8:]:

        search = message.content[8:]
        driver = webdriver.Firefox('/usr/local/bin/geckodriver')
        #driver = webdriver.Chromium()
        url = "http://www.google.com"
        driver.get(url)
        inputElement = driver.find_element_by_name("q")
        inputElement.send_keys(search)
        inputElement.submit()
        try:
            #resultsstats = driver.find_element_by_id().text
            #resultsstats = driver.find_element_by_id("resultStats").text

            #q = driver.find_element_by_id("search").text #res reo

            time.sleep(5)
            #listl = driver.find_elements_by_class_name("iUh30 bc") #links
            lists = driver.find_elements_by_class_name("LC20lb")
            yield from client.send_message(message.channel, "Found "+str(len(lists))+" searches:")
            i = 0
            for listiems in lists:
                yield from client.send_message(message.channel,listiems.text)


                i += 1
                if(i > 4):
                    driver.close()
                    break

                    #p = re.findall(r'<h3>()</h3>', str(q))
                    #print(q)
                    #print(resultsstats)
        except:
            yield from client.send_message(message.channel, "Es gibt einen fehler!")
            time.sleep(5)
            driver.close()
    else:
        embed = discord.Embed(
            title="Commands",
            color=600,  # blue
            description="~search (suche mit 4 Ergebnisse)"
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
        driver.close()
