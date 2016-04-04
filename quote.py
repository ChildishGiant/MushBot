import discord
import random
import settings
import os
async def run(client, msg, args):
	l = []
	if len(args) > 0:
		with open('data/quotes.txt', 'rb') as f:
			content = f.read().decode('utf-8').split(os.linesep)
			for line in content:
				if ' - ' in line:
					if line.split(settings.divider)[1].lower().startswith(args[0].lower()):
						l.append(line)
				else:
					if '-' in line:
						if line.split(settings.divider)[1].lower().startswith(args[0].lower()):
							l.append(line)
	if len(l) < 1:
		with open('data/quotes.txt', 'rb') as f:
			l = f.read().decode('utf-8').split(os.linesep)
	quote = random.choice(l)
	await client.send_message(msg.channel, quote.replace(settings.divider, ' - '))

async def help():
	return '!quote (name) - Return a random quote or a random quote by someone whose name starts with (name) *note: (name) is optional'
