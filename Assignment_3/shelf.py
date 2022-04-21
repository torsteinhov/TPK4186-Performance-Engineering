from winreg import DisableReflectionKey
from numpy import product
from datetime import datetime
from math import floor
import numpy as np

class Shelf:

    def __init__(self, products=None):
        
        self.products = products
        self.max_weight = 100
        self.shelf_weight = 0

    def getShelfWeight(self):

        for product in self.products:

            self.shelf_weight += product.getWeight()

        return self.shelf_weight

    def getProducts(self):
        return self.products
    
    def getMax_weight(self):
        return self.max_weight