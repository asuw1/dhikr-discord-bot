# Dhikr Discord Bot by Abdulaziz AlSuwailim
# بوت أذكار، كتابة عبدالعزيز السويلم
# github.com/asuw1

import discord
import math
import random
import asyncio
import csv

# List that will hold the adhkar from the csv file
dhikr = []

# Opening the csv file that holds the adhkar
with open('dhikr.csv', encoding="utf-8", newline='') as csvfile: # the file can be changed here in the first argument with dhikr.csv or dhikr_tr.csv or dhikr_trlit.csv
    adhkar = csv.reader(csvfile, delimiter=',', quotechar='|')
    dhikr = [i for i in adhkar]
    dhikr = dhikr[0]

# Discord client class initialization
class Client(discord.Client):
    async def on_ready(self):
        print('Logged into discord as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return
        while True:
            await message.channel.send(dhikr[math.floor(random.random()*(len(dhikr)))]) # Sending a random dhikr from the file
            await asyncio.sleep(60)

client = Client()
client.run('API key') # Enter your discord developer API key
