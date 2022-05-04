'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''

class Machine:

    '''
    Assumptions:
        - We assume that all machines have equal capabilities and performance.
        - We assume that we can neglect the travel distance between machines inside the factory. (Importing the layout of the factory would add a new dimensionality of this problem)
    '''

    def __init__(self, id, currOperation = None):
        self.id = id
        self.currOperation = currOperation

    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id

    def getCurrOperation(self):
        return self.currOperation
    
    def setCurrOperation(self, currOperation):
        self.currOperation = currOperation
