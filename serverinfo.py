import _util

def server(client):
    return _util.getServerByName(client,"The Binding of Isaac")

def modRole(client):
    for role in server(client).roles:
        if role.name == "Moderator":
            return role

def adminRole(client):
    for role in server(client).roles:
        if role.name == "Admin":
            return role

def codererRole(client):
    for role in server(client).roles:
        if role.name == "Coderer":
            return role


def modList(client):
    l = []
    for member in server(client).members:
        if member.role == (modRole(client) or adminRole(client)):
            l[len(l)+1] = member
    return l

def adminList(client):
    l = []
    for member in server(client).members:
        if member.role == adminRole(client):
            l[len(l)+1] = member
    return l

def codererList(client):
    l = []
    for member in server(client).members:
        if member.role == codererRole(client):
            l[len(l)+1] = member
    return l
