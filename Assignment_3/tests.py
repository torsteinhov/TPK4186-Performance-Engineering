'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''

from catalog import *
from cell import *
from client_order import *
from delivery import *
from printer import *
from product import *
from robot import *
from shelf import *
from simulator import *
from truck import *
from warehouse import *

import unittest


class Test(unittest.TestCase): 
    
    def __init__(self, catalog, product, robot, warehouse, truck):
        self.catalog = catalog
        self.product = product
        self.robot = robot
        self.warehouse = warehouse
        self.truck = truck

    #Setting up the warehouse(16x24)
    warehouse = Warehouse(height=16,width=24)
    warehouse.constructWarehouseLayout()
    
       
    def testGettersAndSetters(self):

        #Product
        product1 = Product()
        product2 = Product()
        product1.setSerialnr('SN007')
        product1.setWeight(7)
        product2.setSerialnr('SN008')
        product2.setWeight(10)
        self.assertEqual(product1.getSerialnr(),'SN007')
        self.assertEqual(product1.getWeight(), 7)
        self.assertEqual(product2.getSerialnr(),'SN008')
        self.assertEqual(product2.getWeight(), 10)

        #Catalog
        catalog = Catalog()
        catalog.setProducts([product1, product2])
        self.assertEqual(catalog.getProducts(),[product1, product2] ) #må kjøre for å se hva som kommer ut

        #Robot
        warehouse.addRobot(robot1)
        robot1 = Robot('XX-1')
        warehouse.addRobot(robot1)
        self.assertEqual(robot1.getId(), 'XX-1')
        robot1.setCurrPos([4,8])
        self.assertEqual(robot1.getCurrPos(), [4,8])
        #Want to move the robot from position[4,8] to [6,8]
        robot1.setRoute([[4,8],[5,8],[6,8]])
        robot1.getRoute([[4,8],[5,8],[6,8]])
        self.assertEqual(robot1.getCurrPos(), [4,8])
        self.assertEqual(robot1.getNextPos,[5,8]])
        self.assertEqual(robot1.getGoalPos, [6,8])
        robot1.moveRobot()
        self.assertEqual(robot1.getCurrPos(), [5,8])
        self.assertEqual(robot1.getNextPos,[6,8]])
        robot1.moveRobot()
        self.assertEqual(robot1.getCurrPos(), [6,8])

        robot1.setCurrPos([4,8])
        robot1.setGoalPos([7,8])
        self.assertEqual(robot1.getRoute(),[[4,8],[5,8],[6,8],[7,8]])

        

        robot1.setRobotAvailability(False)
        self.assertEqual(robot1.isAvailable(), False)
        robot1.setRobotAvailability(True)
        self.assertEqual(robot1.isAvailable(), True)




        self.assertEqual(robot1.getMaxCarry(), 40) #Må jeg ha self.maxCarry = 40 i init? 

        #Truck
        truck = Truck() 
        truck.addProduct(product1)
        self.assertEqual(truck.getWeight(), 7)
        truck.addProduct(product2)
        self.assertEqual(truck.getWeight(), 17)
        truck.removeProduct(product1)
        self.assertEqual(truck.getWeight(), 10)
        self.assertEqual(truck.notFull(), True)
        self.assertEqual(truck.removeProduct(product1), ValueError)
        self.assertEqual(truck.removeProduct(product2), None) #Usikker hva som kommer ut. Evt. True?

        #Warehouse
        catalog = warehouse.constructCatalog(warehouse.getAmountOfStorageCells()*2)







        

        


        













        






        
        

        




        #Client Order
        order = ClientOrder()




    #Setting up the warehouse(16x24)
    warehouse = Warehouse(height=16,width=24)
    warehouse.constructWarehouseLayout()

    #Print the warehouse
    printer = Printer(warehouse)
    printer.printWarehouseLayout()

    # Constructing a catalog
    # Since each shelf can only contain one product type, the catalog is restricted
    # by the size of the warehouse (amount of shelves = storage cells * 2)
    catalog = warehouse.constructCatalog(warehouse.getAmountOfStorageCells()*2)
    print('Printing the catalog'+ '\n'+str(warehouse.getCatalog()))

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
    warehouse.addRobot(robot1)
    warehouse.loadRobotFromQueue()

    print(f'The robot contains: {robot1.getProducts()}')
    print(f'This cell has coordinates: {warehouse.getLayout()[0][0].getX()}')

    print(warehouse.calculateRouteFromDelivery2Storage(robot1.getProducts()))








if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)