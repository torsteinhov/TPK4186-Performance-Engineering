'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''
import pandas as pd
from models.job import Job
from models.machine import Machine
from models.operation import Operation
from problem import *


schedule = pd.DataFrame(['Job': problem.getJobs(),
                         'Machine': problem.getMachines(),
                         'Start': jo])


print('Job Schedule')
print(schedule.sort_values(by=['Job','Start']).set_index(['Job', 'Machine']))

print('Machine Schedule')
print(schedule.sort_values(by=['Machine','Start']).set_index(['Machine', 'Job']))