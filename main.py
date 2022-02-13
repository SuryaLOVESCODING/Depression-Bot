import discord
import os
import requests
import json
import random
from replit import db
import youtube_dl
from discord.ext import commands
from  neuralintents import GenericAssistant
from dotenv import load_dotenv

chatbot=GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()


load_dotenv()
client = discord.Client()
#This will say you in the shell when the bot is ready. This code is optional
@client.event
async def on_ready():
    print("Bot is ready!")




#Put your token he










sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person"
]

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragment(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if(msg.startswith('$Helpers')):
    await message.channel.send("https://fherehab.com/mental-health-lp/?lkw=depression%20treatment&utm_source=google+cpc&utm_medium=cpc&utm_campaign=Google+FHE-MH&lag=Google+FHE-MH+Depression&lmt=p&las=1&invsrc=455307&gclid=CjwKCAiAxJSPBhAoEiwAeO_fP7SIYGkd1tZxoOk3eamG_fjiOwn15yNy8et_6y58VuEoujNrDVih-BoCD8AQAvD_BwE")

  if(msg.startswith('@DepressionBot')):
    response=chatbot.request(msg[7:])
    await message.channel.send(response)


  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith("$new"):
    encouraging_message = msg.split("$new ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")

  if msg.startswith("$del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del",1)[1])
      delete_encouragment(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  



 

  # Test command
  if msg.startswith('$meme'):
      number=random.randint(1,10)
      if(number==1):
        await message.channel.send(file=discord.File('Discord-Bot-Tutorial-Series-Episode-4/src/mouse.mp4'))
      if(number==2):
        await message.channel.send(file=discord.File('Discord-Bot-Tutorial-Series-Episode-4/src/spiderman.mp4'))

      if(number==3):
        await message.channel.send(file=discord.File('Discord-Bot-Tutorial-Series-Episode-4/src/dog.mp4'))
      if(number==4):
        await message.channel.send(file=discord.File('Discord-Bot-Tutorial-Series-Episode-4/src/pig.mp4'))

      if(number==5):
        await message.channel.send(file=discord.File('Discord-Bot-Tutorial-Series-Episode-4/src/skeleton.mp4'))


      if(number==6):
        await message.channel.send(file=discord.File('Discord-Bot-Tutorial-Series-Episode-4/src/baby.mp4'))

      if(number==7):
        await message.channel.send(file=discord.File('Discord-Bot-Tutorial-Series-Episode-4/src/cat.mp4'))

      if(number==8):
        await message.channel.send(file=discord.File('Discord-Bot-Tutorial-Series-Episode-4/src/cops.mp4'))
      if(number==9):
          await message.channel.send(file=discord.File('Discord-Bot-Tutorial-Series-Episode-4/src/swag.mp4'))

      
      if(number==10):
          await message.channel.send(file=discord.File('Discord-Bot-Tutorial-Series-Episode-4/src/minion.mp4'))   
      
  if msg.startswith('$song'):
      number=random.randint(1,10)
      if(number==1):
        await message.channel.send(file=discord.File('Discord-Bot-Tutorial-Series-Episode-4/src/song1.mp3'))
      if(number==2):
        await message.channel.send(file=discord.File('Discord-Bot-Tutorial-Series-Episode-4/src/song2.mp3'))

      if(number==3):
        await message.channel.send(file=discord.File('Discord-Bot-Tutorial-Series-Episode-4/src/song3.mp3'))
      if(number==4):
        await message.channel.send(file=discord.File('Discord-Bot-Tutorial-Series-Episode-4/src/song4.mp3'))

      if(number==5):
        await message.channel.send(file=discord.File('Discord-Bot-Tutorial-Series-Episode-4/src/song5.mp3'))


      if(number==6):
        await message.channel.send(file=discord.File('Discord-Bot-Tutorial-Series-Episode-4/src/song6.mp3'))

      if(number==7):
        await message.channel.send(file=discord.File('Discord-Bot-Tutorial-Series-Episode-4/src/song7.mp3'))

      if(number==8):
        await message.channel.send(file=discord.File('Discord-Bot-Tutorial-Series-Episode-4/src/song8.mp3'))
      if(number==9):
          await message.channel.send(file=discord.File('Discord-Bot-Tutorial-Series-Episode-4/src/song9.mp3'))
      if(number==10):
          await message.channel.send(file=discord.File('Discord-Bot-Tutorial-Series-Episode-4/src/song10.mp3'))
  
  if msg.startswith('$breathing'):
    await message.channel.send(file=discord.File('breath.png'))

    await message.channel.send("Check how long you inhale and exhale with this stopwatch")

    await message.channel.send("https://portfolio.suryanachiappan.repl.co/")
  
  if msg.startswith('$info'):
    await message.channel.send("Anxiety is a feeling of fear, dread, and uneasiness. It might cause you to sweat, feel restless and tense, and have a rapid heartbeat. It can be a normal reaction to stress. For example, you might feel anxious when faced with a difficult problem at work, before taking a test, or before making an important decision.")
  


    

 





client.run(os.getenv('SECRET'))
#bot.run(os.getenv('SECRET'))









