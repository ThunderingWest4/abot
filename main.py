import json
import discord
from datetime import datetime
import random

with open('secrets.json') as f:
    secrets = json.load(f)

client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user} at time {datetime.now()}")

@client.event
async def on_message(msg):
    cont = msg.content.lower()
    cont = cont.translate(str.maketrans('', '', "!#$%^&()?[]{}\\/.,"))
    cont = cont.replace("\n", "\n>")

    if msg.content.startswith('$ping'):
        await msg.channel.send('pong')
    elif "@everyone" in cont or "@here" in cont:
        await msg.channel.send("hah you thought")
    elif ('based' in cont.split(" ")) and not ('based on ' in cont) and not ('based in ' in cont) and not ('based upon ' in cont) and not ('based off' in cont):
        options = ["based? based on what?", "more like BASED on deez nuts"]
        probs = [0.75, 0.25]
        addition = random.choices(options, weights=probs, k=1)[0]
        await msg.channel.send(f"> {msg.content} \n{addition}")


client.run(secrets['token'])