def giveToken(dictName,user, token):
    if not dictName:
        return None
    else:
        dictName[user] = token


def takeToken(dictName,user):
    if dictName[user]:
        del dict[user]
    else:
        return None
