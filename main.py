import os
import discord
import requests
import json

client = discord.Client()
key = 'K8kPDUS8O3RknkpNyBCT'
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def get_stats(username):
  if username == '':
    return 'Please resend your command with your username at the end.\ni.e. $AL stats CheeseTerds'
  response = requests.get("https://api.mozambiquehe.re/bridge?version=5&platform=PC&player="+ username +"&auth=K8kPDUS8O3RknkpNyBCT")
  json_data = json.loads(response.text) #use json_data to access api's dictionaries
  stats = "Name: " + json_data['global']['name'] + "\nRank: " + json_data['global']['rank']['rankName'] + "\n" + json_data['global']['rank']['rankImg']
  return stats

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$AL test'):
    await message.channel.send('Hi! This is the AL Test Bot.')

  if message.content.startswith('$AL help'):
    await message.channel.send(
      'This is the AL Test Bot. All commands use prefix *"$AL"*.\
      This bot uses the ')

  if message.content.startswith('$AL quote'):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content.startswith('$AL stats'):
    username = message.content
    username = username.split('$AL stats ')   #saves message content to string 
    stats = get_stats(username[1])
    await message.channel.send(stats)

client.run(os.environ['TOKEN'])