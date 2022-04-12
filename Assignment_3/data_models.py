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

        string = 'The Catalog contains: \n'

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

    def __init__(self):
        pass

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
    
class Shelf:

    def __init__(self, product, amount):
        self.product = product
        # total weight can not exceed 100kg
        self.amount = amount

class Cell:

    def __init__(self, x, y, type, shelf1=None, shelf2=None, route=None):
        self.x = x
        self.y = y
        self.type = type
        self.shelf1 = shelf1 # only for storage cells
        self.shelf2 = shelf2 # only for storage cells
        self.route = route # route direction for route cells

class ClientOrder:
    pass # venter litt