import settings
import _util
import shutil
errorMessage = "Please enter a call and a response: `!macro example https://i.imgflip.com/11cpfs.jpg`"


def run(client, msg, args):
    filename = str(args[0].lower())
    url = str(args[1].lower())

    if ('.'or '/') in args[0]:
        return settings.malicious

    if os.path.isfile("images/"+filename + ".png"):
        return "That file already exists, try `{0}`".format(filename + ".png")

    elif os.path.isfile("images/"+filename + ".jpg"):
        return "That file already exists, try `{0}`".format(filename + ".jpg")

    elif os.path.isfile("images/"+filename + ".gif"):
        return "That file already exists, try `{0}`".format(filename + ".gif")

    elif _util.getResponseCode(url) != 200:
        return "Looks like that's not a valid image url."

    elif url.endswith(".jpg" or ".png" or ".gif"):
                r = requests.get(, stream=True)
                with open("images/"+filename+url[len(url)-4:], 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
                return msg.channel, filename+url[len(url)-4:]
    elif len(args) != 2:
        return errorMessage
    else:
        return "To use an image macro type the name of the image."
