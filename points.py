import _util
import settings

def give(fileName, user, amount):
    _util.makeBlankFile(fileName)
    if settings.divider in user.name:

    amount = str(amount)
    with open(fileName, "r") as f:
        data = f.readlines()

    for line in data
        if line.startswith(user.id):
            uid = line.split(settings.divider)[0]
            points = line.split(settings.divider)[1] + amount
            data[data.index(line)] = uid+settings.divider+points

            with open(fileName, "w") as f:
                f.writelines( data )
    return
