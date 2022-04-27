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
import numpy as np
from tabulate import tabulate
from threading import Timer


# handles the operation of the warehouse

# sets the height and width of the warehouse
warehouse = Warehouse(height=16,width=24)
# constructs the layout
warehouse.constructWarehouseLayout()
printer = Printer(warehouse)
printer.printWarehouseLayout()

# Constructing a catalog
# Since each shelf can only contain one product type, the catalog is restricted
# by the size of the warehouse (amount of shelves = storage cells * 2)
catalog = warehouse.constructCatalog(warehouse.getAmountOfStorageCells()*2)
print(warehouse.getCatalog())

# Assign each shelf with its product type
warehouse.assignShelves2ProductTypes()
# Testing a random storage shelf for its product serial number
print(f'Checking the serialnr of a storage shelf: {warehouse.getLayout()[1][6].shelf1.getProductSerialNr()}')
print('\n')

# Initializing a first delivery
delivery = warehouse.constructRandomDelivery(catalog)
print(delivery)
print(f'The amount of storage cells in the warehouse: {warehouse.getAmountOfStorageCells()}')
print('\n')

# Adds the delivery to the warehouse queue
warehouse.add2WarehouseQueue(delivery)

# Testing to set a cell to contain a robot
'''warehouse.getLayout()[0][2].setContainRobot(True)
warehouse.printWarehouseStatus()'''

# Creating a robot
robot1 = Robot('XX-1')
warehouse.addRobot(robot1)
warehouse.loadRobotFromQueue()

print(f'The robot contains: {robot1.getProducts()}')
print(f'The route for the robot to the shelf is: {warehouse.calculateRouteFromDelivery2Storage(robot1.getProducts())}')
print(f'The route for the robot back home is: {warehouse.calculateRouteHome(robot1.getProducts())}')

def simulateLoadWarehouse():

    layout = warehouse.getLayout()

    robots = [robot1]
    for robot in robots:
        if robot.isRobotAvailable():
            warehouse.loadRobotFromQueue()
            robot.setRobotAvailability(False)
            goal = warehouse.findGoalCellLoading(robot.getProducts())
            route2shelf = warehouse.calculateRouteFromDelivery2Storage(robot.getProducts())
            robot.setCurrPos(route2shelf[0])
    
    for move in route2shelf:

        layout[move[1]-1][move[0]-1].setContainRobot(True)
        robot.setCurrPos(move)
        warehouse.printWarehouseStatus()
        layout[move[1]-1][move[0]-1].setContainRobot(False)

        if move == route2shelf[-1]:
            

            shelf1 = layout[goal[1]][goal[0]].getShelf1()
            shelf2 = layout[goal[1]][goal[0]].getShelf2()

            print('robot.getProducts()', robot.getProducts())
            if robot.getProducts()[0] == shelf1.getProductSerialNr():
                robot.loadShelf(shelf1, robot.getProducts()[0], robot.getProducts()[1])
                print(f'Shelf 1 now contains: {shelf1.getProductSerialNr()} - amount: {shelf2.getAmount()}')
            else:
                robot.loadShelf(shelf2, robot.getProducts()[0], robot.getProducts()[1])
                print(f'Shelf 2 now contains: {shelf2.getProductSerialNr()} - amount: {shelf2.getAmount()}')

            

simulateLoadWarehouse()

    #Timer(1, simulateLoadWarehouse).start()