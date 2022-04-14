# A file that holds the Warehouse class with all its associated data structures from data_models
# and create/manage functions for each of those classes.
'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''

from email.errors import MissingHeaderBodySeparatorDefect
from data_models import Catalog, Cell, Product, Delivery
from winreg import DisableReflectionKey
from numpy import product
from datetime import datetime
from math import floor 
import random   

class Warehouse:

    def __init__(self, catalog=None, robots=None):
        self.catalog = catalog
        self.robots = robots
    
    def getCatalog(self):
        return self.catalog
    
    def setCatalog(self, catalog):
        self.catalog = catalog
    
    def getRobots(self):
        return self.robots
    
    def setRobots(self, robots):
        self.robots = robots

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
        return catalog

    def constructRandomTruckDelivery(self, catalog, max_weight=20000):

        products = {}
        # We assume a random delivery containing between 5-10 different products.
        # Creating a random delivery in itself does not make much sense, but we have tried to mimic its intentions.
        n_products = random.randint(5,10)

        # We also assume equal weight for each product
        weight_per_product_type = max_weight/n_products

        for i in range(n_products):
            index = random.randint(0, len(catalog.getProducts())-1)
            product = catalog.getProducts()[index]
            amount = floor(weight_per_product_type/product.getWeight())

            products[product] = amount
        
        delivery = Delivery(products)
        return delivery

    def constructWarehouseLayout(self, x, y):
        
        '''
        Assumptions:    minimum 6x6 cells.
                        each increase in x(width) must be in whole sections (6 cells).
                        y(height) must be minimum 6 cells.
                        each increase in y(height) must be in pairs (2 cells).
        '''

        if x%6 != 0:
            raise ValueError("x(width) must be in whole sections (6 cells)")
        
        if x < 6 or y < 6:
            raise ValueError("Warehouse is too small, must be atleast 6x6 cells")
        
        if y%2 != 0:
            raise ValueError("y(height) must be in pairs")
        
        numberofsections=x/6
        sectiondebt=(y-4)//2

        layout = []

        # top aisle
        #topAisle = [[] for _ in range(sectiondebt)]

        for j in range(1, sectiondebt+1):
            topAisle = []
            for i in range(1,x+1):
                if (i-3)%6 == 0:
                    topAisle.append(Cell(x=i,y=j, type='route' , route='up'))
                elif (i-4)%6 == 0:
                    topAisle.append(Cell(x=i,y=j, type='route' , route='down'))
                elif (i-1)%6 == 0:
                    topAisle.append(Cell(x=i,y=j, type='shelf'))
                elif (i-6)%6 == 0:
                    topAisle.append(Cell(x=i,y=j, type='shelf'))
                else:
                    topAisle.append(Cell(x=i,y=j, type='loading'))
            
            layout.append(topAisle)

        # Construct middle section
        
        # top
        top = []
        for i in range(1, x+1):
            if (i-3)%6 == 0:
                top.append(Cell(x=i,y=int((y/2)-1), type='route' , route='up'))
            elif (i-4)%6 == 0:
                top.append(Cell(x=i,y=int((y/2)-1), type='route' , route='down'))
            else:
                top.append(Cell(x=i,y=int((y/2)-1), type='loading'))
        
        layout.append(top)

        # midtop
        midtop = []
        for i in range(1, x+1):
            if i!=x and i!=x-1:
                midtop.append(Cell(x=i,y=int(y/2), type='route' , route='right'))
            else:
                midtop.append(Cell(x=i,y=int(y/2), type='none'))
        
        layout.append(midtop)

        # midbot
        midbot = []
        for i in range(1, x+1):
            if i!=x and i!=x-1:
                midbot.append(Cell(x=i,y=int((y/2)+1), type='route' , route='left'))
            else:
                midbot.append(Cell(x=i,y=int((y/2)+1), type='none'))
        
        layout.append(midbot)
        
        # bot
        bot = []
        for i in range(1, x+1):
            if (i-3)%6 == 0:
                bot.append(Cell(x=i,y=int((y/2)+2), type='route' , route='down'))
            elif (i-4)%6 == 0:
                bot.append(Cell(x=i,y=int((y/2)+2), type='route' , route='up'))
            else:
                bot.append(Cell(x=i,y=int((y/2)+2), type='loading'))
        
        layout.append(bot)

        # bottom aisle
        for j in range(1, sectiondebt+1):
            botAisle = []
            for i in range(1,x+1):
                if (i-3)%6 == 0:
                    botAisle.append(Cell(x=i,y=j+sectiondebt+4, type='route' , route='down'))
                elif (i-4)%6 == 0:
                    botAisle.append(Cell(x=i,y=j+sectiondebt+4, type='route' , route='up'))
                elif (i-1)%6 == 0:
                    botAisle.append(Cell(x=i,y=j+sectiondebt+4, type='shelf'))
                elif (i-6)%6 == 0:
                    botAisle.append(Cell(x=i,y=j+sectiondebt+4, type='shelf'))
                else:
                    botAisle.append(Cell(x=i,y=j+sectiondebt+4, type='loading'))
            
            layout.append(botAisle)


        return layout
    
'''    def addTopAisle(self, x, y):
        #topsection=[shelf,load,up,down,load,shelf]
        newTopAisle = [Cell(x, y, type='shelf'), ]
    
    def addBottomAisle(self):

    def addMidAisle(self):'''




'''

warehouse = Warehouse()
print(warehouse.constructCatalog(120))
catalog = warehouse.constructCatalog(120)
print(warehouse.constructRandomTruckDelivery(catalog))
print(warehouse.constructWarehouseLayout(24, 16))'''