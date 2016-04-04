import discord
import _util

async def run(client, msg, args):
	if ((msg.author in serverinfo.modList(client)) or (msg.author in serverinfo.codererList(client))):
		c = discord.Colour(int(args[1], 16))
		for r in ch.server.roles:
			if r.name.startswith(args[0]):
				await client.edit_role(ch.server, r, colour=c)
				await client.send_message(ch, "Set color for {} to {}".format(r.name,args[1]))
