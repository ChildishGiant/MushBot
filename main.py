from asyncio import async
from urllib import request as requests
from imp import reload
import discord
import urllib
import _util
import os
import time
import json
import emote
import tokens
import serverinfo
import threading
import settings
import points

#create the client object, set cache_auth
client = discord.Client(cache_auth=False)

#create naughtyList
naughtyList = {}

with open('email.txt', 'r') as f:
	email = f.read()

with open('password.txt', 'r') as f:
	password = f.read()

r = requests.urlopen("http://twitchemotes.com/api_cache/v2/global.json")
emotes = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))

while True:
	if time.time() %% (settings.timeForPoint**60) == 0:
		#create shekels list (they're called points in the code because it's easier to type and I keep typing SHMEKELS)
		_util.makeBlankFile("points.txt")
		for member in serverinfo.server(client).members
			#checks if user is active
			if member.status == discord.status.online:
				points.give("points.txt", msg.author, 1)

#on_message event, triggers anytime a message is received on a channel the client can see
#msg - the object representing the message received
@client.event
async def on_message(msg):
	global naughtyList
	if msg.author == client.user:
		return

	if not msg.channel.is_private:

		if msg.content in emotes["emotes"]:
			em = emote.emote(msg)
			await client.send_message(em[0], em[1])
			await client.send_file(em[0], em[2])

		#logging messages
		ts = msg.timestamp
		targetfile = "logs/{}{}{}/{}.txt".format(ts.year,ts.month,ts.day,msg.channel.name)
		#message format is [hh:mm] auhor - (id): message
		formattedline = "[{}:{}] {} - ({}): ".format(ts.hour, ts.minute, msg.author.name, msg.author.id)
		if len(msg.attachments) > 0:
			embedslinks = ""
			for embed in msg.attachments:
				embedslinks += "attachment({}) ".format(embed['url'])
			formattedline += embedslinks
		else:
			formattedline += msg.content
		#create a folder for the day if there isn't already one
		if not os.path.isdir("logs/{}{}{}".format(ts.year,ts.month,ts.day)):
			os.mkdir("logs/{}{}{}".format(ts.year,ts.month,ts.day))
		#use UTF-8 encoding to handle non-ascii names
		with open(targetfile, "ab") as f:
			f.write((formattedline+"\n").encode('utf-8'))

		#Checks if the user is on cooldown
		if not tokens.checkToken(naughtyList,msg.author):

			#Check for all text commands
			_util.makeBlankFile("ascii.txt")
			lines = open("ascii.txt", 'rb').read().decode("utf-8").split(os.linesep)
			for line in lines:
				if line == "":
					break
				meme = line.split("|DIVIDER|")
				if meme[0] in msg.content.lower():
					await client.send_message(msg.channel, meme[1])

			#command handleing
			if msg.content.startswith(settings.activator):

				#command cooldown for those not worthy enough.
				if msg.author not in (serverinfo.modList(client) or serverinfo.codererList()):
					tokens.giveToken(naughtyList,msg.author, True)
					threading.Timer(settings.commandCooldownTime,tokens.takeToken(naughtyList,msg.author))

				#command is the first word in the message
				args = msg.content.split()
				cmd = args[0]

				#check for a corresponding .py file
				if os.path.isfile(cmd.replace('!','')+'.py'):

					#Get the appropriate module name for the command. Caps matter, so all lower case
					module = cmd.replace('!','').lower()

					#dynamically import the module required, then refresh it to make sure we're running the newest possible code
					command = __import__(module)
					reload(command)

					#actually run the command, command.py file must have a run() method that takes these 4 arguments
					try:
						await command.run(client, msg, args[1:])
					#catching errors due to files not having a run()
					except NameError:
						await client.send_message(msg.channel, settings.invalidCommand)
				else:
					#no command.py file, instead check for a matching image file in the images folder and upload it.
					if '.' in args[0] or '/' in args[0]: #no sketchy folder tricks.
						return

					imagefile = 'images/'+args[0].replace('!','')

					if os.path.isfile(imagefile+'.jpg'):
						await client.send_file(c, imagefile+'.jpg')

					if os.path.isfile(imagefile+'.png'):
						await client.send_file(c, imagefile+'.png')

					if os.path.isfile(imagefile+'.gif'):
						await client.send_file(c, imagefile+'.gif')

#on_ready event, triggers once the client is logged in and ready.
@client.event
async def on_ready():
	print("Client is running as {}".format(client.user.name))

print("Starting bot...")
client.run(email, password)
