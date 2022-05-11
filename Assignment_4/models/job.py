'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''
import copy

class Job:

    '''
    A class used to represent a job
    ...
    
    Attributes
    ----------
    id : int
        an integer with the job's id
    operations: list 
        list of operation objects
    start: int
        an integer representing the start time
    stop: int
        an integer representing the stop time
    operationNr: int
        an integer representing the operation number
    
    
    Methods
    -------
    getOperationNr()
        gets the operation number
    getId()
        gets the job id
    getOperations()
        get a list of operations in the current job
    getNextOperation()
        get the next operation at a specific time
    getStart()
        get the start time
    getStop()
        get the stop time
    setOperationNr(operatinNr)
        sets the operation number
    setId(id)
        sets the job id
    setOperations(operations)
        set a list of operations in a job
    addOperation(operation)
        add a single operation to a job
    setStart(start)
        sets a start time
    setStop(stop)
        sets a stop time 

 
    Constraints:
        Precedence constraints - This comes from the condition that for two consecutive tasks in the same job, we must complete the first one before the second job can be started.
                                 If we use task (0,1) and task (0,2) as example  the start time for task (0,2) must be 1 time unit after the start of task (0,2) => (1,3)

        No overlap constraints - This comes from the restriction that a machine can not work on two different tasks at the same time. As example we can take task (0,1) and (0,2)
                                 if these are to be performed on the same machine, one of them need to be moved their elapsed time amount.
    '''

    def __init__(self, id, operations=[], start=None, stop=None, operationNr=0):
        self.id = id
        self.operations = operations # [operation_object, operation_object,..]
        self.start = start
        self.stop = stop
        self.operationNr = operationNr

    def getOperationNr(self):
        return self.operationNr

    def setOperationNr(self,operationNr):
        self.operationNr = operationNr    

    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id
    
    def getOperations(self):
        return self.operations
    
    def getNextOperation(self, time):
        for operation in self.getOperations():
            if operation.getStart() >= time:
                return operation
    
    def setOperations(self, operations):
        self.operations = operations
    
    def addOperation(self, operation):
        #if operation not in self.operations:
        self.operations.append(operation)

    def removeOperation(self, operation):
        if operation in self.getOperations():
            self.operations.remove(operation)
    
    def getStart(self):
        return self.start
    
    def getStop(self):
        return self.stop

    def setStart(self, start):
        self.start = start
    
    def setStop(self, stop):
        self.stop = stop
    

    
    