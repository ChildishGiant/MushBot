import _util

def server(client):
    return _util.getServerByName(client,"The Binding Of Isaac")

def modRole(client):
    for role in server(client):
        if role.name == "Moderator":
            return role

def adminRole(client):
    for role in server(client):
        if role.name == "Admin":
            return role

def modList(client):
    l = []
    for member in server(client).members:
        if member.role == (modRole(client) or adminRole(client))
            l[len(l)+1] = member
    return l 

