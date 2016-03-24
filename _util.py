
def getServerByName(client, n):
    for server in client.servers:
        if server.name == n:
            return server

def makeBlankFile(filename):
    #checks to see if file exists
    if os.path.isfile(filename):
    else:
        #make file
        open(filename, 'a').close()
