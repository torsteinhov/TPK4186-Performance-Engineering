'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''

class Operation:

    def __init__(self, machine, duration, start=None, stop=None):
        self.machine = machine
        self.duration = duration
        self.start = start
        self.stop = stop
    
    def getDuration(self):
        return self.duration
    
    def setDuration(self, duration):
        self.duration = duration
    
    def getMachine(self):
        return self.machine
    
    def setMachine(self, machine):
        self.machine = machine
    
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
    
    