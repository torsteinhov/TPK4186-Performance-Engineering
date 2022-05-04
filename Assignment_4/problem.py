'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''

from models.job import Job
from models.machine import Machine
from models.operation import Operation
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Problem:

    def __init__(self, machines, jobs):
        self.machines = machines # [machine, machine, ...]
        self.jobs = jobs # [job, job, ...]
        self.data = pd.read_excel('jobs_data.xlsx', index_col=0)

    def getMachines(self):
        return self.machines
    
    def setMachines(self, machines):
        self.machines = machines
    
    def getJobs(self):
        return self.jobs
    
    def setJobs(self, jobs):
        self.jobs = jobs
    
    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data
    
    def printData(self):
        print(self.getData())
    
    def visualize(self):
    
        JOBS = self.getJobs()
        MACHINES = self.getMachines()
        data = self.getData()
        
        bar_style = {'alpha':1.0, 'lw':25, 'solid_capstyle':'butt'}
        text_style = {'color':'white', 'weight':'bold', 'ha':'center', 'va':'center'}
        colors = ['blue', 'yellow', 'red']

        fig, ax = plt.subplots(1, figsize=(12, 5+(len(JOBS)+len(MACHINES))/4))

        ax.barh(data.operation, data.duration)
        
        plt.show()





'''EKSPERIMENTERING MED DATASTRUKTUREN'''

machine1 = Machine('M-1')
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
#problem.visualize()