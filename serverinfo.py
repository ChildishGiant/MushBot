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
        if (modRole(client) or adminRole(client)) in member.roles:
            l.append(member)
    return l

def adminList(client):
    l = []
    for member in server(client).members:
        if adminRole(client) in member.roles:
            l.append(member)
    return l

def codererList(client):
    l = []
    for member in server(client).members:
        if codererRole(client) in member.roles:
            l.append(member)
    return l
