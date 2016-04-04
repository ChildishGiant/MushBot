import discord
import _util

async def run(client, msg, args):
    await client.send_message(msg.channel, "Test!")
