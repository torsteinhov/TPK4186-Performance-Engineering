# A file that holds the Warehouse class with all its associated data structures from data_models
# and create/manage functions for each of those classes.
'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''

from catalog import *
from cell import *
from client_order import ClientOrder
from product import *
from delivery import *
from shelf import *
from numpy import product
from robot import *
from datetime import datetime
from math import floor 
import random
from tabulate import tabulate

class Warehouse:

    """
    A class that represents the warehouse which contains all the other data models within the warehouse.
    This class also has all the methods that creates data for all the simulation and optimization.
    ...

    Attributes
    ----------
    catalog : list
        A list with all the different products that exist in the warehouse
    robots: list
        A list of all the robots within the warehouse
    layout : 2D list
        A datastructure that holds the layout of the warehouse with all corresponding cells
    height: int 
        The height of the warehouse (y-value)
    width : int
        The width of the warehouse (x-value)
    warehouseQueue: list
        A list of all deliveries that is coming into the warehouse
    clientOrderQueue : list
        A list of all client orders waiting for robots in the warehouse
    
    
    Methods
    -------
    getCatalog()
        gets the catalog of the warehouse
    setCatalog(catalog)
        sets the catalog for the warehouse
    getRobots()
        gets the robots in the warehouse
    setRobots()
        sets the robots in the warehouse
    addRobots(n_robots)
        Adds robots to the warehouse
    getLayout()
        Gets the layout of the warehouse
    setLayout()
        Sets the layout of the warehouse
    getHeight()
        Gets the height of the warehouse
    getWidth()
        Gets the width of the warehouse
    getWarehouseQueue()
        Gets the warehouse queue
    setWarehouseQueue()
        Sets the warehouse queue
    getClientOrderQueue()
        Gets the client order queue
    setClientOrderQueue()
        Sets the client order queue
    add2WarehouseQueue()
        Adds a delivery to the warehouse queue
    add2ClientOrderQueue()
        Adds a client order to the client order queue
    add_product()
        Adds a product to the catalog
    remove_product()
        Removes a product from the catalog
    constructCatalog()
        Constructs a catalog of different products with their own serial numbers based on the size of the warehouse.
    constructRandomDelivery()
        Constructs a random delivery based of the catalog of the warehouse, therefore deliveries can only contain
        products that fits in the warehouse.
    constructRandomClientOrder()
        Constructs a random client order based of the catalog of the warehouse. It is also checked whether the products
        exist in the warehouse. We did not create a ValueError here since we thought that assuming that the warehouse has
        what the client has ordered is a reasonable assumption.
    constructWarehouseLayout()
        Constructs the layout of the warehouse based of the height and width of the warehouse. We have based the construction
        off of basic logic with operators such as +,- and % to get the layout correct. It is also added the correct type
        of Cell based on where the Cell lies.
    getAmountOfStorageCells()
        Iterates through the layout of the warehouse (all cells) and returns the amount of storage cells, if you multiply this number
        by 2, which is done throughout the project, you get the amount of storage SHELVES.
    assignShelves2ProductTypes()
        Iterates through the layout of the warehouse (all cells) and assign each shelf a specific product type with a
        corresponding serial number. This assignment is based off the catalog which again is based of the size of the warehouse, 
        therefore all shelves will be assigned a product type.
    printWarehouseStatus()
        Prints out a more visual friendly status of the warehouse.
    getAvailableRobot()
        Checks the robots list for available robots.
    loadRobotFromQueue()
        Unloads the robot with products from the warehouse when the robot is in the corresponding storage cell and correct shelf.
        To deliver from trucks to the shelves.
    loadRobotFromOrder()
        Loads the robot with products from the warehouse when the robot is in the corresponding storage cell and correct shelf.
        To retrieve for the customer.
    findGoalCellLoading(products)
        Takes in a product and finds the correct storage cell within the warehouse, and the correct shelf within the storage cell.
    calculateRouteFromDelivery2Storage()
        Calculates the route for the robot from the delivery depot (trucks) to the correct storage cell and sets the route for the robot.
    calculateRouteHome()
        Calculates the route for the robot from the storage cell to the delivery depot and sets the route for the robot.
    createRobots(n_robots)
        Creates n amount of robots and sets them to be assigned to the warehouse.

    """

    def __init__(self, height, width, catalog=None, robots=[], layout=None, warehouseQueue=[], clientOrderQueue=[]):
        self.catalog = catalog
        self.robots = robots
        self.layout = layout
        self.height = height
        self.width = width
        self.warehouseQueue = warehouseQueue
        self.clientOrderQueue = clientOrderQueue
    
    def getCatalog(self):
        return self.catalog
    
    def setCatalog(self, catalog):
        self.catalog = catalog
    
    def getRobots(self):
        return self.robots
    
    def setRobots(self, robots):
        self.robots = robots
    
    def addRobots(self, robots):
        for robot in robots:
            self.robots.append(robot)
    
    def getLayout(self):
        return self.layout
    
    def setLayout(self, layout):
        self.layout = layout

    def getHeight(self):
        return self.height
    
    def getWidth(self):
        return self.width
    
    def getWarehouseQueue(self):
        return self.warehouseQueue
    
    def setWarehouseQueue(self, warehouseQueue):
        self.warehouseQueue = warehouseQueue
    
    def getClientOrderQueue(self):
        return self.clientOrderQueue
    
    def setClientOrderQueue(self, clientOrderQueue):
        self.clientOrderQueue = clientOrderQueue
    
    def add2WarehouseQueue(self, delivery):

        # Iterates through the delivery dictionary to add products to the queue for loading
        for product, amount in delivery.getProducts().items():
            delivery_list = [product, amount]
            self.getWarehouseQueue().append(delivery_list)
    
    def add2ClientOrderQueue(self, clientOrder):

        # Iterates through the client order dictionary to add products to the queue for retrieving
        for product, amount in clientOrder.getOrder().items():
            clientOrder_list = [product, amount]
            self.getClientOrderQueue().append(clientOrder_list)

    def add_product(self, product):
        # Takes a product and adds it in the catalog
        if product not in self.catalog:
            self.catalog.getProducts().append(product)
    
    def remove_product(self, product):
        # Takes a product and removes it from the catalog
        if product in self.catalog:
            self.catalog.getProducts().remove(product)
    
    
    ''' TASK 2: From here and downwards we have many functions that creates deliveries, client orders, warehouse layout etc..'''

    def constructCatalog(self, n):

        products = []
        percentageSmallProducts = 0.7 # We assume that 70% of the products weigh between 2-10 kg.
        

        for i in range(1,n+1):
            serialnr = 'SN' + str(i)
            
            
            if i <= floor(n*percentageSmallProducts):
                weight = random.randint(2,10)
            else:
                weight = random.randint(11,40)
            
            product = Product(serialnr, weight)
            products.append(product)
        
        catalog = Catalog(products)
        self.setCatalog(catalog)
        return catalog

    ''' TASK 2: From here and downwards we have many functions that creates deliveries, client orders, warehouse layout etc..'''

    def constructRandomDelivery(self, catalog):

        truck_max = 20000
        delivery_cap = min(self.getAmountOfStorageCells()*200, truck_max)
        products = {}
        # We assume a random delivery containing between 5-10 different products.
        # We also assume that each 
        # Creating a random delivery in itself does not make much sense, but we have tried to mimic its intentions.
        n_products = random.randint(10,20)

        # We also assume equal weight for each product
        weight_per_product_type = 40

        delivery_weight = 0
        for i in range(n_products):

            
            # We need to make sure that the weight of the delivery does not exceed the maximum capacity of the warehouse and the truck
            # This relates mostly to products of heavy weight.
            if delivery_weight > delivery_cap:
                break

            else:
                index = random.randint(0, len(catalog.getProducts())-1)
                product = catalog.getProducts()[index]
                
                amount = floor(weight_per_product_type/product.getWeight())

                products[product] = amount
                delivery_weight += product.getWeight()
        
        delivery = Delivery(products)
        return delivery
    
    def constructRandomClientOrder(self, catalog):

        # Set the warehouse cap to be amount of storage cells * 200 (2 shelves * 100 kg)
        warehouse_cap = self.getAmountOfStorageCells()*200
        products = {}

        n_products = random.randint(3,8)

        order_weight = 0
        while len(products) < n_products:

            weight_per_product_type = random.randint(20, 100)
            existInWarehouse = False
            
            # We need to make sure that the weight of the client order does not exceed the maximum capacity of the warehouse
            # This relates mostly to products of heavy weight.
            if order_weight > warehouse_cap:
                break

            else:
                index = random.randint(0, len(catalog.getProducts())-1)
                product = catalog.getProducts()[index]
                
                amount = floor(weight_per_product_type/product.getWeight())

                for row in self.getLayout():
                    for cell in row:
                        if cell.getType() == 'storage':
                            if cell.getShelf1().getProductSerialNr() == product.getSerialnr() or cell.getShelf2().getProductSerialNr() == product.getSerialnr():
                                existInWarehouse = True

                if existInWarehouse:
                    products[product] = amount
                    order_weight += product.getWeight()
        
        order = ClientOrder(products)
        return order
        

    def constructWarehouseLayout(self):
        
        '''
        Assumptions:    minimum 6width6 cells.
                        each increase in width(width) must be in whole sections (6 cells).
                        height(height) must be minimum 6 cells.
                        each increase in height(height) must be in pairs (2 cells).
        '''

        if self.width%6 != 0:
            raise ValueError("width(width) must be in whole sections (6 cells)")
        
        if self.width < 6 or self.height < 6:
            raise ValueError("Warehouse is too small, must be atleast 6width6 cells")
        
        if self.height%2 != 0:
            raise ValueError("height(height) must be in pairs")
        
        numberofsections=self.width/6
        sectiondebt=(self.height-4)//2

        layout = []

        # top aisle
        #topAisle = [[] for _ in range(sectiondebt)]

        for j in range(1, sectiondebt+1):
            topAisle = []
            for i in range(1,self.width+1):
                if (i-3)%6 == 0:
                    topAisle.append(Cell(x=i,y=j, type='route' , route='up'))
                elif (i-4)%6 == 0:
                    topAisle.append(Cell(x=i,y=j, type='route' , route='down'))
                elif (i-1)%6 == 0:
                    topAisle.append(Cell(x=i,y=j, type='storage', shelf1=Shelf(), shelf2=Shelf()))
                elif (i-6)%6 == 0:
                    topAisle.append(Cell(x=i,y=j, type='storage', shelf1=Shelf(), shelf2=Shelf()))
                else:
                    topAisle.append(Cell(x=i,y=j, type='loading'))
            
            layout.append(topAisle)

        # Construct middle section
        
        # top
        top = []
        for i in range(1, self.width+1):
            if (i-3)%6 == 0:
                top.append(Cell(x=i,y=int((self.height/2)-1), type='route' , route='up'))
            elif (i-4)%6 == 0:
                top.append(Cell(x=i,y=int((self.height/2)-1), type='route' , route='down'))
            else:
                top.append(Cell(x=i,y=int((self.height/2)-1), type='loading'))
        
        layout.append(top)

        # midtop
        midtop = []
        for i in range(1, self.width+1):
            if i!=self.width and i!=self.width-1:
                midtop.append(Cell(x=i,y=int(self.height/2), type='route' , route='right'))
            else:
                midtop.append(Cell(x=i,y=int(self.height/2), type='none'))
        
        layout.append(midtop)

        # midbot
        midbot = []
        for i in range(1, self.width+1):
            if i!=self.width and i!=self.width-1:
                midbot.append(Cell(x=i,y=int((self.height/2)+1), type='route' , route='left'))
            else:
                midbot.append(Cell(x=i,y=int((self.height/2)+1), type='none'))
        
        layout.append(midbot)
        
        # bot
        bot = []
        for i in range(1, self.width+1):
            if (i-3)%6 == 0:
                bot.append(Cell(x=i,y=int((self.height/2)+2), type='route' , route='down'))
            elif (i-4)%6 == 0:
                bot.append(Cell(x=i,y=int((self.height/2)+2), type='route' , route='up'))
            else:
                bot.append(Cell(x=i,y=int((self.height/2)+2), type='loading'))
        
        layout.append(bot)

        # bottom aisle
        for j in range(1, sectiondebt+1):
            botAisle = []
            for i in range(1,self.width+1):
                if (i-3)%6 == 0:
                    botAisle.append(Cell(x=i,y=j+sectiondebt+4, type='route' , route='down'))
                elif (i-4)%6 == 0:
                    botAisle.append(Cell(x=i,y=j+sectiondebt+4, type='route' , route='up'))
                elif (i-1)%6 == 0:
                    botAisle.append(Cell(x=i,y=j+sectiondebt+4, type='storage', shelf1=Shelf(), shelf2=Shelf()))
                elif (i-6)%6 == 0:
                    botAisle.append(Cell(x=i,y=j+sectiondebt+4, type='storage', shelf1=Shelf(), shelf2=Shelf()))
                else:
                    botAisle.append(Cell(x=i,y=j+sectiondebt+4, type='loading'))
            
            layout.append(botAisle)

        self.setLayout(layout)
        return layout
    
    def getAmountOfStorageCells(self):

        storagecells = 0

        for row in self.layout:
            for cell in row:
                if cell.getType() == 'storage':
                    storagecells += 1
        
        return storagecells
    
    def assignShelves2ProductTypes(self):
        
        serialNrCount = 0
        for row in self.layout:
            for cell in row:
                if cell.getType() == 'storage':
                    cell.shelf1.setProductSerialNr(str(self.getCatalog().getProducts()[serialNrCount].getSerialnr()))
                    cell.shelf2.setProductSerialNr(str(self.getCatalog().getProducts()[serialNrCount+1].getSerialnr()))
                    serialNrCount += 2
    
    def printWarehouseStatus(self):
        
        grid = []
        for row in self.layout:
            row_grid = []
            for cell in row:
                if cell.getContainRobot() == True:
                    row_grid.append('웃')
                elif cell.getType() == 'route':
                    row_grid.append('  ')
                elif cell.getType() == 'loading':
                    row_grid.append(' -')
                elif cell.getType() == 'storage':
                    row_grid.append('☐')
            
            grid.append(row_grid)
        
        print(tabulate(grid, tablefmt='fancy_grid'))
    
    def getAvailableRobot(self):
        for robot in self.robots:
            if robot.isRobotAvailable():
                return robot
        
        print('No available robots!')

    # We take a product from the warehouse queue, which is loaded from deliveries and load our robot with the products,
    # the warehouse queue is then updated.
    def loadRobotFromQueue(self):
        robot = self.getAvailableRobot()
        loading_delivery = self.warehouseQueue[0]
        product_weight = loading_delivery[0].getWeight()
        cap_robot_products = floor(robot.getMaxCarry()/product_weight)

        if loading_delivery[1] > cap_robot_products:
            loading_delivery[1] -= cap_robot_products
            robot.loadRobot(loading_delivery[0].getSerialnr(), cap_robot_products)
        else:
            self.warehouseQueue.pop(0)
            robot.loadRobot(loading_delivery[0].getSerialnr(), loading_delivery[1])
        
    
    # We retrieve a product from the client order queue and adds it to the robot,
    # The client order queue is then updated
    def loadRobotFromOrder(self):
        robot = self.getAvailableRobot()
        loading_order = self.clientOrderQueue[0]
        product_weight = loading_order[0].getWeight()
        cap_robot_products = floor(robot.getMaxCarry()/product_weight)

        if loading_order[1] > cap_robot_products:
            loading_order[1] -= cap_robot_products
            robot.loadRobot(loading_order[0].getSerialnr(), cap_robot_products)
        else:
            self.clientOrderQueue.pop(0)
            robot.loadRobot(loading_order[0].getSerialnr(), loading_order[1])
    
    # Finds the shelf for the specific product in the warehouse
    def findGoalCellLoading(self, product):
        
        x, y = 0,0
        for row in self.layout:
            for cell in row:
                if cell.getType() == 'storage':
                    if cell.getShelf1().getProductSerialNr() == product[0]:
                        x = cell.getX()
                        y = cell.getY()
                    elif cell.getShelf2().getProductSerialNr() == product[0]:
                        x = cell.getX()
                        y = cell.getY()

        return [x,y]
    
    def calculateRouteFromDelivery2Storage(self, product):

        route = []
        goal = self.findGoalCellLoading(product)
        start_y = int(len(self.layout)/2)

        # Find the amount of moves along the x-axis
        for i in range(6, len(self.layout[0])+1, 6):
            if goal[0] <= i:
                stop_x = i-3
                # Add the moves to the route
                for x in range(1, stop_x+1):
                    route.append([x, start_y])
                break
        
        
        # Find the amount of moves along the y-axis and add the moves to the route
        if goal[1] < start_y:
            for i in range(start_y-1, goal[1]-1, -1):
                route.append([stop_x, i])
        else:
            for i in range(start_y+1, goal[1]+1, 1):
                route.append([stop_x, i])
        
        # Move from the transportation cells in to the loading cell
        if goal[0] < route[-1][0]:
            route.append([route[-1][0]-1, route[-1][1]])
        else:
            route.append([route[-1][0]+1, route[-1][1]])
            route.append([route[-1][0]+1, route[-1][1]])

        # Need to add 12 times the last route to simulate that loading takes 120 seconds.
        for i in range(12):
            route.append(route[-1])

        return route
    
    def calculateRouteHome(self, start):
        # start = [x,y]

        # Calculates the start cell, which is the loading cell to the shelf that corresponds with the product the robot holds.
        end_y = int(len(self.layout)/2)+1
        route = []

        # Route from loading cell to transportation cell
        if ((start[0]-1)%6) == 0:
            route.append([start[0]+2, start[1]])
            route.append([start[0]+3, start[1]])
        else:
            route.append([start[0]-2, start[1]])
        
        # Route from storage aisle to mid aisle
        if start[1] < end_y:
            for i in range(start[1]+1, end_y+1, 1):
                route.append([route[-1][0], i])
        else:
            for i in range(start[1]-1, end_y-1, -1):
                route.append([route[-1][0], i])
        
        # Route from mid aisle to home
        for i in range(route[-1][0]-1, -1, -1):
            route.append([i, route[-1][1]])
        
        return route
    
    def createRobots(self, n_robots):

        robots = []
        for i in range(1, n_robots+1):
            id = 'XX-'+str(i)
            robots.append(Robot(id))

        return robots