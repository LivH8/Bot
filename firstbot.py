import discord
import os
import requests
import json
import random

client = discord.Client()

sad_words = ['sad', 'depressed', 'depressing', 'depression', 'unhappy', 'miserable', 'angry', 'boring', 'kill', 'loath myself', 'loathe myself', 'perturbed', 'weep', 'hate',
 'toaster bath', 'agony', 'despair', 'fear', 'fearing', 'suffer', 'suffering', 'contempt']

joneswords = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

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

"""
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
client = MyClient()
"""

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

    '''
    if 'bot' in msg:
        await message.channel.send("I am watching you!")

    if 'hello, it' in msg:
        await message.channel.send("Have you tried turning it off and on again?")

    if 'dog' in msg:
        await message.channel.send("kitten***")
    ''' 

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragement))
    '''
    if any(word in msg for word in joneswords):
        if message.author.id == 446780461084311572: #currently nedz not jones
            await message.channel.send('Woof Woof 🐶')
    '''

    if message.content.startswith('!commands'):
        commands = ['!hello', '!reply', '!inspire', '!role']
        com_message = ''
        for i in range(len(commands)):
            com_message = com_message + commands[i] + '\n'
        await message.channel.send(com_message)

    if '!addrole' in msg:
        userid = str(message.author.id)
        if userid == '357621946709442561':
            await message.channel.send("Confirm?")
            user = message.author
            role = discord.utils.get(user.guild.roles, name="Mapcore")
            await user.add_roles(role)
        else:
            await message.channel.send("Permission denied.")

    if '!embed' in msg:
        userid = str(message.author.id)
        if userid == '357621946709442561':
            reactionEmbed = discord.Embed(title="Role Selection", description="React with emojis to add roles", colour=0x87CEEB)
            reactionEmbed.add_field(name="To add Mapcore role:", value="🤡", inline=False)
            reactionEmbed.add_field(name="To add Test role:", value="🎇", inline=True)
            reactionEmbed.add_field(name="To add Test2 role:", value="👺", inline=True)
            confirm = await message.channel.send(embed=reactionEmbed)
            await confirm.add_reaction('🤡')
            await confirm.add_reaction('🎇')
            await confirm.add_reaction('👺')
        else:
            await message.channel.send("Permission denied.")

    if '!role' in msg:
        userid = str(message.author.id)
        if userid == '357621946709442561':
            reactionEmbed = discord.Embed(title="Role Selection", description="React with emojis to add roles", colour=0x87CEEB)
            reactionEmbed.add_field(name="To add Mapcore role:", value="🤡", inline=False)
            reactionEmbed.add_field(name="To add Test role:", value="🎇", inline=False)
            reactionEmbed.add_field(name="To add Test2 role:", value="👺", inline=False)
            confirm = await message.channel.send(embed=reactionEmbed)
            await confirm.add_reaction('🤡')
            await confirm.add_reaction('🎇')
            await confirm.add_reaction('👺')
            print(confirm.id)

            f = open("confirmid.txt", "w")
            f.write(str(confirm.id))
            f.close()
        else:
            await message.channel.send("Permission denied.")


@client.event
async def on_reaction_add(reaction, user):
    if user != client.user:
        f = open("confirmid.txt", "r")

        fileread = str(f.read())
        reactionread = str(reaction.message.id)

        if (fileread == reactionread) and str(reaction.emoji) == "🤡":
            role = discord.utils.get(user.guild.roles, name="Mapcore")
            await user.add_roles(role)
            print(reaction)
            print(user)
        if (fileread == reactionread) and str(reaction.emoji) == "🎇":
            role = discord.utils.get(user.guild.roles, name="Test")
            await user.add_roles(role)
            print(reaction)
            print(user)
        if (fileread == reactionread) and str(reaction.emoji) == "👺":
            role = discord.utils.get(user.guild.roles, name="Test2")
            await user.add_roles(role)
            print(reaction)
            print(user)


#token
token_file = open("token.txt")
token = token_file.read()
client.run(token)

"""
hi :0
"""