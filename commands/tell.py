import discord
import random
perm = 3

def ex(args, message, client, invoke):
    args = message.content.split
    if args(" ")[1:]:
        #name = str(args()[2:3])[2:-2]



        try:

            pwort = open("/home/pi/Desktop/bots/discord_botv2.4/commands/tell/begrüßung.txt", "a")
            pwort.write(str(args()[1:2])[1:-1]+", ")
            pwort.close()

            #PWORT = []
            PWORT = open("/home/pi/Desktop/bots/discord_botv2.4/commands/tell/begrüßung.txt", "r")




            print("1. "+PWORT.readline())

            liste = ["test"]
            liste.append("hi")
            print("2. "+liste)


            '''
            print("2. "+list(PWORT.readline()))

            antwort = list(PWORT.readline())
            print("3. "+random.choice(antwort))
            '''

            #
            #yield from client.send_message(message.channel, )
            PWORT.close()
        except:

            yield from client.send_message(message.channel, "nope")
            pass
