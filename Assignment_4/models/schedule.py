'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''


"""Schedule is a list of jobs"""
class Schedule:

    def __init__(self, jobs=None, operationsJobId = []):
        self.jobs = jobs
        self.operationsJobId = operationsJobId #[operation, operation, operation, ...] with the number representing the job ID
    
    def getJobs(self):
        return self.jobs
    
    def setJobs(self, jobs):
        self.jobs = jobs