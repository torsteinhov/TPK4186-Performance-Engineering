'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''

class Operation:

    '''
    A class used to represent an operation
    ...
    
    Attributes
    ----------
    machine : machine object
        a machine object
    duration: int 
        an integer representing the duration of the operation   
    uncertainDuration: 
        float with duration time from the triangular distrubution 
    start: int
        an integer with the start time of the operation
    stop: int
        an integer with the stop time of the operation
    jobId: int
        an integer with the job's id
    
    
    

    Methods
    -------

    getDuration()
        gets the operations' duration
    getUncertainDuration()
        LARS SKRIV HER
    getMachine()
        get the machine used in the operation
    getStart()
        get the start time
    getStop()
        get the stop time
    checkStartStop(operations)
        checks if the start time plus duration gives stop time. True if it does, otherwise false
    setDuration(duration)
        sets the duration
    setUncertainDuration(uncertainDuration)
        LARS SKRIV HER
    setMachine(machine)
        sets the machine to be used
    setStart(start)
        sets the start time
    setStop(stop)
        sets the stop time

    '''

    def __init__(self, machine, duration, uncertainDuration=None, start=None, stop=None, jobId=None):
        self.machine = machine
        self.duration = duration
        self.uncertainDuration = uncertainDuration
        self.start = start
        self.stop = stop
        self.jobId = jobId
    
    def getDuration(self):
        return self.duration
    
    def setDuration(self, duration):
        self.duration = duration

    def getUncertainDuration(self):
        return self.uncertainDuration
    
    def setUncertainDuration(self,uncertainDuration):
        self.uncertainDuration = uncertainDuration
            
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
    
    def getJobId(self):
        return self.jobId
    
    def setJobId(self, jobId):
        self.jobId = jobId
    
    def checkStartStop(self):
        if (self.getStart() + self.getDuration()) == self.getStop() and (self.getStop() - self.getDuration()) == self.getStart():
            return True
        else:
            return False
    
    