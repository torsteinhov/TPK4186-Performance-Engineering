'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''


class Schedule:
    
    '''
    A class used to represent an schedule which is a list of jobs
    ...
    
    Attributes
    ----------
    jobs : list
        a list with job objects
    operationsJobId: list
        a list
    

    Methods
    -------

    getJobs()
        gets the jobs
    setJobs(jobs)
        sets the jobs
    '''

    def __init__(self, jobs=None, operationsJobId = []):
        self.jobs = jobs
        self.operationsJobId = operationsJobId #[operation, operation, operation, ...] with the number representing the job ID
    
    def getJobs(self):
        return self.jobs
    
    def setJobs(self, jobs):
        self.jobs = jobs