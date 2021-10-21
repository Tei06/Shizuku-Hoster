import requests
import discord
from discord.ext import commands
import json
import pymongo
import random

mongo_url = "mongodb+srv://Tei:12345CATRPG@cluster0.cjmtd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
cluster = pymongo.MongoClient(mongo_url)
db = cluster["CatRPG"]
collection = db['GeneralDB']

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def last_replace(s, old, new):
    li = s.rsplit(old, 1)
    return new.join(li)
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
def text_to_owo(text):
    """ Converts your text to OwO """
    smileys = [';;w;;', '^w^', '>w<', 'UwU', '(・`ω\´・)', '(´・ω・\`)']

    text = text.replace('L', 'W').replace('l', 'w')
    text = text.replace('R', 'W').replace('r', 'w')

    text = last_replace(text, '!', '! {}'.format(random.choice(smileys)))
    text = last_replace(text, '?', '? owo')
    text = last_replace(text, '.', '. {}'.format(random.choice(smileys)))

    for v in vowels:
        if 'n{}'.format(v) in text:
            text = text.replace('n{}'.format(v), 'ny{}'.format(v))
        if 'N{}'.format(v) in text:
            text = text.replace('N{}'.format(v), 'N{}{}'.format(
                'Y' if v.isupper() else 'y', v))

    return text

async def check_status(user):
    status = collection.find_one({'_id':user.id})
    print(status)