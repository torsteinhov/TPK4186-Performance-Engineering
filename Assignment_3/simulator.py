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


# handles the operation of the warehouse

warehouse = Warehouse(height=30,width=24)
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
warehouse.getLayout()[0][2].setContainRobot(True)
warehouse.printWarehouseStatus()

# Creating a robot
robot1 = Robot('XX-1')
robot1.loadRobot(delivery[0])


'''# Initalizing a second delivery
# Inserting new products in the list of products delivered to the warehouse
delivery2 = warehouse.constructRandomDelivery(catalog)
print(delivery2)
deliveries = [delivery, delivery2]

# Putting the deliveries in a truck
truck = Truck(deliveries)
print(truck)'''


