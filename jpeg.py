import discord
import _util
from PIL import Image
import urllib
from PIL import ImageFilter
import requests
import shutil
import random

async def run(client, msg, args):
    #jpeg quality
    qual = 5
    #how many times to distort random chunks
    passes = random.randint(0,100)
    if len(args) > 1:
        qual = int(args[1])
	if len(args) > 2:
        passes = int(args[2])

    #make sure the link is actually a link to an image
    if not (args[0].startswith('http') and ('.jpg' in args[0].lower() or '.jpeg' in args[0].lower() or '.png' in args[0].lower()):
        await client.send_message(msg.channel, "That link doesn't look quite right!")
        return

    filename = args[0].split('/')[-1]
	r = requests.get(args[0], stream=True)
    if r.status_code == 200:
        with open("images/"+filename, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
