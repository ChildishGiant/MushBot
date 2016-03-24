import os
import settings

def run(client, msg, args):
    #checks to see if ascii.txt exists
    if os.path.isfile("ascii.txt"):
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
    else:
        #make ascii.txt
        open("ascii.txt", 'a').close()
