from asyncio import async
import discord
from urllib import request as requests
import emote
import os

#create the client object, set cache_auth 
client = discord.Client(cache_auth=False)

with open('email.txt', 'r') as f:
	email = f.read()

with open('password.txt', 'r') as f:
	password = f.read()
	
#on_message event, triggers anytime a message is received on a channel the client can see
#msg - the object representing the message received
@client.event
async def on_message(msg):
	if msg.author == client.user:
		return

	if not msg.channel.is_private:

		if "lenny" in msg.content.lower():
			client.send_message(msg.channel, "( ͡° ͜ʖ ͡°)")

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
		if not os.path.isdir("{}{}{}".format(ts.year,ts.month,ts.day)):
			os.mkdir("{}{}{}".format(ts.year,ts.month,ts.day))
		#use UTF-8 encoding to handle non-ascii names
		with open(targetfile, "ab") as f:
			f.write((formattedline+"\n").encode('utf-8'))
		
		#command handling
		if msg.startswith('!'):
			args = msg.split()
			#command is the first word in the message
			command = args[0]
			
			#check for a corresponding .py file
			if os.path.isfile(command.replace('!','')+'.py'):
			
				#Get the appropriate module name for the command. Caps matter, so all lower case
				module = command.replace('!','').lower()
				
				#dynamically import the module required, then refresh it to make sure we're running the newest possible code
				command = __import__(module)
				reload(command)
				
				#actually run the command, command.py file must have a run() method that takes these 4 arguments
				await command.run(client, msg.channel, msg.author, args[1:])
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