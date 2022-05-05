'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''

from itertools import permutations

class Calculator:

    def __init__(self, machines, jobs):
        self.jobs = jobs
        self.machines = machines
    
    def getMachines(self):
        return self.machines
    
    def setMachines(self, machines):
        self.machines = machines
    
    def getJobs(self):
        return self.jobs
    
    def setJobs(self, jobs):
        self.jobs = jobs
    
    def fromTuple2List(self, allCandidateSchedules):
        allCandidateSchedulesList = []
        for cand in allCandidateSchedules:
            candidate = []
            for element in cand:
                candidate.append(element)
            allCandidateSchedulesList.append(candidate)
        return allCandidateSchedulesList
    
    def generateAllPossibleSchedules(self):
        simpleSchedule=[]
        for job in self.getJobs():
            for operation in job.getOperations():
                simpleSchedule.append(job.getId())
        
        allCandidateSchedules=list(permutations(simpleSchedule))
        allCandidateSchedulesList = self.fromTuple2List(allCandidateSchedules)

        # REMOVE DUPLICATES
        allCandidateSchedulesList = list(set(map(lambda i: tuple(i), allCandidateSchedulesList)))
        allCandidateSchedulesList2 = self.fromTuple2List(allCandidateSchedulesList)

        print("The number of different schedules is {}".format(len(allCandidateSchedulesList2)))
        return allCandidateSchedulesList2

    # schedule = [1,1,1,2,2,2] jobId's
    def calcTotalOperationTime(self, schedule, problem):

        for machine in problem.getMachines():
            machine.setOperations([])

        machineTimes = [0]*len(problem.getMachines()) # [time machine 1, time machine 2, ...]
        # schedule = [1,2,2,3,1,3,1,3]
        for jobId in schedule:
            
            job = problem.getJob(jobId)
            operationNr = job.getOperationNr()
            operation = job.getOperations()[operationNr]

            if job.getOperationNr() == 0:
                machineTimes[operation.getMachine()-1] += operation.getDuration()
            elif job.getOperationNr() > 0:
                previousOperation = job.getOperations()[operationNr-1]
                previousTime = machineTimes[operation.getMachine()-1]
                machineTimes[operation.getMachine()-1] = previousTime + operation.getDuration()

            print('machineTimes: ', machineTimes)
            job.setOperationNr(operationNr+1)

        return max(machineTimes)

        '''    firstStart = 0
            for operation in operation.getMachine().getOperations():
                firstStart += operation.getDuration()

            for machine in problem.getMachines():
                start, stop = machine.getLastJob(jobId)

                if stop == firstStart:
                    # We can neglect the order of jobs with this jobId
                    if stop > 0:
                        firstStart = stop + 1
                elif stop > firstStart:
                    firstStart = stop + 1
            
            operation.getMachine().addOperation(operation, jobId, firstStart)
        
        totalTime = 0'''
        
        '''newSchedule = []
        time = 0
        schedule = self.getSchedule()
        for job in schedule:
            firstOperation = job.getOperations()[0]
            if firstOperation.getMachine().isAvailable():
                firstOperation.getMachine().isAvailable(False)
                time += firstOperation.getDuration()
            else:
                pass'''