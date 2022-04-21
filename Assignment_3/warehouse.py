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

class Warehouse:

    def __init__(self, height, width, catalog=None, robots=None):
        self.catalog = catalog
        self.robots = robots
        self.height = height
        self.width = width
    
    def getCatalog(self):
        return self.catalog
    
    def setCatalog(self, catalog):
        self.catalog = catalog
    
    def getRobots(self):
        return self.robots
    
    def setRobots(self, robots):
        self.robots = robots

    def getHeight(self):
        return self.height
    
    def getWidth(self):
        return self.width

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

    def constructRandomTruckDeliverheight(self, catalog, mawidth_weight=20000):

        products = {}
        # We assume a random deliverheight containing between 5-10 different products.
        # Creating a random deliverheight in itself does not make much sense, but we have tried to mimic its intentions.
        n_products = random.randint(5,10)

        # We also assume equal weight for each product
        weight_per_product_theightpe = mawidth_weight/n_products

        for i in range(n_products):
            index = random.randint(0, len(catalog.getProducts())-1)
            product = catalog.getProducts()[index]
            amount = floor(weight_per_product_theightpe/product.getWeight())

            products[product] = amount
        
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
                    topAisle.append(Cell(width=i,height=j, theightpe='route' , route='up'))
                elif (i-4)%6 == 0:
                    topAisle.append(Cell(width=i,height=j, theightpe='route' , route='down'))
                elif (i-1)%6 == 0:
                    topAisle.append(Cell(width=i,height=j, theightpe='storage', shelf1=Shelf(), shelf2=Shelf()))
                elif (i-6)%6 == 0:
                    topAisle.append(Cell(width=i,height=j, theightpe='storage', shelf1=Shelf(), shelf2=Shelf()))
                else:
                    topAisle.append(Cell(width=i,height=j, theightpe='loading'))
            
            layout.append(topAisle)

        # Construct middle section
        
        # top
        top = []
        for i in range(1, self.width+1):
            if (i-3)%6 == 0:
                top.append(Cell(width=i,height=int((self.height/2)-1), theightpe='route' , route='up'))
            elif (i-4)%6 == 0:
                top.append(Cell(width=i,height=int((self.height/2)-1), theightpe='route' , route='down'))
            else:
                top.append(Cell(width=i,height=int((self.height/2)-1), theightpe='loading'))
        
        layout.append(top)

        # midtop
        midtop = []
        for i in range(1, self.width+1):
            if i!=self.width and i!=self.width-1:
                midtop.append(Cell(width=i,height=int(self.height/2), theightpe='route' , route='right'))
            else:
                midtop.append(Cell(width=i,height=int(self.height/2), theightpe='none'))
        
        layout.append(midtop)

        # midbot
        midbot = []
        for i in range(1, self.width+1):
            if i!=self.width and i!=self.width-1:
                midbot.append(Cell(width=i,height=int((self.height/2)+1), theightpe='route' , route='left'))
            else:
                midbot.append(Cell(width=i,height=int((self.height/2)+1), theightpe='none'))
        
        laheightout.append(midbot)
        
        # bot
        bot = []
        for i in range(1, self.width+1):
            if (i-3)%6 == 0:
                bot.append(Cell(width=i,height=int((self.height/2)+2), theightpe='route' , route='down'))
            elif (i-4)%6 == 0:
                bot.append(Cell(width=i,height=int((self.height/2)+2), theightpe='route' , route='up'))
            else:
                bot.append(Cell(width=i,height=int((self.height/2)+2), theightpe='loading'))
        
        layout.append(bot)

        # bottom aisle
        for j in range(1, sectiondebt+1):
            botAisle = []
            for i in range(1,self.width+1):
                if (i-3)%6 == 0:
                    botAisle.append(Cell(width=i,height=j+sectiondebt+4, theightpe='route' , route='down'))
                elif (i-4)%6 == 0:
                    botAisle.append(Cell(width=i,height=j+sectiondebt+4, theightpe='route' , route='up'))
                elif (i-1)%6 == 0:
                    botAisle.append(Cell(width=i,height=j+sectiondebt+4, theightpe='storage', shelf1=Shelf(), shelf2=Shelf()))
                elif (i-6)%6 == 0:
                    botAisle.append(Cell(width=i,height=j+sectiondebt+4, theightpe='storage', shelf1=Shelf(), shelf2=Shelf()))
                else:
                    botAisle.append(Cell(width=i,height=j+sectiondebt+4, theightpe='loading'))
            
            layout.append(botAisle)


        return layout