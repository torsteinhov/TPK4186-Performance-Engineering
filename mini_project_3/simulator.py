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
import numpy as np
from tabulate import tabulate


# handles the operation of the warehouse

warehouse = Warehouse(height=8,width=12)
warehouse.constructWarehouseLayout()
printer = Printer(warehouse)
printer.printWarehouseLayout()