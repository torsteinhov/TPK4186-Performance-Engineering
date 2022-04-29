'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
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


class Optimizer:

    def __init__(self):
        pass

    def createDifferentWarehouseSizes(self):

        warehouses = []
        # Minimum sizes for our optimization, we saw it as unreasonable to have a smaller warehouse.
        x = 10
        y = 12

        for i in range(10):

            x += 2*i
            if i%4 == 0:
                y += 6
            
            warehouse = Warehouse(x,y)
            warehouse.constructWarehouseLayout()
            warehouse.constructCatalog(warehouse.getAmountOfStorageCells()*2)
            warehouse.assignShelves2ProductTypes()
            warehouses.append(warehouse)
        
        return warehouses

    def optimizeWarehouseSizes(self):

        data = [] # [[# storage cells: elapsed loading time],...]
        warehouses = self.createDifferentWarehouseSizes()

        for warehouse in warehouses:

            storagecells = warehouse.getAmountOfStorageCells()

            # Wish to calculate the average of 100 deliveries to get accurate measurements (power of randomness)
            loadtimeList = []
            for i in range(100):
                delivery = warehouse.constructRandomDelivery(warehouse.getCatalog())
                warehouse.add2WarehouseQueue(delivery)
                time2Load = simulateLoadWarehouse(visualization=False, printRoute=False)
                loadtimeList.append(time2Load)
                warehouse.setWarehouseQueue([])
            
            avgLoadTime = sum(loadtimeList)/len(loadtimeList)

            data.append([storagecells, avgLoadTime])

        return data

optimizer = Optimizer()
print(optimizer.optimizeWarehouseSizes())