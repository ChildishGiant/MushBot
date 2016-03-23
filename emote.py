from urllib import request as requests
import os

#get a list of all global emotes
emotes = requests.urlretrieve("http://twitchemotes.com/api_cache/v2/global.json").json()

def emote(msg):
    em = msg.content
    r = requests.urlretrieve("http://static-cdn.jtvnw.net/emoticons/v1/" + str(emotes["emotes"][em]["image_id"]) + "/1.0")
    if r.status_code == 200:
        if not os.path.isfile("emotes/" + em + ".png"):
            with open("emotes/" + em + ".png", "wb") as f:
                f.write(r.content)
        return msg.channel, "emotes/" + em + ".png"
    else:
        print("Emote " + em + " returned status code " + r.status_code)