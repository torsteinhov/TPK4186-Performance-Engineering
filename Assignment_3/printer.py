'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''

from warehouse import Warehouse
from catalog import *
from cell import *
from product import *
from delivery import *
from shelf import *
import numpy as np
from tabulate import tabulate

class Printer:

    """
    A class used to print different operations/status in the warehouse
    ...

    Attributes
    ----------
    warehouse : warehouse object
        a warehouse object
    layout: 2D list
        2D list of the warehouse
    
    Methods
    -------
    printWarehouseLayoutRAW()
        for troubleshooting when creating the warehouse layout. Prints out coordinates and cell type in a readable format
    printWarehouseLayout()
        prints the warehouse layout
    printCatalog(catalog)
        prints the catalog
    printRobot(robot)
        prints the robot
    """

    def __init__(self, warehouse):
        self.warehouse = warehouse
        self.layout = warehouse.constructWarehouseLayout()
    
    def printWarehouseLayoutRAW(self):
        
        for row in self.layout:
            print('\n')

            for cell in row:
                print('x: ', cell.x, ' y: ', cell.y, ' type: ', cell.type)
    
    def printWarehouseLayout(self):
        
        grid = []
        for row in self.layout:
            row_grid = []
            for cell in row:
                if cell.type == 'route':
                    row_grid.append(cell.getRoute())
                else:
                    row_grid.append(cell.getType())
            
            grid.append(row_grid)
        
        print(tabulate(grid, tablefmt='fancy_grid'))
    
    def printCatalog(self, catalog):
        print(catalog)
    
    def printRobot(self, robot):
        print(robot)