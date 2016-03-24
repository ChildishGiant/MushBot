from urllib import request as urlrequests
import os
import json
import requests
import shutil

#get a list of all global emotes
r = urlrequests.urlopen("http://twitchemotes.com/api_cache/v2/global.json")
emotes = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))


def emote(msg):
    em = msg.content
    r = requests.get("http://static-cdn.jtvnw.net/emoticons/v1/" + str(emotes["emotes"][em]["image_id"]) + "/1.0", stream=True)
    if r.status_code == 200:
        if not os.path.isfile("emotes/"+em+".png"):
            with open("emotes/"+em+".png", 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
        return msg.channel, msg.author.mention, "emotes/" + em + ".png"
    else:
        print("Emote " + em + " returned status code " + r.status_code)
