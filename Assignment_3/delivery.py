from winreg import DisableReflectionKey
from numpy import product
from datetime import datetime
from math import floor
import numpy as np

class Delivery:

    def __init__(self, products):

        self.date = datetime.today()
        self.products = products
    
    def __str__(self):

        string = 'Delivery: \n produced - ' + str(self.date) +'\n'

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