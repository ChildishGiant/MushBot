import cleverbot
import discord
import _util

async def run(client, msg, args):
	response = _util.ask(" ".join(args)).decode('utf-8')
	await client.send_message(msg.channel, msg.author.mention + ": "+response)

async def help():
	return "!cb [question] - Talk to cleverbot!"
