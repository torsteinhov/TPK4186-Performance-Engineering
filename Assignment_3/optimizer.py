'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''

'''
RUNNING THIS PROGRAM MAY TAKE 1 MINUTE BECAUSE OF ALL THE CALCULATIONS, PLEASE BE PATIENT :)
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
import numpy as np
import matplotlib.pyplot as plt


"""
    The class allows the user to explore with different variables to optimize the operation of the warehouse.
    ...
    
    Methods
    -------
    createDifferentWarehouseSizes()
        creates different warehouse layouts within the boundaries that are set for a warehouse.
        Logic operations such as constructing the layout, constructing the catalog and assigning each shelf
        to a product type is also performed.
    optimizeWarehouseSizes(n_robots)
        iterates through warehouses (NUMBER_OF_WAREHOUSES) and perform all necessary logic operations such as creating
        a random delivery, adding it to the warehousequeue, creating robots and adding them to the warehouse.
        Running the simulation of loading the warehouse with the robots (without visualization) and then adding the elapsed time
        to a list, after this is done 50 times we calculate the average elapsed time and adds to a list that is returned with
        the corresponding results from the other warehouses aswell (with other sizes).
    visualizeWarehousesizeVSLoadingtime(n_robots)
        Takes the result from optimizeWarehouseSizes() and plots it in a line diagram to show the correlation
        between the size of the warehouse and elapsed time when loading the warehouse from deliveries.
    """




'''Here you can change the number of robots and warehouses for the otimization:'''

NUMBER_OF_ROBOTS = 3
NUMBER_OF_WAREHOUSES = 10

class Optimizer:

    def __init__(self):
        pass

    def createDifferentWarehouseSizes(self):

        warehouses = []
        # Minimum sizes for our optimization, we saw it as unreasonable to have a smaller warehouse.
        x = 12
        y = 20

        #The number of warehouses
        for i in range(NUMBER_OF_WAREHOUSES):

            y += 2*i
            if i%4 == 0:
                x += 6
            
            warehouse = Warehouse(y,x)
            warehouse.constructWarehouseLayout()
            warehouse.constructCatalog(warehouse.getAmountOfStorageCells()*2)
            warehouse.assignShelves2ProductTypes()
            warehouses.append(warehouse)
        
        return warehouses

    def optimizeWarehouseSizes(self, n_robots):

        data = [] # [[# storage cells: elapsed loading time],...]
        warehouses = self.createDifferentWarehouseSizes()

        for warehouse in warehouses:
            printer = Printer(warehouse)

            '''Uncomment to print out the different warehouse layouts'''
            #printer.printWarehouseLayout()
            storagecells = warehouse.getAmountOfStorageCells()

            # Wish to calculate the average of 50 deliveries to get accurate measurements (power of randomness)
            loadtimeList = []
            for i in range(50):
                delivery = warehouse.constructRandomDelivery(warehouse.getCatalog())
                warehouse.add2WarehouseQueue(delivery)
                robots = warehouse.createRobots(n_robots)
                warehouse.addRobots(robots)
                time2Load = simulateLoadWarehouse(visualization=False, printRoute=False, warehouse=warehouse)
                loadtimeList.append(time2Load)
                warehouse.setWarehouseQueue([])
                warehouse.setRobots([])
            
            avgLoadTime = sum(loadtimeList)/len(loadtimeList)

            data.append([storagecells, avgLoadTime])

        return data
    
    def visualizeWarehousesizeVSLoadingtime(self, n_robots):

        data = optimizer.optimizeWarehouseSizes(n_robots)

        for point in data:
            print(f'Storage cells: {point[0]}   -   Elapsed time: {point[1]}\n')
        
        storageCells=[]
        time=[]
        for datapoint in data:
            storageCells.append(datapoint[0])
            time.append(datapoint[1])
        fig = plt.figure(figsize = (10, 5))
        plt.plot(storageCells, time, color ='maroon')
        plt.xlabel("Number of storage cells in the warehouse")
        plt.ylabel("Number of seconds to fill the warehouse ")
        plt.title("Warehouse size vs time to fill the warehouse, number of robots = {}.".format(n_robots))
        plt.show()



optimizer = Optimizer()
optimizer.visualizeWarehousesizeVSLoadingtime(NUMBER_OF_ROBOTS)