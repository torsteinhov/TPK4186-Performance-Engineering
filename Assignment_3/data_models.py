# This file contains data models for the simulation of the warehouse, and their functionalities

'''
Torstein Heltne Hovde
Lars Magnus Johnsen
Simen Eger Heggelund
'''

from winreg import DisableReflectionKey
from numpy import product
from datetime import datetime
from math import floor
import numpy as np

# Classes
'''
Type of products and catalogs
Deliveries
Products
Cells (storage cells, loading/unloading cells, route cells)
Robots
Client orders
'''

class Product:

    def __init__(self, serialnr, weight):

        self.serialnr = serialnr

        # premise: 40kg >= weight >= 2kg
        if weight <= 40 and weight >= 2:
            self.weight = weight
        
        else:
            raise ValueError("Weight does not have a valid value")
        
    def getSerialnr(self):
        return self.serialnr
        
    def setSerialnr(self, serialnr):
        self.serialnr = serialnr
    
    def getWeight(self):
        return self.weight
    
    def setWeight(self, weight):
        self.weight = weight

class Catalog:
    
    def __init__(self, products):

        self.products = products

    def __str__(self):

        string = 'The Catalog contains '+ str(len(self.products)) +' products: \n'

        for product in self.products:
            info = product.getSerialnr() + ' - ' + str(product.getWeight()) + 'kg \n'
            string += info

        return string
    
    def getProducts(self):
        return self.products

    def setProducts(self, products):
        self.products = products        
    
class Robot:
    # Max 40kg, can carry products of only one type at a time.

    def __init__(self, id, curr_pos, goal_pos, products=None):
        self.curr_pos = curr_pos #tuple (x,y)
        self.goal_pos = goal_pos #tuple (x,y)
        self.loadtime = 120
        self.movetime = 10
        self.id = id

        # Make sure that all the products are of the same type.
        type = product[0].getType()
        for product in products:
            if product.getType() != type:
                raise ValueError('The products are not the same type!')

        self.products = products
    
    def __str__(self):

        string = 'Robot: ' + str(self.id) + ' current position: ' + str(self.getCurrPos()) + ' goal position: ' + str(self.getGoalPos()) + ' \n'

        for product in self.products:
            info = product.getSerialnr() + ' - ' + str(product.getWeight()) + 'kg \n'
            string += info

        return string

    def getCurrPos(self):
        return self.curr_pos
    
    def setCurrPos(self, curr_pos):
        self.curr_pos = curr_pos
    
    def getGoalPos(self):
        return self.goal_pos
    
    def setGoalPos(self, goal_pos):
        self.goal_pos = goal_pos
    
    def getProducts(self):
        return self.products
    
    def setProducts(self, products):
        self.products = products

class Delivery:

    def __init__(self, products):

        self.date = datetime.today()
        self.products = products
    
    def __str__(self):

        string = 'Delivery: \n produced - ' + str(self.date)

        for product, amount in self.products.items():
            info = product.serialnr + ' - ' + str(floor(amount)) + ' units\n'
            string += info
        
        string += 'The total weight of the delivery: ' + str(self.getWeight()) + ' kg'

        return string
    
    def remove(self, product, amount):
        pass
    
    def add(self, product, amount):
        pass

    def getWeight(self):
        weight = 0
        for product in self.products.keys():
            weight += product.getWeight() * self.products[product]
        
        return weight
    
    def getDate(self):
        return self.date
    
    def getProducts(self):
        return self.products

    def setProducts(self, products):
        self.products = products
    
class Shelf:

    def __init__(self, product, amount):
        self.product = product
        # total weight can not exceed 100kg
        self.amount = amount
    
    def getProduct(self):
        return self.product
    
    def setProduct(self, product):
        self.product = product
    
    def getAmount(self):
        return self.amount
    
    def setAmount(self, amount):
        self.amount = amount

class Cell:

    def __init__(self, x, y, type, shelf1=None, shelf2=None, route=None):
        self.x = x
        self.y = y
        self.type = type
        self.shelf1 = shelf1 # only for storage cells
        self.shelf2 = shelf2 # only for storage cells
        self.route = route # route direction for route cells
    
    def getX(self):
        return self.x
    
    def setX(self, x):
        self.x = x
    
    def getY(self):
        return self.y
    
    def setY(self, y):
        self.y = y
    
    def getType(self):
        return self.type
    
    def setType(self, type):
        self.type = type
    
    def getShelf1(self):
        return self.shelf1
    
    def setShelf1(self, shelf1):
        self.shelf1 = shelf1
    
    def getShelf2(self):
        return self.shelf2
    
    def setShelf2(self, shelf2):
        self.shelf2 = shelf2
    
    def getRoute(self):
        return self.route
    
    def setRoute(self, route):
        self.route = route


class ClientOrder:
    pass # venter litt