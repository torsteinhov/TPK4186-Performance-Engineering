'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''
import sys
import random
import time
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
    
    def getRandomSchedule(self, allSchedules):
        index = random.randint(0, len(allSchedules))
        return allSchedules[index]
    
    def positionSwap(self, list, p1, p2):

        copyList = list.copy()
        copyList[p1], copyList[p2] = copyList[p2], copyList[p1]

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

    
    '''TASK 9'''
    def experimentAllSchedules(self, problem):

        start_timeV1 = time.time()
        allSchedules = self.generateAllPossibleSchedules()

        # TODO SHOW EXPERIMENT

        # Would like to demonstrate the length of different schedules
        print("The number of different schedules is {}".format(len(allSchedules)))
        print('\n')

        worstTime = self.calcTotalOperationTime(allSchedules[0], problem)
        bestTime = self.calcTotalOperationTime(allSchedules[0], problem)
        bestSchedule = allSchedules[0]
        worstSchedule = allSchedules[0]

        for schedule in allSchedules:
            operationTime = self.calcTotalOperationTime(schedule, problem)
            if operationTime < bestTime:
                bestSchedule = schedule
                bestTime = operationTime
                
            elif operationTime > worstTime:
                worstSchedule = schedule
                worstTime = operationTime
        
        print(f'The best schedule for the given problem is: {bestSchedule}')
        print(f'The duration time of the best schedule is: {bestTime}')
        print('\n')
        print(f'The worst schedule for the given problem is: {worstSchedule}')
        print(f'The duration time of the worst schedule is: {worstTime}')
        print('\n')
        print(f'The runtime of the brute force algorithm was: {round(time.time() - start_timeV1, 3)} seconds')

    '''TASK 10'''
    def gradientDescentV1(self, problem):
        
        # Creates a random schedule based on the problem
        allSchedules = self.generateAllPossibleSchedules()

        # This is the initial schedule choosed random
        initialSchedule = self.getRandomSchedule(allSchedules)

        makespan = self.calcTotalOperationTime(initialSchedule, problem)
        
        best = True
        bestNeighbour,bestMakespan = self.calculateBestNeighbour(initialSchedule, problem, makespan, alreadyCheckedSchedule=[])
        #Stop the recursiv call when no better solotuion from neibhours is achieved. 
        while best:
            if bestMakespan < makespan:
                bestNeighbour, makespan = self.calculateBestNeighbour(initialSchedule, problem, makespan, alreadyCheckedSchedule=[])
            else:
                best=False

        
        print(f'The best schedule after gradient descent v1 is: {bestNeighbour}')
        print(f'With a makespan of: {makespan}')

        return bestNeighbour,makespan
    
    '''TASK 11'''
    def gradientDescentV2(self, problem, n_initialStates):
        bestNeighbourV2 = None
        bestMakespanV2 = sys.maxsize

        # Creates all possible schedules
        allSchedules = self.generateAllPossibleSchedules()

        for i in range(n_initialStates):
            alreadyCheckedSchedules=[]

            # This is the initial schedule choosed random
            initialSchedule = self.getRandomSchedule(allSchedules)
            alreadyCheckedSchedules.append(initialSchedule)
            makespan = self.calcTotalOperationTime(initialSchedule, problem)
            
            best = True
            bestNeighbour,bestMakespan = self.calculateBestNeighbour(initialSchedule, problem, makespan, alreadyCheckedSchedules)
            #Stop the recursive call when no better solution from neibhours is achieved. 
            while best:
                if bestMakespan < makespan:
                    bestNeighbour, makespan = self.calculateBestNeighbour(initialSchedule, problem, makespan, alreadyCheckedSchedules)
                    alreadyCheckedSchedules.append(bestNeighbour)
                else:
                    best=False
            
            if makespan < bestMakespanV2:
                bestMakespanV2 = makespan
                bestNeighbourV2 = bestNeighbour

        print(f'The best schedule after gradient descent v2 is: {bestNeighbourV2}')
        print(f'With a makespan of: {bestMakespanV2}')
        

        return bestNeighbourV2,bestMakespanV2
    
    '''TASK 12'''
    def experimentalStudyGradientDescent(self, problem, n_initialStates):

        start_timeV1 = time.time()
        self.gradientDescentV1(problem)
        print(f'The runtime of the initial algorithm was: {round(time.time() - start_timeV1, 3)} seconds')

        start_timeV2 = time.time()
        self.gradientDescentV2(problem, n_initialStates)
        print(f'The runtime of the improved algorithm was: {round(time.time() - start_timeV2, 3)} seconds')

    def calculateBestNeighbour(self, schedule, problem, makespan, alreadyCheckedSchedule):
        
        neighbours= []
        bestSchedule = schedule
        for i in range(1, len(schedule)):
            if schedule[i]!=schedule[i-1]:
                neighbour = self.positionSwap(schedule, i-1, i)
                neighbours.append(neighbour)

        for neighbour in neighbours:
            
            if neighbour not in alreadyCheckedSchedule: 
                operationTimeNeighbour = self.calcTotalOperationTime(neighbour, problem)
                if operationTimeNeighbour < makespan:
                    bestSchedule = neighbour
                    makespan = operationTimeNeighbour
            else: 
                continue

        return bestSchedule, makespan
