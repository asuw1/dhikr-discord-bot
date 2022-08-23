# Dhikr Discord Bot by Abdulaziz AlSuwailim
# بوت أذكار، كتابة عبدالعزيز السويلم
# github.com/asuw1

import discord
import math
import random
import asyncio
import csv

dhikr = []

with open('dhikr.csv', encoding="utf-8", newline='') as csvfile:
    adhkar = csv.reader(csvfile, delimiter=',', quotechar='|')
    dhikr = [i for i in adhkar]
    dhikr = dhikr[0]


class Client(discord.Client):
    async def on_ready(self):
        print('Logged into discord as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return
        while True:
            await message.channel.send(dhikr[math.floor(random.random()*(len(dhikr)+1))])
            await asyncio.sleep(60)

client = Client()
client.run('API key')
