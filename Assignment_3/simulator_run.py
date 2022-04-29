'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''

'''
This program is for you to run the different functions, and therefore operations of the warehouse,
this is done by uncommenting a line and run the program.

First you have to run the simulator.py file, this will preview the creation of all the logistics inside
the warehouse. With logistics we mean creation of layout, catalog, client orders, deliveries, robots etc..)

'''

from catalog import *
from warehouse import *
from cell import *
from product import *
from delivery import *
from shelf import *
from printer import *
from truck import *
from robot import *
from simulator import *
import numpy as np
import time
from tabulate import tabulate
from threading import Timer

'''Simulate the loading of the warehouse'''
print(simulateLoadWarehouse(visualization=True))

# Initialize the first client order
clientOrder = warehouse.constructRandomClientOrder(catalog)
print(f'{clientOrder}\n')

time.sleep(3)
# Adds the client order to the client order queue
warehouse.add2ClientOrderQueue(clientOrder)

'''Simulate the robots retrieving client orders'''
print(simulateRetrieveOrders(visualization=True))