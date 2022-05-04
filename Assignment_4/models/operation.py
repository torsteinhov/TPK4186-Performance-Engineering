'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''

class Operation:

    def __init__(self, id, duration, start=None, stop=None):
        self.id = id
        self.duration = duration
        self.start = start
        self.stop = stop
    
    def getDuration(self):
        return self.duration
    
    def setDuration(self, duration):
        self.duration = duration
    
    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id
    
    def getStart(self):
        return self.start
    
    def setStart(self, start):
        self.start = start
    
    def getStop(self):
        return self.stop
    
    def setStop(self, stop):
        self.stop = stop
    
    def checkStartStop(self):
        if (self.getStart() + self.getDuration()) == self.getStop() and (self.getStop() - self.getDuration()) == self.getStart():
            return True
        else:
            return False
    
    