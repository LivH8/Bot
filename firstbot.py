import discord
import os
import requests
import json
import random

client = discord.Client()

sad_words = ['sad', 'depressed', 'depressing', 'depression', 'unhappy', 'miserable', 'angry', 'boring', 'kill', 'loath myself', 'loathe myself', 'perturbed', 'weep', 'hate',
 'toaster bath', 'agony', 'despair', 'fear', 'fearing', 'suffer', 'suffering']

starter_encouragement = [
    'Cheer up!',
    'Hang in there.',
    'You are a great person.',
    'Tomorrow is another day.',
    'Turn that frown upside down!',
]

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#class MyClient(discord.Client):
#    async def on_ready(self):
#        print('Logged on as {0}!'.format(self.user))
#    async def on_message(self, message):
#        print('Message from {0.author}: {0.content}'.format(message))
#client = MyClient()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!reply'):
        print (message)
        await message.channel.send('Hello World! 👍')

    if message.content.startswith('!inspire'):
            quote = get_quote()
            await message.channel.send(quote)

    if 'bot' in msg:
        await message.channel.send("I am watching you!")

    if 'hello, it' in msg:
        await message.channel.send("Have you tried turning it off and on again?")

    if 'dog' in msg:
        await message.channel.send("kitten***")

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragement))

#jones speak
#@client.event
#async def on_message(message):
#     if message.author.id == 244214874324860929 and ' ' in message.content.lower():
#        await message.channel.send('Woof Woof 🐶')

#token
token_file = open("token.txt")
token = token_file.read()
client.run(token)