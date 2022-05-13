'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''

from calculator import Calculator
from models.job import Job
from models.machine import Machine
from models.operation import Operation
from models.schedule import Schedule
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

class Problem:
    '''
    A class used to represent problems. It is possible to create machines, jobs and import/export operations from Excel via methods in the class. 
    ...
    
    Attributes
    ----------
    filename : string
        a string with the Excel-files' path 
    machines: list
        a list of machine-objects
    jobs: list
        a list of job-objects
    data: dataframe
        a dataframe containing imported data from Excel

    Methods
    -------

    getMachines()
        gets the machines
    getJobs()
        gets the jobs
    getData()
        gets the data
    setMachines(machines)
        sets the machines
    setJobs(jobs)
        sets the jobs
    addJob(job)
        adds a single job
    removeJob(job)
        removes a single job
    setData(data)
        sets the data
    printData()
        prints the data 
    formatData2
        prints the data in list form
    createRandomJobScheduling(nrOfJobs, maxOpsPerJob, minOpsPerJob, nrOfMachines, maxDuration)
        creates a random job scheduling
    loadAndFormatData(filename)
        This function generates a random job scheduling problem with the given parameters: number of jobs,
        maximum opservations per job, minimium operations per job, number og machines and maximum duration
        of a operation.
    exportProblem2Excel(filename)
        exports the data to a Excel-file

    '''

    def __init__(self, machines=None, jobs=None):
        self.machines = machines # [machine, machine, ...]
        self.jobs = jobs # [job, job, ...]
        self.data = None

    def getMachines(self):
        return self.machines
    
    def setMachines(self, machines):
        self.machines = machines
    
    def addMachine(self, machine):
        self.machines.append(machine)
    
    def removeMachine(self, machine):
        self.machines.remove(machine)
    
    def getJobs(self):
        return self.jobs
    
    def getJob(self, jobId):
        for job in self.getJobs():
            if job.getId() == jobId:
                return job
    
    def addJob(self, job):
        self.jobs.append(job)
    
    def removeJob(self, job):
        self.jobs.remove(job)
    
    def setJobs(self, jobs):
        self.jobs = jobs
    
    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data
    
    def printData(self):
        print(self.getData())
    
    def formatData2(self):
        print(self.getData().values.tolist())
    
    '''TASK 4'''

    def createRandomJobScheduling(self, nrOfJobs, maxOpsPerJob, minOpsPerJob, nrOfMachines, maxDuration):
       
        machines = []
        machineID = [i for i in range(nrOfMachines)]
        for id in machineID:
            machines.append(Machine(id))

        jobs = []
        
        for i in range(1,nrOfJobs+1):
            jobs.append(Job(i,operations=[]))

        for job in jobs:
            for i in range(random.randint(minOpsPerJob,maxOpsPerJob)):
                operation=Operation(random.randint(0, nrOfMachines),random.randint(1,maxDuration+1))
                job.addOperation(operation)
                    
        self.setJobs(jobs)
        self.setMachines(machines)
    
    def printProblem(self):
        operations = 0
        for job in self.getJobs():
            for operation in job.getOperations():
                operations += 1
                
        print(f'This job scheduling problem has {len(self.getJobs())} Jobs, with a total of {operations} Operations and {len(self.getMachines())} Machines.')
        
    def loadAndFormatData(self, filename):
        '''Imports and formats the data from a file'''
        self.setData(pd.read_excel(filename, header=0))
        jobs = []

        # Gets the job number of the last element in the Job column
        numberOfJobs=self.data['Job'].max()
        for i in range(1,numberOfJobs+1):
            jobs.append(Job(i,operations=[]))
            
        machines = []
        machinesID=[]

        for index, row in self.getData().iterrows():

            operation=[]
            for job in jobs:
                if row['Job']==job.getId():

                    operation = Operation(row['Machine'], row['Duration'])
                    job.addOperation(operation)    
            
            machineID=row["Machine"]
            
            if machineID not in machinesID:
                machinesID.append(machineID)
                machines.append(Machine(row["Machine"]))

        self.setJobs(jobs)
        self.setMachines(machines)

    '''TASK 5'''
    def exportProblem2Excel(self,filename):

        excel_list = [['Job', 'Machine', 'Duration']]
        for job in self.getJobs():
            for operation in job.getOperations():
                excel_list.append([job.getId(), operation.getMachine(), operation.getDuration()])

        df = pd.DataFrame(excel_list)
        writer = pd.ExcelWriter(filename, engine='xlsxwriter')
        df.to_excel(writer, index=False)
        writer.save()

problem = Problem()
#problem.loadAndFormatData('test3.xlsx')

'''Here we overwrite the input file and create our own dataset with given parameters(for simplicity):'''
#problem.createRandomJobScheduling(nrOfJobs=5, maxOpsPerJob=200, minOpsPerJob=100, nrOfMachines=5, maxDuration=10)
#problem.exportProblem2Excel()

#calculator = Calculator(problem.getMachines(), problem.getJobs())
#print(calculator.generateAllPossibleSchedules())
#print(calculator.calcTotalOperationTime([1,2,2,3,1,3,1,3], problem))
#print(calculator.calcTotalOperationTime([1,3,3,3,1,2,2,1], problem))

#calculator.experimentAllSchedules(problem)
#calculator.gradientDescentV1(problem)
#calculator.gradientDescentV2(problem, 3)
#calculator.experimentalStudyGradientDescent(problem, n_initialStates=3)
#calculator.experimentalStudyUncertainties(problem, n_initialStates=3, leftTail=0.5, rightTail=1.5, allowedError=0.01)
#calculator.gradientDescentUncertaintiesWithML(problem, 5, 0.5, 1.5, 100)