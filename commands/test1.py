import discord
from discord.ext import commands
import asyncio
client = discord.Client()
import time

def ex(args, message, ctx, member : discord.Member, *, reason=None):
    yield from member.kick(reason=reason)






#from selenium import webdriver
#chromedriver = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe"
#browser = webdriver.Chrome(chromedriver)
#
#browser.get('http://seleniumhq.org/')




#import selenium.webdriver as webdriver
#
#def get_results(search_term):
#    url = "https://www.startpage.com"
#    browser = webdriver.Chrome('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chromedriver.exe')
#    browser.get(url)
#    search_box = browser.find_element_by_id("query")
#    search_box.send_keys(search_term)
#    search_box.submit()
#    try:
#        links = browser.find_element_by_xpath("//ol@class='web_regular_results']//h3//a")
#    except:
#        links = browser.find_element_by_xpath("//h3//a")
#    results = []
#    for link in links:
#        href = link.get_attribute("href")
#        print(href)
#        results.append(href)
#    browser.close()
#    return results
#get_results("test")
