import os.path
import cleverbot
from urllib import request as requests

cb1 = cleverbot.Cleverbot()

def getServerByName(client, n):
    for server in client.servers:
        if server.name == n:
            return server

def ask(q):
	return cb1.ask(q)

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
