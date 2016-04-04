import _util
import settings
import time

def give(fileName, user, amount):
    _util.makeBlankFile("data/"+fileName)
    if settings.divider in user.name:
        return settings.malicious
    amount = str(amount)
    with open("data/"+fileName, "r") as f:
        data = f.readlines()

    for line in data:
        if line.startswith(user.id):
            uid = line.split(settings.divider)[0]
            points = line.split(settings.divider)[1] + amount
            data[data.index(line)] = uid+settings.divider+points

            with open("data/"+fileName, "w") as f:
                f.writelines( data )
    return

#only to be called in a thread.
def tip():
    while True:
    	if time.time() % (settings.timeForPoint**60) == 0:
    		#create shekels list (they're called points in the code because it's easier to type and I keep typing SHMEKELS)
    		_util.makeBlankFile("points.txt")
    		for member in serverinfo.server(client).members:
    			#checks if user is active
    			if member.status == discord.status.online:
    				give("points.txt", msg.author, 1)
