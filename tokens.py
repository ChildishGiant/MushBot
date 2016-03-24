def giveToken(dictName,user, token):
    dictName[user] = token
    return dictName

def takeToken(dictName, user):
    if dictName[user]:
        del dictName[user]
    else:
        return None

def checkToken(dictName, user):
    try:
        if dictName[user]:
            return True
    except KeyError:
        return False
