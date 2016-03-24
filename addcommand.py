import os
import settings
import _util

async def run(client, msg, args):
    _util.makeBlankFile("ascii.txt")
    if "|DIVIDER|" not in msg.content:
        if len(args) > 2:
            call = args[0]
            response = " ".join(args[1:])
            with open("ascii.txt", "ab") as a:
                a.write((call+"|DIVIDER|"+response+os.linesep).encode('utf-8'))
                await client.send_message(msg.channel, "Added command:`"+settings.activator+call+"`")
        else:
            await client.send_message(msg.channel, "Example: `!addcommand lenny ( ͡° ͜ʖ ͡°)`")
    else:
        #if they're trying to break it.
        await client.send_message(msg.channel, settings.malicous)
