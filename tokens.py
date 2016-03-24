def giveToken(dictName,user, token):
    global dictName
    if not dictName:
        return None
    else:
        dictName[user] = token


def takeToken(dictName, user):
    global dictName
    if dictName[user]:
        del dict[user]
    else:
        return None

def checkToken(dictName, user):
    global dictName
    try:
        if dictName[user]:
            return True
    except KeyError:
        return False
