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

class Problem:

    def __init__(self, machines=None, jobs=None):
        self.machines = machines # [machine, machine, ...]
        self.jobs = jobs # [job, job, ...]
        #self.data = pd.read_excel('jobs_data.xlsx', header=0)
        self.data = pd.read_excel('test.xlsx', header=0)

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
            
    def visualize(self):
    
        JOBS = self.getJobs()
        MACHINES = self.getMachines()
        
        bar_style = {'alpha':1.0, 'lw':25, 'solid_capstyle':'butt'}
        text_style = {'color':'white', 'weight':'bold', 'ha':'center', 'va':'center'}
        colors = ['blue', 'yellow', 'red']

        fig, ax = plt.subplots(1, figsize=(12, 5+(len(JOBS)+len(MACHINES))/4))

        ax.barh(data.operation, data.duration)
        
        plt.show()

problem = Problem()
problem.loadAndFormatData()
problem.exportData2Excel()

calculator = Calculator(problem.getMachines(), problem.getJobs())
calculator.generateAllPossibleSchedules()
print(calculator.calcTotalOperationTime([1,2,2,3,1,3,1,3], problem))
#print(calculator.calcTotalOperationTime([1,3,3,3,1,2,2,1], problem))

calculator.experimentAllSchedules(problem)

'''
for job in problem.getJobs():
    #print('Operations: ', job.getOperations())
    for operation in job.getOperations():
        print('Jeg er koplet til maskin: ', operation.getMachine(), ' og varer ', operation.getDuration())

for machine in problem.getMachines():
    print('Jeg er maskin nr: ', machine.getId())'''



'''EKSPERIMENTERING MED DATASTRUKTUREN'''

'''machine1 = Machine('M-1')
machine2 = Machine('M-2')
machines = [machine1, machine2]

operation1 = Operation('O-1', 2)
operation2 = Operation('O-2', 4)
operation3 = Operation('O-3', 1)
operations1 = [operation1, operation2, operation3]

job1 = Job('J-1',operations1)
operations2 = [operation1, operation3]
job2 = Job('J-2',operations2)
jobs = [job1, job2]

for operation in job1.getOperations():
    print(f'Operation: {operation.getId()} - duration: {operation.getDuration()}')

problem = Problem(machines, jobs)
for job in problem.getJobs():
    duration = 0
    for operation in job.getOperations():
        duration += operation.getDuration()

    print(f'Job: {job.getId()} lasts for a total of {duration} seconds')

problem.printData()
#problem.visualize()'''