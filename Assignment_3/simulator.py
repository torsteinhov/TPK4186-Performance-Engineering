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
import time
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
print(f'{delivery}\n')
print(f'The amount of storage cells in the warehouse: {warehouse.getAmountOfStorageCells()}')
print('\n')


# Adds the delivery to the warehouse queue
warehouse.add2WarehouseQueue(delivery)

# Creating a robot
robots = warehouse.createRobots(3)
warehouse.addRobots(robots)
warehouse.loadRobotFromQueue()


print(f'The robot contains: {robots[0].getProducts()}')
print(f'The route for the robot to the shelf is: {warehouse.calculateRouteFromDelivery2Storage(robots[0].getProducts())}')
#print(f'The route for the robot back home is: {warehouse.calculateRouteHome()}')

def simulateLoadWarehouse(visualization=True):
    
    timer = 0

    while warehouse.getWarehouseQueue():
        layout = warehouse.getLayout()

        for robot in warehouse.getRobots():

            #print('Robot availability: ', robot.isRobotAvailable())
            #print('Robot route: ', robot.getRoute())
            if robot.isRobotAvailable():
                Print = False
                warehouse.loadRobotFromQueue()
                robot.setRobotAvailability(False)
                goal = warehouse.findGoalCellLoading(robot.getProducts())
                robot.setGoalPos(goal)
                route2shelf = warehouse.calculateRouteFromDelivery2Storage(robot.getProducts())
                robot.setRoute(route2shelf)
                robot.setGoing2Shelf(True)
                robot.setCurrPos(route2shelf[0])

            else:
                Print = True
                print('Robot route: ', robot.getRoute())

                if not robot.getRoute():
                    if robot.getGoing2Shelf():
                        shelf1 = layout[robot.getGoalPos()[1]-1][robot.getGoalPos()[0]-1].getShelf1()
                        shelf2 = layout[robot.getGoalPos()[1]-1][robot.getGoalPos()[0]-1].getShelf2()

                        if robot.getProducts()[0] == shelf1.getProductSerialNr():
                            robot.loadShelf(shelf1, robot.getProducts()[0], robot.getProducts()[1])
                            print(f'Shelf 1 now contains: {shelf1.getProductSerialNr()} - amount: {shelf1.getAmount()}')
                        elif robot.getProducts()[0] == shelf2.getProductSerialNr():
                            robot.loadShelf(shelf2, robot.getProducts()[0], robot.getProducts()[1])
                            print(f'Shelf 2 now contains: {shelf2.getProductSerialNr()} - amount: {shelf2.getAmount()}')

                        layout[robot.getLastPos()[1]-1][robot.getLastPos()[0]-1].setContainRobot(True)
                        robot.setGoing2Shelf(False)
                        robot.setGoingHome(True)
                        route2home=warehouse.calculateRouteHome(robot.getGoalPos())
                        robot.setRoute(route2home)

                    elif robot.getGoingHome():
                        # Do not want to print when we are already back at start
                        if robot.getGoingHome() and len(robot.getRoute())==0:
                            robot.setRobotAvailability(True)
                            break                        
                
                else:
                    move = robot.getRoute()[0]
                    if layout[move[1]-1][move[0]-1].getContainRobot():
                        continue
                    else:
                        move = robot.getRoute().pop(0)

                    if robot.getRoute():
                        layout[move[1]-1][move[0]-1].setContainRobot(True)
                        robot.setCurrPos(move)
                
        if Print:
            if visualization:
                warehouse.printWarehouseStatus()
            for row in layout:
                for cell in row:
                    cell.setContainRobot(False)

        timer += 1
        if visualization:
            time.sleep(0.1)
    return timer


def simulateRetrieveOrders(visualization=True):
    
    timer = 0

    while warehouse.getClientOrderQueue():
        layout = warehouse.getLayout()

        for robot in warehouse.getRobots():

            #print('Robot availability: ', robot.isRobotAvailable())
            #print('Robot route: ', robot.getRoute())
            if robot.isRobotAvailable():
                Print = False
                warehouse.loadRobotFromOrder()
                robot.setRobotAvailability(False)
                goal = warehouse.findGoalCellLoading(robot.getProducts())
                robot.setGoalPos(goal)
                route2shelf = warehouse.calculateRouteFromDelivery2Storage(robot.getProducts())
                robot.setRoute(route2shelf)
                robot.setGoing2Shelf(True)
                robot.setCurrPos(route2shelf[0])

            else:
                Print = True
                print('Robot route: ', robot.getRoute())

                if not robot.getRoute():
                    if robot.getGoing2Shelf():
                        shelf1 = layout[robot.getGoalPos()[1]-1][robot.getGoalPos()[0]-1].getShelf1()
                        shelf2 = layout[robot.getGoalPos()[1]-1][robot.getGoalPos()[0]-1].getShelf2()

                        if robot.getProducts()[0] == shelf1.getProductSerialNr():
                            robot.unloadShelf(shelf1, robot.getProducts()[0], robot.getProducts()[1])
                            print(f'Shelf 1 now contains: {shelf1.getProductSerialNr()} - amount: {shelf1.getAmount()}')
                        elif robot.getProducts()[0] == shelf2.getProductSerialNr():
                            robot.unloadShelf(shelf2, robot.getProducts()[0], robot.getProducts()[1])
                            print(f'Shelf 2 now contains: {shelf2.getProductSerialNr()} - amount: {shelf2.getAmount()}')

                        layout[robot.getLastPos()[1]-1][robot.getLastPos()[0]-1].setContainRobot(True)
                        robot.setGoing2Shelf(False)
                        robot.setGoingHome(True)
                        route2home=warehouse.calculateRouteHome(robot.getGoalPos())
                        robot.setRoute(route2home)

                    elif robot.getGoingHome():
                        # Do not want to print when we are already back at start
                        if robot.getGoingHome() and len(robot.getRoute())==0:
                            robot.setRobotAvailability(True)
                            break                        
                
                else:
                    move = robot.getRoute()[0]
                    if layout[move[1]-1][move[0]-1].getContainRobot():
                        continue
                    else:
                        move = robot.getRoute().pop(0)

                    if robot.getRoute():
                        layout[move[1]-1][move[0]-1].setContainRobot(True)
                        robot.setCurrPos(move)
                
        if Print:
            if visualization:
                warehouse.printWarehouseStatus()
            for row in layout:
                for cell in row:
                    cell.setContainRobot(False)

        timer += 1
        if visualization:
            time.sleep(0.1)
    return timer