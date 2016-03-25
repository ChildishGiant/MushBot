import os.path
from urllib import request as requests

def getServerByName(client, n):
    for server in client.servers:
        if server.name == n:
            return server

def makeBlankFile(filename):
    #checks to see if file exists
    if os.path.isfile(filename):
        return None
    else:
        #make file
        open(filename, 'a').close()

def getResponseCode(url):
    conn = urllib.requests.urlopen(url)
    return conn.getcode()
