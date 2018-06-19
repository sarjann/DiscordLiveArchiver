import asyncio
import discord
from discordpull import store

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as ' + client.user.name + ' : ' + client.user.id)
    print('______________________________________________')

@client.event
async def on_message(message):
    print('Storing message from ' + str(message.author) + ' posted in ' + str(message.channel))
    print(message.content)
    print('______________________________________________')
    store(message.id,message.channel.id,message.channel,message.author,message.content)


client.run('REDACTED')