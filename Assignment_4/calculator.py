'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''
import sys
import random
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
    
    def getRandomSchedule(allSchedules):
        index = random.randint(0, len(allSchedules))
        return allSchedules[index]
    
    def positionSwap(list, p1, p2):

        copyList = list.copy()

        copyList[p1] = copyList[p2]
        copyList[p2] = copyList[p1]

        return copyList
    
    def fromTuple2List(self, allCandidateSchedules):
        allCandidateSchedulesList = []
        for cand in allCandidateSchedules:
            candidate = []
            for element in cand:
                candidate.append(element)
            allCandidateSchedulesList.append(candidate)
        return allCandidateSchedulesList
    
    '''TASK 8'''
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

        return allCandidateSchedulesList2

    '''TASK 7'''
    # schedule = [1,2,2,3,1,3,1,3]
    def calcTotalOperationTime(self, schedule, problem):

        for machine in problem.getMachines():
            machine.setOperations([])
        
        for job in problem.getJobs():
            job.setOperationNr(0)

        machineTimes = [0]*len(problem.getMachines()) # [time machine 1, time machine 2, ...]

        for jobId in schedule:
            
            job = problem.getJob(jobId)
            operationNr = job.getOperationNr()
            operation = job.getOperations()[operationNr]

            if job.getOperationNr() == 0:
                machineTimes[operation.getMachine()-1] += operation.getDuration()
            elif job.getOperationNr() > 0:

                prevJobsTime = 0
                for i in range(job.getOperationNr()):
                    prevJobsTime += job.getOperations()[i].getDuration()

                if prevJobsTime > machineTimes[operation.getMachine()-1]:
                    machineTimes[operation.getMachine()-1] = prevJobsTime + operation.getDuration()
                else:
                    machineTimes[operation.getMachine()-1] += operation.getDuration()

            #print('machineTimes: ', machineTimes)
            job.setOperationNr(operationNr+1)

        return max(machineTimes)

    

    def experimentAllSchedules(self, problem):

        allSchedules = self.generateAllPossibleSchedules()

        # TODO SHOW EXPERIMENT

        # Would like to demonstrate the length of different schedules
        print("The number of different schedules is {}".format(len(allSchedules)))
        print('\n')

        worstTime = self.calcTotalOperationTime(allSchedules[0], problem)
        bestTime = self.calcTotalOperationTime(allSchedules[0], problem)
        bestSchedule = None
        worstSchedule = None

        for schedule in allSchedules:
            operationTime = self.calcTotalOperationTime(schedule, problem)
            if operationTime < bestTime:
                bestSchedule = schedule
                bestTime = operationTime
                break
            elif operationTime > worstTime:
                worstSchedule = schedule
                worstTime = operationTime
        
        print(f'The best schedule for the given problem is: {bestSchedule}')
        print(f'The duration time of the best schedule is: {bestTime}')
        print('\n')
        print(f'The worst schedule for the given problem is: {worstSchedule}')
        print(f'The duration time of the worst schedule is: {worstTime}')

    def gradientDescentV1(self, problem):
        
        # Creates a random schedule based on the problem
        allSchedules = self.generateAllPossibleSchedules(problem)

        # This is the initial schedule choosed random
        currSchedule = self.getRandomSchedule(allSchedules)

        makespan = self.calcTotalOperationTime(problem, currSchedule)

        checkedNeighbours = []
        currNeighbours = []
        for 

