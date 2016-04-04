naughtyList = {}

def giveToken(user,token):
    global naughtyList
    naughtyList[str(user)] = token

def takeToken(user):
    global naughtyList
    if naughtyList[str(user)]:
        del naughtyList[str(user)]
    else:
        return None

def checkToken(user):
    global naughtyList
    try:
        if naughtyList[str(user)]:
            return True
    except KeyError:
        return False
