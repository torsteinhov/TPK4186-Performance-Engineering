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



    def __init__(self, machines=None, jobs=None, filename=None):
        self.filename = filename
        self.machines = machines # [machine, machine, ...]
        self.jobs = jobs # [job, job, ...]
        #self.data = pd.read_excel('jobs_data.xlsx', header=0)
        self.data = pd.read_excel(filename, header=0)

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
    def loadAndFormatData(self):
        jobs = []

        # Gets the job number of the last element in the Job column
        numerOfJobs=self.data['Job'].max()
        for i in range(1,numerOfJobs+1):
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
    def exportData2Excel(self):

        excel_list = [['Job', 'Machine', 'Duration']]
        for job in self.getJobs():
            for operation in job.getOperations():
                excel_list.append([job.getId(), operation.getMachine(), operation.getDuration()])

        df = pd.DataFrame(excel_list)
        writer = pd.ExcelWriter('exported_data.xlsx', engine='xlsxwriter')
        df.to_excel(writer, index=False)
        writer.save()

problem = Problem(filename='test2.xlsx')
problem.loadAndFormatData()
#problem.loadAndFormatUncertainData()
#problem.exportData2Excel()

calculator = Calculator(problem.getMachines(), problem.getJobs())
#print(calculator.generateAllPossibleSchedules())
#print(calculator.calcTotalOperationTime([1,2,2,3,1,3,1,3], problem))
#print(calculator.calcTotalOperationTime([1,3,3,3,1,2,2,1], problem))

#calculator.experimentAllSchedules(problem)
#calculator.gradientDescentV1(problem)
#calculator.gradientDescentV2(problem, 3)
#calculator.experimentalStudyGradientDescent(problem, n_initialStates=3)
#calculator.experimentalStudyUncertainties(problem, n_initialStates=3, leftTail=0.5, rightTail=1.5, allowedError=0.01)