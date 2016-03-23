
def getServerByName(client, n):
    for server in client.servers:
        if server.name == n:
            return server
