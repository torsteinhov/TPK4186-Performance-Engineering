'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''
import sys
import random
import time
import numpy as np
import pandas as pd
from itertools import permutations
from lightgbm import LGBMRegressor

class Calculator:

    '''
    A class used to calculate the total operation time of a schedule and the makespan of a problem.
    The class also includes multiple methods of different levels for performing the gradient descent algorithm for stochastic simulations.  
    ...
    
    Attributes
    ----------
    jobs : list
        a list with job objects
    machines: list
        a list of machine object
        
    Methods
    -------
    getMachines()
        gets the machines

    getJobs()
        gets the jobs

    setMachines(machine)
        sets the machines

    setJobs(jobs)
        sets the jobs

    getRandomSchedule()
        gets a random schedule

    positionSwap(list, p1, p2)
        swaps position for checking neighbours in gradient descent

    fromTuple2List
        creates a list from candidate schedules

    generateAllPossibleSchedules()
        generates all possible schedules

    generateAllPossibleSchedulesWithUncertainties(leftTail, rightTail)
        generates all possible schedules with uncertainties

    calcTotalOperationTime(schedule, problem)
        calculates the total operation time for a given schedule in a problem

    calcTotalUncertainOperationTime(schedule, problem)
        calculates the total operation time with uncertainties for a given schedule in a problem

    experimentAllSchedules(problem)
        gives the best and worst schedule, with their corresponding duration, for a given problem using a brute force algorithm.

    gradientDescentV1(problem)
        Implements the gradient descent algorithm that guesses an schedule, and through observing the operation time of its neighbours
        moves in the downhill direction of faster schedule times until it meets a minimum.

    gradientDescentV2(problem, n_initialStates)
        Implements the gradient descent algorithm that guesses multiple schedules to not be victim for local minimums.
        When a local minimum is reached, the algorithm can still rely on another gradient descent path that hopefully find the best schedule,
        the n_initialStates variable controls the amount of guesses and the algorithm should initialize. It also holds track of the neighbours it has
        already calculated, it therefore does not calculate any previous state multiple times.

    experimentalStudyGradientDescent(problem, n_initialStates)
        Conducts an experimental study to investigate the differences in the two gradient descent algorithms, which displays that the first initial algorithm
        may fall into a local minimum which does not result in the best schedule. We save computational power aswell by not calculating some neighbours
        twice, but this effect is overshadowed by the extra computational power to run multiple guesses and investigate its neighbours.

    gradientDescentV2Uncertainties(problem, n_initialStates, leftTail, rightTail)
        Takes the same logic as gradientDescentV2 but implements a factor of uncertainty based on a triangular distribution with the original duration as mode.
        This makes the schedule open for delays but also early finishes, this form of uncertainty will lead to different results, which needs to converge.

    experimentalStudyUncertainties(problem, n_initialStates, leftTail, rightTail, allowedError)
        We here want to tackle the problem with the uncertainties, which is calculate how many iterations we need for the results to converge when uncertainties is presented.
        This is done by an experimental study of the different calculations, iterations and runtime.

    calculateBestNeighbour(schedule, problem, makespan, alreadyCheckedSchedule)
        Takes in a schedule and finds all the different neighbours of that specific schedule.
        It then calculates the makespan of all the neighbours and returns the best neighbour for the given schedule,
        which is the next step of our algorithm.

    calculateBestNeighbourWithUncertainty(schedule, problem, makespan, alreadyCheckedSchedule)
        Same logic as in calculateBestNeighbour but with the uncertainties introduced.

    gradientDescentUncertaintiesWithML(problem, n_initialStates, leftTail, rightTail)
        The crown of the assignment.
        Implements the best gradient descent algorithm and when N schedules have been calculated,
        it runs a machine learning model (ensemble lightGBM) on the data to be able to predict future schedules.
        This shows drastic value when the job scheduling problems really increases in size.

    calculateBestNeighbourWithUncertaintyML(schedule, problem, makespan, alreadyCheckedSchedule)
        Same logic as in calculateBestBeighbourWithUncertainty but with additional logic to support the machine learning prediction.
        We are here given in the already fitted model, and can use it to predict all the neighbours,
        instead of manually calculating the schedule time.
    '''

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
    
    def createRandomSchedule(self, schedule):
        shuffleSchedule = schedule.copy()
        random.shuffle(shuffleSchedule)
        return shuffleSchedule
    
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
        '''Generates all the possible schedules corresponding to a problem.'''


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
    
    
    def generateUncertainDurationSchedule(self, leftTail, rightTail):
        simpleSchedule=[]
        for job in self.getJobs():
            for operation in job.getOperations():
                uncertain_duration = np.random.triangular(operation.getDuration()*leftTail, operation.getDuration(), operation.getDuration()*rightTail)
                operation.setUncertainDuration(uncertain_duration)

                simpleSchedule.append(job.getId())
        
        return simpleSchedule
    
    def generateSimpleSchedule(self):
        simpleSchedule=[]
        for job in self.getJobs():
            for operation in job.getOperations():
                simpleSchedule.append(job.getId())
        
        return simpleSchedule
    
    
    def generateAllPossibleSchedulesWithUncertainties(self):
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
        '''Calculates the operation time for a given schedule in a problem. '''

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

            job.setOperationNr(operationNr+1)

        return max(machineTimes)
    

    '''TASK 13'''
    def calcTotalUncertainOperationTime(self, schedule, problem):

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
                machineTimes[operation.getMachine()-1] += operation.getUncertainDuration()
            elif job.getOperationNr() > 0:

                prevJobsTime = 0
                for i in range(job.getOperationNr()):
                    prevJobsTime += job.getOperations()[i].getUncertainDuration()

                if prevJobsTime > machineTimes[operation.getMachine()-1]:
                    machineTimes[operation.getMachine()-1] = prevJobsTime + operation.getUncertainDuration()
                else:
                    machineTimes[operation.getMachine()-1] += operation.getUncertainDuration()

            job.setOperationNr(operationNr+1)

        return max(machineTimes)

    
    '''TASK 9'''
    def experimentAllSchedules(self, problem):

        start_timeV1 = time.time()
        allSchedules = self.generateAllPossibleSchedules()

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
        
        # This is the initial schedule choosed random
        simpleSchedule = self.generateSimpleSchedule()
        initialSchedule = self.createRandomSchedule(simpleSchedule)

        makespan = self.calcTotalOperationTime(initialSchedule, problem)
        
        best = True
        bestNeighbour,bestNeighbourMakespan = self.calculateBestNeighbour(initialSchedule, problem, makespan, alreadyCheckedSchedule=[])
        #Stop the recursiv call when no better solotuion from neibhours is achieved. 
        while best:
            if bestNeighbourMakespan < makespan:
                makespan=bestNeighbourMakespan
                bestNeighbour, bestNeighbourMakespan = self.calculateBestNeighbour(initialSchedule, problem, makespan, alreadyCheckedSchedule=[])

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
        simpleSchedule = self.generateSimpleSchedule()

        for i in range(n_initialStates):
            alreadyCheckedSchedules=[]

            # This is the initial schedule choosed random
            initialSchedule = self.createRandomSchedule(simpleSchedule)
            alreadyCheckedSchedules.append(initialSchedule)
            makespan = self.calcTotalOperationTime(initialSchedule, problem)
            
            best = True
            bestNeighbour, bestNeighbourMakespan = self.calculateBestNeighbour(initialSchedule, problem, makespan, alreadyCheckedSchedules)
            #Stop the recursive call when no better solution from neibhours is achieved. 
            while best:
                if bestNeighbourMakespan < makespan:
                    makespan=bestNeighbourMakespan
                    bestNeighbour, bestNeighbourMakespan = self.calculateBestNeighbour(initialSchedule, problem, makespan, alreadyCheckedSchedule=[])
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
        print(f'The runtime of the initial gradient descent algorithm was: {round(time.time() - start_timeV1, 3)} seconds\n')

        start_timeV2 = time.time()
        self.gradientDescentV2(problem, n_initialStates)
        print(f'The runtime of the improved gradient descent algorithm was: {round(time.time() - start_timeV2, 3)} seconds\n')
    
    
    def gradientDescentV2Uncertainties(self, problem, n_initialStates, leftTail, rightTail): # tails given as a decimal representing percentage
        bestNeighbourV2 = None
        bestMakespanV2 = sys.maxsize

        simpleSchedule = self.generateUncertainDurationSchedule(leftTail, rightTail)

        for i in range(n_initialStates):
            alreadyCheckedSchedules=[]

            # This is the initial schedule choosed random
            initialSchedule = self.createRandomSchedule(simpleSchedule)
            alreadyCheckedSchedules.append(initialSchedule)
            makespan = self.calcTotalUncertainOperationTime(initialSchedule, problem)
            
            best = True
            bestNeighbour,bestNeighbourMakespan = self.calculateBestNeighbourWithUncertainty(initialSchedule, problem, makespan, alreadyCheckedSchedules)
            #Stop the recursive call when no better solution from neibhours is achieved. 
            while best:
                if bestNeighbourMakespan < makespan:
                    makespan=bestNeighbourMakespan
                    bestNeighbour, bestNeighbourMakespan = self.calculateBestNeighbour(initialSchedule, problem, makespan, alreadyCheckedSchedule=[])
                    alreadyCheckedSchedules.append(bestNeighbour)
                else:
                    best=False
            
            if makespan < bestMakespanV2:
                bestMakespanV2 = makespan
                bestNeighbourV2 = bestNeighbour

        print(f'The best schedule after gradient descent v2 with uncertainties is: {bestNeighbourV2}')
        print(f'With a makespan of: {bestMakespanV2}')
        

        return bestNeighbourV2,bestMakespanV2

    '''TASK 14 & 15'''
    def experimentalStudyUncertainties(self, problem, n_initialStates, leftTail, rightTail, allowedError):

        print('\n')
        start_timeV1 = time.time()
        bestSchedule, bestMakespan = self.gradientDescentV2(problem, n_initialStates)
        print(f'The runtime of the algorithm with determined durations was: {round(time.time() - start_timeV1, 3)} seconds\n')

        start_timeV2 = time.time()
        makespanUncertaintyTimeList = []
        avg = 0.0
        numExecutions = 0
        
        while not ((avg < round(bestMakespan*(1+allowedError),2)) and (avg > round(bestMakespan*(1-allowedError),2))):
            uncertainSchedule, uncertainMakespan = self.gradientDescentV2Uncertainties(problem, n_initialStates, leftTail, rightTail)
            makespanUncertaintyTimeList.append(uncertainMakespan)
            avg = sum(makespanUncertaintyTimeList)/len(makespanUncertaintyTimeList)
            numExecutions += 1
            print(f'The average is now {avg}')

        print('\n')
        print(f'The runtime of the algorithm with convergence of uncertain durations was: {round(time.time() - start_timeV2, 3)} seconds\n')
        print(f'The amount of iterations required to converge with allowed error {allowedError}, was: {numExecutions}')
        print(f'The different makespans during the calculations was the following: {makespanUncertaintyTimeList}, with the average makespan: {avg}')

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

    def calculateBestNeighbourWithUncertainty(self, schedule, problem, makespan, alreadyCheckedSchedule):
        
        neighbours= []
        bestSchedule = schedule
        for i in range(1, len(schedule)):
            if schedule[i]!=schedule[i-1]:
                neighbour = self.positionSwap(schedule, i-1, i)
                neighbours.append(neighbour)

        for neighbour in neighbours:
            
            if neighbour not in alreadyCheckedSchedule: 
                operationTimeNeighbour = self.calcTotalUncertainOperationTime(neighbour, problem)
                if operationTimeNeighbour < makespan:
                    bestSchedule = neighbour
                    makespan = operationTimeNeighbour
            else: 
                continue

        return bestSchedule, makespan

    '''TASK 17'''
    def gradientDescentUncertaintiesWithML(self, problem, n_initialStates, leftTail, rightTail, trainingSize): # tails given as a decimal representing percentage
        bestNeighbourV2 = None
        bestMakespanV2 = sys.maxsize
        unTrained = True

        # Initialize a schedule where uncertain durations are set
        simpleSchedule = self.generateUncertainDurationSchedule(leftTail=leftTail, rightTail=rightTail)

        calculatedSchedules=[]
        for i in range(n_initialStates):
            alreadyNeighbourSchedules=[]

            # This is the initial schedule choosed random
            initialSchedule = self.createRandomSchedule(simpleSchedule)
            alreadyNeighbourSchedules.append(initialSchedule)
            makespan = self.calcTotalUncertainOperationTime(initialSchedule, problem)
            tempInit=initialSchedule.copy()
            tempInit.append(makespan)
            calculatedSchedules.append(tempInit)

            best = True
            bestNeighbour,bestMakespan, x = self.calculateBestNeighbourWithUncertaintyML(initialSchedule, problem, makespan, alreadyNeighbourSchedules)
            for el in x:
                calculatedSchedules.append(el)
            #Stop the recursive call when no better solution from neibhours is achieved. 
            while best:

                if len(calculatedSchedules) > trainingSize and unTrained:

                    dataframe = pd.DataFrame(calculatedSchedules)
                    columns = []
                    for i in range(len(dataframe.iloc[0])):
                        if i == len(dataframe.loc[0])-1:
                            columns.append('Target')
                            break
                        columns.append('Attribute_'+str(i+1))

                    dataframe.columns = columns

                    X = dataframe.iloc[:, dataframe.columns != 'Target']
                    y = dataframe['Target']

                    lgbm = LGBMRegressor()
                    lgbm.fit(X,y)

                    unTrained = False

                if len(calculatedSchedules) > trainingSize and not unTrained:
                    if bestMakespan < makespan:
                        bestNeighbour, makespan, neighboursCalced = self.estimateBestNeighbourWithUncertaintyML(initialSchedule, makespan, alreadyNeighbourSchedules, lgbm)
                        bestMakespan = makespan
                        alreadyNeighbourSchedules.append(bestNeighbour)
                        for el in neighboursCalced:
                            calculatedSchedules.append(el)
                    else:
                        best=False
                
                else:
                    if bestMakespan < makespan:
                        bestNeighbour, makespan, neighbours = self.calculateBestNeighbourWithUncertaintyML(initialSchedule, problem, makespan, alreadyNeighbourSchedules)
                        bestMakespan = makespan
                        alreadyNeighbourSchedules.append(bestNeighbour)
                        for el in neighbours:
                            calculatedSchedules.append(el)
                    else:
                        best=False
            
            if makespan < bestMakespanV2:
                bestMakespanV2 = makespan
                bestNeighbourV2 = bestNeighbour

        print(f'The number of calculated schedules is: {len(calculatedSchedules)}')
        print(f'The best schedule after gradient descent with uncertainties and machine learning is: {bestNeighbourV2}')
        print(f'With an estimated makespan of: {bestMakespanV2}')

        return bestNeighbourV2,bestMakespanV2

    def calculateBestNeighbourWithUncertaintyML(self, schedule, problem, makespan, alreadyCheckedSchedule):
        
        neighbours= []
        bestSchedule = schedule
        for i in range(1, len(schedule)):
            if schedule[i]!=schedule[i-1]:
                neighbour = self.positionSwap(schedule, i-1, i)
                neighbours.append(neighbour)
                
        neighboursCalced=[]
        for neighbour in neighbours:
        
            if neighbour not in alreadyCheckedSchedule:

                operationTimeNeighbour = self.calcTotalUncertainOperationTime(neighbour, problem)
                tempNeighbour = neighbour.copy()
                tempNeighbour.append(operationTimeNeighbour)
                neighboursCalced.append(tempNeighbour) 
                if operationTimeNeighbour < makespan:
                    bestSchedule = neighbour
                    makespan = operationTimeNeighbour
            else:
                continue

        return bestSchedule, makespan, neighboursCalced
    
    def estimateBestNeighbourWithUncertaintyML(self, schedule, makespan, alreadyCheckedSchedule, lgbm):
        
        neighbours= []
        bestSchedule = schedule
        for i in range(1, len(schedule)):
            if schedule[i]!=schedule[i-1]:
                neighbour = self.positionSwap(schedule, i-1, i)
                neighbours.append(neighbour)
                
        neighboursCalced=[]
        for neighbour in neighbours:
        
            if neighbour not in alreadyCheckedSchedule:
                
                newData = pd.DataFrame(neighbour)
                newData = newData.transpose()
                operationTimeNeighbour = lgbm.predict(newData)

                tempNeighbour = neighbour.copy()
                tempNeighbour.append(operationTimeNeighbour[0])
                neighboursCalced.append(tempNeighbour) 
                if operationTimeNeighbour < makespan:
                    bestSchedule = neighbour
                    makespan = operationTimeNeighbour
            else:
                continue

        return bestSchedule, makespan, neighboursCalced