import json
import discord
from datetime import datetime
import string

with open('secrets.json') as f:
    secrets = json.load(f)

client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user} at time {datetime.now()}")

@client.event
async def on_message(msg):
    cont = msg.content.lower()
    cont = cont.translate(str.maketrans('', '', string.punctuation))
    if msg.content.startswith('$ping'):
        await msg.channel.send('pong')
    elif ('based' in cont.split(" ")) and not ('based on' in cont):
        await msg.channel.send(f"> {msg.content} \nbased? based on what")


client.run(secrets['token'])