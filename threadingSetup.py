#Taken from http://www.tutorialspoint.com/python/python_multithreading.htm
#We're using threading not thread. Deal with it.
import threading
import time

exitFlag = 0

class newThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting " + self.name)
    def runFunction(function, args):
        run(self)
        function(args)
