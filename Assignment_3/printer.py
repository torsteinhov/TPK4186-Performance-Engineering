from warehouse import Warehouse
from data_models import Robot
import numpy as np
from tabulate import tabulate

class Printer:

    def __init__(self, warehouse, x, y):
        self.warehouse = warehouse
        self.layout = warehouse.constructWarehouseLayout(x, y)
    
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
    


warehouse = Warehouse()
catalog = warehouse.constructCatalog(120)
products = catalog.getProducts()
print(products)
robot = Robot(1, (2,3), (5,5), products)
warehouse.setCatalog(catalog)
warehouse.setRobots(robot)
printer = Printer(warehouse, 24, 16)
printer.printWarehouseLayout()
printer.printCatalog(warehouse.getCatalog())
printer.printRobot(warehouse.getRobots())