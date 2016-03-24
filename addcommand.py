import os
import settings
import _util

def run(client, msg, args):
    _util.makeBlankFile("ascii.txt")
    if "|DIVIDER|" not in msg.content:
        if len(args) == "2":
            call = args[0]
            response = args[1]
            with open("ascii.txt", "") as a
                a.write(call+"|DIVIDER|"+response+os.linesep)
                return "Added command:`"+settings.activator+call+"`"
        else:
            return "Example: `!addcommand lenny ( ͡° ͜ʖ ͡°)`"
    else:
        #if they're trying to break it.
        return settings.malicous
