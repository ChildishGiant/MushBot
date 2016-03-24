
def run(client, msg, args):
    if args[1].lower() == "new":
        if len(args) != 2:
            return "Please enter a call and a response: `!newmacro example https://i.imgflip.com/11cpfs.jpg`"
        elif args[1].endswith(".jpg" or ".png"):
            # download and store.

        else:
            return "Make sure the response is a png or jpg: `!newmacro example https://i.imgflip.com/11cpfs.jpg`"
    else:
        #find and return macro
