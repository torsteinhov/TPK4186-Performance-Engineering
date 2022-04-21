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
import numpy as np
from tabulate import tabulate


# handles the operation of the warehouse

warehouse = Warehouse(height=30,width=24)
warehouse.constructWarehouseLayout()
printer = Printer(warehouse)
printer.printWarehouseLayout()

# Constructing a catalog
# Since each shelf can only contain one product type, the catalog is restricted
# by the size of the warehouse
catalog = warehouse.constructCatalog(warehouse.getAmountOfStorageCells()*2)
print(warehouse.getCatalog())

# Assign each shelf with its product type
warehouse.assignShelves2ProductTypes()
# Testing a random storage shelf for its product serial number
print(warehouse.getLayout()[1][6].shelf1.getProductSerialNr())

# Initializing a first delivery
delivery = warehouse.constructRandomDelivery(catalog)
print(delivery)
print(warehouse.getAmountOfStorageCells())

# Initalizing a second delivery
# Inserting new products in the list of products delivered to the warehouse
delivery2 = warehouse.constructRandomDelivery(catalog)
deliveries = [delivery, delivery2]

# Putting the deliveries in a truck
truck = Truck(deliveries)
print(truck)


