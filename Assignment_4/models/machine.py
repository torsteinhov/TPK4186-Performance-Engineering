'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''

class Machine:

    '''
    A class used to represent a machine
    ...
    
    Attributes
    ----------
    id : string
        a string with the machines' id
    operations: list 
        list of operation objects
    available: boolean
        true if the machine is available. Otherwise false 
    

    Methods
    -------

    getId()
        gets the machines' id
    getOperations()
        get a list of operations 
    getLastJob()
        get the machine's last jobb
    getStart()
        get the start time
    isAvailable()
        check if the machine is available
    setId(id)
        sets the machine's id
    setOperations(operations)
        set a list of operations
    addOperation(operation)
        add a single operation to a machine


    Assumptions:
        - We assume that all machines have equal capabilities and performance.
        - We assume that we can neglect the travel distance between machines inside the factory. (Importing the layout of the factory would add a new dimensionality of this problem)

    '''

    def __init__(self, id, available=True):
        self.id = id
        self.operations = []
        self.available = available

    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id

    def getOperations(self):
        return self.operations
    
    def setOperations(self, operations):
        self.operations = operations
    
    def addOperation(self, operation, jobId, start):

        operation.setStart(start)
        operation.setJobId(jobId)
        self.getOperations().append(operation)
        '''
        # We want to handle the case where the machine has nothing to do
        if start > len(self.getOperations()):

            for i in range(start - len(self.getOperations())):
                self.getOperations().append(0)'''
    
    def isAvailable(self, availability):
        self.available = availability

    def getLastJob(self, jobId):

        start = 0
        stop = 0
        # Find the start index of the last job performed on this machine
        for i in range(len(self.getOperations())):
            if self.getOperations()[i] == jobId:
                start = i
                break
        # Find the stop index of the last job performed on this machine
        for i in range(len(self.getOperations()), -1, -1, -1):
            if self.getOperations()[i] == jobId:
                stop = i
                break
        return start, stop


