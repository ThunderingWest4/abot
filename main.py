import json
import discord

with open('secrets.json') as f:
    secrets = json.load(f)

client = discord.Client()

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(msg):
    if msg.content.startswith('$ping'):
        await msg.channel.send('pong')
    elif msg.content.lower().startswith('based'):
        await msg.channel.send(f"> {msg.content} \nbased? based on what")


client.run(secrets['token'])