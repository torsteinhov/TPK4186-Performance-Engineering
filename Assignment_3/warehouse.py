# A file that holds the Warehouse class with all its associated data structures from data_models
# and create/manage functions for each of those classes.
'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''

from catalog import *
from cell import *
from product import *
from delivery import *
from shelf import *
from numpy import product
from datetime import datetime
from math import floor 
import random
from tabulate import tabulate

class Warehouse:

    def __init__(self, height, width, catalog=None, robots=[], layout=None, warehouseQueue=[]):
        self.catalog = catalog
        self.robots = robots
        self.layout = layout
        self.height = height
        self.width = width
        self.warehouseQueue = warehouseQueue
    
    def getCatalog(self):
        return self.catalog
    
    def setCatalog(self, catalog):
        self.catalog = catalog
    
    def getRobots(self):
        return self.robots
    
    def addRobot(self, robot):
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
    
    def add2WarehouseQueue(self, delivery):
        #self.warehouseQueue.update(delivery)
        for product, amount in delivery.getProducts().items():
            delivery_list = [product, amount]
            self.getWarehouseQueue().append(delivery_list)

    def add_product(self, product):
        # Takes a product and adds it in the catalog
        if product not in self.catalog:
            self.catalog.getProducts().append(product)
    
    def remove_product(self, product):
        # Takes a product and removes it from the catalog
        if product in self.catalog:
            self.catalog.getProducts().remove(product)
    
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

    def constructRandomDelivery(self, catalog):

        truck_max = 20000
        delivery_cap = min(self.getAmountOfStorageCells()*200, truck_max)
        products = {}
        # We assume a random delivery containing between 5-10 different products.
        # We also assume that each 
        # Creating a random delivery in itself does not make much sense, but we have tried to mimic its intentions.
        n_products = random.randint(10,20)

        # We also assume equal weight for each product
        weight_per_product_type = 100

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
                    row_grid.append('')
                elif cell.getType() == 'loading':
                    row_grid.append('-')
                elif cell.getType() == 'storage':
                    row_grid.append('S')
            
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

        
        return route
    
    def calculateRouteHome(self, product):
        # start = [x,y]

        # Calculates the start cell, which is the loading cell to the shelf that corresponds with the product the robot holds.
        start = self.findGoalCellLoading(product)
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